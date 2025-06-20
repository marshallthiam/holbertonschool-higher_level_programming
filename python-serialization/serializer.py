import json

def serialize_to_json(data, filename):
    """
    Serialize a Python dictionary to a JSON file.

    Args:
        data (dict): The dictionary to serialize.
        filename (str): The name of the file to write to.
    """
    if not isinstance(data, dict):
        raise TypeError("Only dictionaries can be serialized with this module.")
    
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)
    print(f"Data serialized to {filename}")


def deserialize_from_json(filename):
    """
    Deserialize a JSON file to a Python dictionary.

    Args:
        filename (str): The name of the JSON file to read.

    Returns:
        dict: The deserialized dictionary.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)

    if not isinstance(data, dict):
        raise ValueError("The JSON file does not contain a dictionary.")
    
    print(f"Data deserialized from {filename}")
    return data
