#!/usr/bin/python3
""" initialize python pakage """
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
