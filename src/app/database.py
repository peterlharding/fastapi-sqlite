import sqlalchemy as _sqla
import sqlalchemy.orm as _orm

from sqlalchemy.ext import declarative

# -----------------------------------------------------------------------------

SQLALCHEMY_DATABASE_URL = "sqlite:///./database.sqlite"

# -----------------------------------------------------------------------------

engine = _sqla.create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative.declarative_base()

# -----------------------------------------------------------------------------
