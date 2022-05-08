#!/usr/bin/env python3
# encoding: utf-8
#
#
# pylint disable=
# -----------------------------------------------------------------------------

from typing import List

from fastapi import (
    FastAPI,
    Depends,
    HTTPException,
)

import sqlalchemy.orm as _orm

from . import services as _services
from . import schemas as _schemas

# -----------------------------------------------------------------------------

description = """
This Sqlite FastAPI app provides a framework for you to investigate using SqlAlchemy with FastAPI. 🚀

## Users

You will be able to:

* **Insert users** (_not implemented_).
* **Read users** (_not implemented_).

## Addresses

You can **read addresses**.

"""

# -----------------------------------------------------------------------------


tags_metadata = [
    {
        "name": "users",
        "description": "Operations with users. The **login** logic is also here.",
    },
    {
        "name": "items",
        "description": "Manage items. So _fancy_ they have their own docs.",
        "externalDocs": {
            "description": "Items external docs",
            "url": "https://fastapi.tiangolo.com/",
        },
    },
]

# -----------------------------------------------------------------------------

app = FastAPI(
    title="Sqlite Sandbox",
    description=description,
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Sqlite",
        "url": "http://www.example.com/contact/",
        "email": "sqlite@example.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
    openapi_tags=tags_metadata,
)


# ============================================================================

@app.post("/users/", response_model=_schemas.User)
def create_user(user: _schemas.UserCreate,
                db: _orm.Session = Depends(_services.get_db)):

    db_user = _services.get_user_by_email(db=db, email=user.email)

    if db_user:
        raise HTTPException(
            status_code=400, detail="user already exists"
        )
    return _services.create_user(db=db, user=user)

# -----------------------------------------------------------------------------

@app.get("/users/", response_model=List[_schemas.User])
def read_users(limit: int = 10,
               db: _orm.Session = Depends(_services.get_db)):
    users = _services.get_users(db=db, limit=limit)
    return users

# -----------------------------------------------------------------------------

@app.get("/users/{user_id}", response_model=_schemas.User)
def read_user(user_id: int,
              db: _orm.Session = Depends(_services.get_db)):
    db_user = _services.get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(
            status_code=404, detail="user does not exist"
        )
    return db_user

# -----------------------------------------------------------------------------

@app.post("/users/{user_id}/addresses/", response_model=_schemas.Address)
def create_address(user_id: int,
                   address: _schemas.AddressCreate,
                   db: _orm.Session = Depends(_services.get_db)):
    db_user = _services.get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(
            status_code=404, detail="user does not exist"
        )
    return _services.create_address(db=db, address=address, user_id=user_id)

# -----------------------------------------------------------------------------

@app.get("/addresses/", response_model=List[_schemas.Address])
def read_addresses(limit: int = 10,
                   db: _orm.Session = Depends(_services.get_db)):
    addresses = _services.get_addresses(db=db, limit=limit)
    return addresses

# -----------------------------------------------------------------------------

@app.get("/addresses/{address_id}", response_model=_schemas.Address)
def read_address(address_id: int,
                 db: _orm.Session = Depends(_services.get_db)):
    address = _services.get_address(db=db, address_id=address_id)
    if address is None:
        raise HTTPException(
            status_code=404, detail="sorry this address does not exist"
        )

    return address

# -----------------------------------------------------------------------------

@app.delete("/addresses/{address_id}")
def delete_address(address_id: int,
                   db: _orm.Session = Depends(_services.get_db)):
    _services.delete_address(db=db, address_id=address_id)
    return {"message": f"successfully deleted address with id: {address_id}"}

# -----------------------------------------------------------------------------

@app.put("/addresses/{address_id}", response_model=_schemas.Address)
def update_address(address_id: int,
                   address: _schemas.AddressCreate,
                   db: _orm.Session = Depends(_services.get_db)):
    return _services.update_address(db=db, address=address, address_id=address_id)

# -----------------------------------------------------------------------------
