import os
from io import BytesIO 
from marker.converters.pdf import PdfConverter
from marker.models import create_model_dict
from marker.output import text_from_rendered,save_output

converter = PdfConverter(
    artifact_dict=create_model_dict(),
)

def make_markdown(file_stream: BytesIO, fname: str):
    """
    Converts PDF Byte Stream to Markdown format
    
    Args:
        file_stream: BytesIO

    Returns:
        str: Markdown content
    """
    try:
        output = f"Markdown/{fname}"

        os.makedirs(output, exist_ok=True)

        rendered = converter(file_stream)
        save_output(rendered, output, fname )
        text, _, images = text_from_rendered(rendered)

        return text
    except Exception as e:
        print("Error on making Markdown")