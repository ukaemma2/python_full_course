#!/usr/bin/python3
"""Define class function called BaseModel cless"""

import uuid
from datetime import datetime

class BaseModel:
    """base models function call"""

    def __init__(self):
        
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def save(self):
        """update updated_at time to the current time"""
        self.updated_at = datetime.today ()

    def to_dict(self):
        """return a dict representation of this model instance 
        with the following fields: id, created_at, updated_at and className
        or key/value pairs 1for all fileds of the model instance 
        in the database
        """

        returned_dict = self.__dict__.copy()
        returned_dict["created_at"] = self.created_at.isoformat()
        returned_dict["updated_at"] = self.updated_at.isoformat()
        returned_dict["__class__"] = self.__class__.__name__
        return returned_dict


def __str__(self):
    className = self.__class__.__name__
    return "[{} ({}) {}]".format(className, self.id, self.__dict__)