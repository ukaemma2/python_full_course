import json

class FileStorage:

    __file_path = 'file.json'
    __objects = {}

    def all(self):
       return self.__objects

    def new(self, obj):
        className = obj.__class__.__name__
        self.__objects['{}.{}'.format(className, obj.id)] = obj

    def save(self):
