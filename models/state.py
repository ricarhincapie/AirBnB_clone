#!/usr/bin/python3
"""
State module has class State definition
"""
from models.base_model import BaseModel


class State(BaseModel):
    """State defines attributes for the political
    unity defined as a State.

    Arguments:
        BaseModel {[Basemodel]} -- Inherits
    """
    name = ""
