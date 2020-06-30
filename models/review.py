#!/usr/bin/python3
"""
Review module has class Review definition
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review defines attributes for the platform
    places reviews module.
    Arguments:
        BaseModel {[BaseModel]} -- Inherits
    """
    place_id = ""
    user_id = ""
    text = ""
