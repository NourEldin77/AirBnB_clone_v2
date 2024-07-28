#!/usr/bin/python3
""" base model """

import models
import uuid
import datetime

class BaseModel:
    """
    parent class define all common attributes/methods for other class
    :Attributes:
    :methods:
        save: update date/time
        __str__: string repr for object
    """
    def __init__(self, *args, **kwargs):
        """
    constructor function for BaseModel class
    :param:
        id: getnrated universal unique identifier to object
        created_at: when object created
        updated_at: use save to updated the object date/time
    :return:
        void
    """
        if (kwargs):
            for key in kwargs.keys():
                if key == "created_at":
                    self.created_at = datetime.datetime.strptime(
                            kwargs['created_at'],
                            "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.updated_at = datetime.datetime.strptime(
                            kwargs['updated_at'],
                            "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "__class__":
                    continue
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def save(self):
        """ update time with current datetime"""
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        return dictionary containing all
        key: value of all attributes in object instance
        with some time and date in isoformat
        and class name attribute
        """
        obj = self.__dict__.copy()
        obj['__class__'] = self.__class__.__name__
        obj['created_at'] = self.created_at.isoformat()
        obj['updated_at'] = self.updated_at.isoformat()
        return (obj)

    def __str__(self):
        """
        Return a string representation of the obj to end usr

        returns a string containing basic info about object,
        including its class name, unique identifier (UUID), and attributes
        """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id,
                                      self.__dict__))

    def __cus__(self):
        obj = self.__dict__.copy()
        obj['created_at'] = self.created_at.isoformat()
        obj['updated_at'] = self.updated_at.isoformat()

        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id,
                                      obj))

