
from fastapi import FastAPI, UploadFile, File
import pytesseract
from PIL import Image
import io
import camelot
import os

app = FastAPI()

# OCR endpoint
@app.post("/ocr/")
async def extract_text(file: UploadFile = File(...)):
    file_ext = os.path.splitext(file.filename)[1].lower()
    
    if file_ext in [".jpg", ".jpeg", ".png"]:
        # Extract text from images
        contents = await file.read()
        image = Image.open(io.BytesIO(contents))
        text = pytesseract.image_to_string(image)
        return {"extracted_text": text}
    
    elif file_ext == ".pdf":
        # Extract text and tables from PDF
        contents = await file.read()
        with open("temp.pdf", "wb") as f:
            f.write(contents)
        
        tables = camelot.read_pdf("temp.pdf", pages="all")
        table_data = [table.df.to_dict() for table in tables]
        
        os.remove("temp.pdf")
        
        return {"tables": table_data}
    
    else:
        return {"error": "Unsupported file format"}
