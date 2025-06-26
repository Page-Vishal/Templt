
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse,JSONResponse

from src.trigger import trigger
from src.utilis.check_PDF import check_PDF
from src.utilis.load_HTML import load_content
from src.utilis.show_json import show_json
app = FastAPI()

@app.post("/pdf")
async def upload_pdf(file: UploadFile = File(...)):

    check_PDF(file)

    file_name = file.filename
    file_bytes = await file.read()

    trigger(file_name,file_bytes)
    JSON = show_json(file_name)
    return JSONResponse(content=JSON)

@app.get("/")
async def main():

    content = load_content()
    return HTMLResponse(content=content)