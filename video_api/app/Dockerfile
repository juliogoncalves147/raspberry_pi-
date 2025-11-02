FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py app.py
COPY videos/ videos/

RUN apt-get update && apt-get install -y ffmpeg

EXPOSE 5000

CMD ["python", "app.py"]
