import os

def json_writer(filename:str, content:str):
    """
        Make the json form of template
    """
    # Define the file path and markdown content
    file_path = os.path.join("Template", filename +".json" )

    # Write to the file
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)