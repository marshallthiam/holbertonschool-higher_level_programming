import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to an XML file.
    """
    root = ET.Element('data')
    for key, value in dictionary.items():
        item = ET.SubElement(root, 'item', key=key)
        item.text = str(value)
        item.set("type", type(value).__name__)  # Store type as attribute

    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserialize an XML file back into a Python dictionary.
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    result = {}

    for item in root.findall('item'):
        key = item.get('key')
        value_type = item.get('type')
        text = item.text

        # Convert text back to the appropriate type
        if value_type == 'int':
            result[key] = int(text)
        elif value_type == 'float':
            result[key] = float(text)
        elif value_type == 'bool':
            result[key] = text == 'True'
        else:
            result[key] = text

    return result
