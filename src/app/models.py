import sqlalchemy as _sqla
import sqlalchemy.orm as _orm

from datetime import datetime

from . import database as _database

# ============================================================================

class User(_database.Base):
    __tablename__   = "user"
    id              = _sqla.Column(_sqla.Integer, primary_key=True, index=True)
    username        = _sqla.Column(_sqla.String, unique=True, index=True)
    email           = _sqla.Column(_sqla.String, unique=True, index=True)
    hashed_password = _sqla.Column(_sqla.String)
    is_active       = _sqla.Column(_sqla.Boolean, default=True)

    addresses       = _orm.relationship("Address", back_populates="owner")

# ============================================================================

class Address(_database.Base):
    __tablename__ = "address"
    id            = _sqla.Column(_sqla.Integer, primary_key=True, index=True)
    address       = _sqla.Column(_sqla.String, index=True)
    city          = _sqla.Column(_sqla.String, index=False)
    state         = _sqla.Column(_sqla.String, index=False)
    postcode      = _sqla.Column(_sqla.String, index=False)
    coordinates   = _sqla.Column(_sqla.String, index=True)
    owner_id      = _sqla.Column(_sqla.Integer, _sqla.ForeignKey("user.id"))
    when_created  = _sqla.Column(_sqla.DateTime, default=datetime.utcnow)
    when_updated  = _sqla.Column(_sqla.DateTime, default=datetime.utcnow)

    owner = _orm.relationship("User", back_populates="addresses")

# ============================================================================
