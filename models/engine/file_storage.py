import json

class FileStorage:

    __file_path = 'file.json'
    __objects = {}

    def all(self):
       return FileStorage.__objects

    def new(self, obj):
        className = obj.__class__.__name__
        FileStorage.__objects['{}.{}'.format(className, obj.id)] = obj

    def save(self):
        otherdictionary = FileStorage.__objects
        objectDictionary = {obj: otherdictionary[obj].to_dict() for obj in objectDictionary.keys()}
        with open(FileStorage.__file_path, 'w') as file_handle:
            json.dump(objectDictionary, file_handle)

    def reload(self):
        try:
            with open(FileStorage.__file_path) as file_handle:
                objectDictionary = json.load(file_handle)
                for obj in objectDictionary.values():
                    className = obj["__class_-"]
                    del obj["__class__"]
                    self.new(eval(className)(objectDictionary))
        except FileNotFoundError:
            return