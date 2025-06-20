import pickle

class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the object to the specified file using pickle."""
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            print(f"Serialization failed: {e}")

    @classmethod
    def deserialize(cls, filename):
        """Deserialize an object from the specified file using pickle."""
        try:
            with open(filename, 'rb') as file:
                obj = pickle.load(file)
                if isinstance(obj, cls):
                    return obj
                else:
                    print("Deserialized object is not of type CustomObject.")
                    return None
        except Exception as e:
            print(f"Deserialization failed: {e}")
            return None
