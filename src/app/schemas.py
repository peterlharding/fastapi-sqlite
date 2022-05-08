#!/usr/bin/env python3
# encoding: utf-8
#
#
# pylint disable=
# -----------------------------------------------------------------------------

from typing import List, Optional
from datetime import datetime 
from pydantic import BaseModel

# ============================================================================

class _AddressBase(BaseModel):
    address: str
    city: str
    state: str
    postcode: str
    coordinates: str

# -----------------------------------------------------------------------------

class AddressCreate(_AddressBase):
    pass

# -----------------------------------------------------------------------------

class Address(_AddressBase):
    id: int
    owner_id: int
    when_created: datetime
    when_updated: datetime

    class Config:
        orm_mode = True

# ============================================================================

class _UserBase(BaseModel):
    username: str
    email: str
    name: Optional[str]

# -----------------------------------------------------------------------------

class UserCreate(_UserBase):
    password: str

# -----------------------------------------------------------------------------

class User(_UserBase):
    id: int
    is_active: bool
    addresses: List[Address] = []

    class Config:
        orm_mode = True

# ============================================================================
