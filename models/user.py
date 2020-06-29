#!/usr/bin/env python3
"""
User module has class User definition
"""
from models.base_model import BaseModel


class User(BaseModel):
    """User defines platform user's attributes
    Arguments:
        BaseModel {[BaseModel]} -- Inherits
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
