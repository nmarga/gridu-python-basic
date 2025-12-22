import json
import os
from pathlib import Path
import xml.etree.ElementTree as ET
import xml.dom.minidom

def dict_to_xml(tag: str, d: dict) -> ET.Element:
    """Convert a dictionary to an ElementTree element."""
    elem = ET.Element(tag)
    for key, val in d.items():
        if isinstance(val, dict):
            elem.append(dict_to_xml(key, val))
        elif isinstance(val, list):
            for item in val:
                elem.append(dict_to_xml(key, item if isinstance(item, dict) else { 'value': item }))
        else:
            child = ET.Element(key)
            child.text = str(val)
            elem.append(child)
    return elem

def pretty_format_xml(element: ET.Element):
    """Returns a pretty-printed XML string for the Element."""
    ET.indent(element, space=" ")
    fomrated_string = ET.tostring(element, encoding='unicode')
    return fomrated_string

def json_to_xml(src_path: str, xml_path: str) -> None:
    """Function to create an XML file for Spain for 2021-09-25"""
    for dir_path in os.listdir(src_path):
        json_path = Path(os.path.join(src_path, dir_path))
        print(dir_path)
        for file_path in json_path.rglob("*.json"):
            print(f"Found file: {file_path}")
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                data_dict = json.loads(content)
                #print(data_dict)
            print(pretty_format_xml(dict_to_xml('root', data_dict)))

if __name__ == "__main__":
    json_to_xml('source_data', '.')
