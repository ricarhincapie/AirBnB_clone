#!/usr/bin/env python3

"""
This module create an instance of FileStorage
"""

from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
