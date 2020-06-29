#!/usr/bin/env python3
"""
City module has class Amenity definition
"""
from models.base_model import BaseModel


class City(BaseModel):
    """City defines city's attributes and how it
    relates to other classes.
    Arguments:
        BaseModel {[BaseModel]} -- Inherits from BM
    """
    state_id = ""
    name = ""
