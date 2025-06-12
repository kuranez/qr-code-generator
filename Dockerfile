FROM python:3.12-slim

# Prevent .pyc files and enable unbuffered logging
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code and relevant folders
COPY app/ .
COPY app/assets/ ./assets/
COPY app/docs/ ./docs/

# Expose the application port
EXPOSE 5010

# Start the application
CMD ["panel", "serve", "qr-code-generator.py", "--address", "0.0.0.0", "--port", "5010", "--num-procs", "1", "--allow-websocket-origin=*", "--use-xheaders", "--log-level=info", "--prefix", "/qr-code-generator"]

# (No USER instruction here; set user at runtime!)