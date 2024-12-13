from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request
import cv2
import numpy as np
import os

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Image Filter Application</title>
</head>
<body>
    <h1>Upload an Image</h1>
    <form action="/upload" method="post" enctype="multipart/form-data">
        <input type="file" name="file" accept="image/*" required>
        <select name="filter">
            <option value="grayscale">Grayscale</option>
            <option value="blur">Blur</option>
            <option value="edge">Edge Detection</option>
        </select>
        <button type="submit">Apply Filter</button>
    </form>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return html_content

templates = Jinja2Templates(directory="templates")

@app.get("/image", response_class=HTMLResponse)
async def image_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/upload")
async def upload_image(file: UploadFile = File(...), filter: str = Form(...)):
    file_location = f"static/uploads/{file.filename}"
    with open(file_location, "wb") as f:
        f.write(await file.read())

    image = cv2.imread(file_location)

    if filter == "grayscale":
        processed_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    elif filter == "blur":
        processed_image = cv2.GaussianBlur(image, (15, 15), 0)
    elif filter == "edge":
        processed_image = cv2.Canny(image, 100, 200)
    else:
        return {"error": "Invalid filter"}
    
    processed_file_location = f"static/uploads/processed_{file.filename}"
    cv2.imwrite(processed_file_location, processed_image)

    return {"filename": processed_file_location}