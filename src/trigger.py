
print("Loading Model...\n")

import io
import os
from src.PDF2Markdown import make_markdown
from src.Markdown2Json import make_template
from src.utilis.filter_markdown import remove_backticks_and_json
from src.utilis.json_writer import json_writer

print("Model Loaded\n")

def trigger(file_name, file_bytes):

    try:
        print("file read\n")
        file_stream = io.BytesIO(file_bytes)

        file_name,_ = os.path.splitext(file_name)
        content = make_markdown(file_stream=file_stream,fname=file_name)

        print('Creating Template')
        template_draft = make_template(content)
        template = remove_backticks_and_json(template_draft)

        json_writer(filename=file_name, content=template)
        
        print("Over")
        # return template
    
    except Exception as e:
        print("Error on the program")