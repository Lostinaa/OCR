
# OCR Service with FastAPI

This project provides an Optical Character Recognition (OCR) service that allows users to extract text from images (JPG, PNG) and PDFs. The service is built using FastAPI and includes table detection for PDFs.

## Features
- **OCR for Images**: Extracts text from image files (e.g., JPG, PNG).
- **OCR for PDFs**: Extracts text from PDF files and detects/extracts tables using `Camelot`.
- **API Endpoint**: Simple POST `/ocr` API to upload a file and receive the extracted text or tables.
- **Docker Support**: Easily containerize the app with the provided Dockerfile.

## Setup

### Prerequisites
- **Python 3.9+**
- **Tesseract OCR** installed on your system (for OCR functionality)
- **Docker** (if you want to containerize the application)

### Installation

1. Clone the repository:
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Install **Tesseract** on your system:
    - On Ubuntu:
        ```bash
        sudo apt-get install tesseract-ocr
        ```
    - On MacOS (using Homebrew):
        ```bash
        brew install tesseract
        ```

4. Run the FastAPI server:
    ```bash
    uvicorn main:app --reload
    ```

### Usage

- **Endpoint**: `/ocr`
- **Method**: POST
- **Description**: Upload an image (JPG, PNG) or a PDF, and get extracted text or table data in JSON format.

#### Example Request
```bash
curl -X 'POST'   'http://127.0.0.1:8000/ocr/'   -H 'accept: application/json'   -H 'Content-Type: multipart/form-data'   -F 'file=@your_file.jpg'
```

### Docker Usage

1. Build the Docker image:
    ```bash
    docker build -t ocr-service .
    ```

2. Run the Docker container:
    ```bash
    docker run -p 8000:8000 ocr-service
    ```

### Advanced Feature: Table Detection
When a PDF is uploaded, the service attempts to detect tables and return them as structured data in JSON format.

## Optional Enhancements
- **Table Detection**: For extracting structured data from PDFs.
- **Dockerization**: Provided Dockerfile for containerizing the service.

## File Structure
```
.
├── main.py           # FastAPI app
├── Dockerfile        # Dockerfile to containerize the app
├── requirements.txt  # Project dependencies
└── README.md         # Project instructions
```
