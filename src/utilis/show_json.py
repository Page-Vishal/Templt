import os
import json

def show_json(file_name:str):
    """
    Retrieves the failename.json and reads and return json

    Args:
        filename.ext of original file

    Return:
        json format of Template/file_name.json
    """
    file_name,ext = os.path.splitext(file_name)
    with open( os.path.join("Template",file_name+".json"),"r") as f:
        json_format = json.load(f)

    return json_format