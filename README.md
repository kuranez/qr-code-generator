# QR Code Generator
A web-based tool built with `panel`and `qrcode` library that allows users to generate customized QR codes from URLs, with options to set error correction, size, colors, and download the generated image.

---

## 🌐 WebApp 

> **Try the interactive web app — create, customize, and download QR codes instantly, all in your browser.**
>
> 🟢 [https://apps.kuracodez.space/qr-code-generator/app](https://apps.kuracodez.space/qr-code-generator/app)

---

## Screenshot

> ![webapp.png](https://raw.githubusercontent.com/kuranez/qr-code-generator/refs/heads/main/screenshots/webapp_v.1.1.png)

---

## ⚙️ Features

> - Generate QR codes from any URL input.
> - Select error correction level (L, M, Q, H).
> - Customize QR code size and margin.
> - Choose foreground and background colors.
> - Preview QR code instantly.
> - Download QR code as PNG image.
> - Responsive web interface built with [Panel](https://panel.holoviz.org/index.html).

---

## 📦 Python Packages


**This script utilizes the following Python packages:**
> - `qrcode`: Used to generate QR codes from user-provided URLs with customizable options.
> - `panel`: Provides the interactive web interface for user input, QR code preview, and download functionality.

**Please ensure these packages are installed in your environment to enable full functionality of the code.**

---

## 📁 File Structure

```yaml
qr-code-generator/
|
├── app.py              # WebApp
├── requirements.txt    # Install requirements
├── assets/             # Logos
├── docs/               # Documentation
|
├── Dockerfile          # Docker files
├── docker-compose.yml
├── docker-compose.debug.yml
|
├── scripts/          # Version history, learning scripts
├── output/           # Output folder for static QR code generation
|
└── README.md
```

---

## ❓ How 2 Use

### 1. Install & Run Locally

```bash
# Clone the repository
git clone https://github.com/kuranez/qr-code-generator.git
cd qr-code-generator

# Install dependencies
pip install -r requirements.txt

# Start the app
panel serve app.py --port 5010
```
Visit [http://localhost:5010](http://localhost:5010) in your browser.

---

### 2. Run with Docker

```bash
# Build the Docker image
docker build -t qr-code-generator .

# Run the container
docker run -p 5010:5010 qr-code-generator
```
Open [http://localhost:5010](http://localhost:5010) to use the app.

---

## 📙 Documentation

**Visit the [Project Documentation Page](https://github.com/kuranez/qr-code-generator/blob/main/docs/qr-code-generator-documentation.md) for more info.** 

---

## 📕 Resources


- [Holoviz Panel](https://panel.holoviz.org/)
- [qrcode library on PyPI](https://pypi.org/project/qrcode/)
- [Docker Documentation](https://docs.docker.com/)

---

## 📘 License

This project is open source and available under the **MIT License**. 
You may modify, distribute, and use it freely in your own projects.

---