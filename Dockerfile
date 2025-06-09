FROM python:3-slim

# Prevent .pyc files and enable unbuffered logging
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system dependencies (optional, add/remove as needed)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app/ .

# Create non-root user and set permissions
RUN useradd -m appuser && chown -R appuser /app

# Ensure output directory exists and is owned by appuser
RUN mkdir -p /app/output && chown -R appuser /app


# Switch to non-root user
USER appuser

# Expose the application port
EXPOSE 5010

# Start the application
CMD ["panel", "serve", "qr-code-generator.py", "--address", "0.0.0.0", "--port", "5010", "--num-procs", "1", "--allow-websocket-origin=*", "--use-xheaders", "--log-level=info"]
