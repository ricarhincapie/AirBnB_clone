#!/usr/bin/env python3
"""
Amenity module has class Amenity definition
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity has a list with the property's
    ammenities.
    Arguments:
        BaseModel {[BaseModel]} -- Inherits from BM
    """
    name = ""
