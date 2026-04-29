FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Generate a self-signed SSL certificate directly inside the container!
RUN apt-get update && apt-get install -y openssl && \
    openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365 -subj "/CN=localhost"

COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
