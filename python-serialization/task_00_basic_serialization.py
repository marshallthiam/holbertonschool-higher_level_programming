import json

def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary to JSON and saves it to a file.

    Args:
        data (dict): The dictionary to serialize.
        filename (str): The path to the file where the JSON will be saved.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def load_and_deserialize(filename):
    """
    Loads and deserializes JSON data from a file back into a Python dictionary.

    Args:
        filename (str): The path to the JSON file to read.

    Returns:
        dict: The deserialized dictionary.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
