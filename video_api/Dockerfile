FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies (compiler + ffmpeg for moviepy later)
RUN apt-get update && apt-get install -y \
    build-essential \
    ffmpeg \
    libsm6 \
    libxext6 \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY app/requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY app/ .

EXPOSE 5000

CMD ["python", "app.py"]
