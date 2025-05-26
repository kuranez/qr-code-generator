FROM python:3-slim

# No .pyc-files and live-logging
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy requirements.txt first (better Cache)
COPY app/requirements.txt .

# Install packages
RUN pip install --no-cache-dir -r requirements.txt

# Add non-root user
RUN useradd -m appuser

# Use non-root user from now on
USER appuser

# Copy rest of application files
COPY app/ .

# Exposed port
EXPOSE 5010

# Start the application
# CMD ["panel", "serve", "qr-code-generator.py", "--address", "0.0.0.0", "--port", "5010", "--num-procs", "1", "--allow-websocket-origin=*", "--use-xheaders", "--log-level=info"]
CMD ["panel", "serve", "qr-code-generator.py", "--address", "0.0.0.0", "--port", "5010", "--num-procs", "4", "--allow-websocket-origin=vigilant-davinci.217-154-75-75.plesk.page", "--use-xheaders", "--log-level=info"]

