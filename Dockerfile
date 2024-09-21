
# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install required dependencies
RUN apt-get update && apt-get install -y tesseract-ocr
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get install -y ghostscript python3-opencv

# Expose port 8000
EXPOSE 8000

# Run FastAPI on container start
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
