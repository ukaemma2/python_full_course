#!/usr/bin/python3
"""Define class function called BaseModel cless"""

from asyncio.windows_events import NULL
import uuid
from datetime import datetime
import models


class BaseModel:
    """base models function call"""

    def __init__(self, *args, **kwargs):

        time_frame = "%Y-%m-%dT%H:%M:%S.%f"
        
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        if len(kwargs) != ' ':
            for k, v in kwargs.items():
                if k == 'created_at' or k == 'updated_at':
                    self.__dict__[k] = datetime.strptime(v, time_frame)
                else:
                    self.__dict__[k] = v

        else: 
            models.storage.new(self)

    def save(self):
        """update updated_at time to the current time""" 
        self.updated_at = datetime.today ()
        models.storage.save()
 
    def to_dict(self):
        """return a dict representation of this model instance 
        with the following fields: id, created_at, updated_at and className
        or key/value pairs for a ll fileds of the model instance 
        in the database
        """

        returned_dict = self.__dict__.copy()
        returned_dict["created_at"] = self.created_at.isoformat()
        returned_dict["updated_at"] = self.updated_at.isoformat()
        returned_dict["__class__"] = self.__class__.__name__
        return returned_dict


    def __str__(self):
        className = self.__class__.__name__
        return "[{}] ({}) {}".format(className, self.id, self.__dict__)