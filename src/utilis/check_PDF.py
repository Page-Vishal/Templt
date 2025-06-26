
from fastapi import UploadFile, HTTPException

def check_PDF(file: UploadFile):
    """
        Input:
            Takes file as input to check if PDF or not

    """
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF files are allowed.")
