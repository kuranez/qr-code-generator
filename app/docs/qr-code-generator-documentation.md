# QR Code Generator Documentation

This guide showcases how to generate QR codes in Python, starting from the most basic script, progressing through notebook-based customization, and culminating in a full-featured interactive web app using Panel.

---

## Table of Contents

1. [Introduction](#introduction)
2. [Basic QR Code Generation (Script/Notebook)](#basic-qr-code-generation)
    - [Minimal Example](#minimal-example)
    - [Customizing Output Directory](#customizing-output-directory)
    - [Debugging Output](#debugging-output)
    - [Displaying QR Codes in Jupyter](#displaying-qr-codes-in-jupyter)
3. [Interactive QR Code Generator App](#interactive-qr-code-generator-app)
    - [App Overview](#app-overview)
    - [Core Features](#core-features)
    - [Advanced Options Explained](#advanced-options-explained)
    - [Component Structure](#component-structure)
4. [Deploying the App](#deploying-the-app)
    - [Install Requirements](#install-requirements)
    - [Running with Panel](#running-with-panel)
    - [Docker Deployment](#docker-deployment)
5. [References](#references)

---

## Introduction

This project demonstrates generating QR codes in Python using the `qrcode` library, from a simple script to a modern web application with Panel. The tools and techniques shown enable both quick code generation and advanced customization for broader use cases.

**Project Repository:**  
[https://github.com/kuranez/qr-code-generator](https://github.com/kuranez/qr-code-generator)

---

## Basic QR Code Generation

The simplest way to generate a QR code is with a few lines of Python using the `qrcode` library.

### Minimal Example

```python
import qrcode

url = "https://github.com/kuranez/QR-Code-Generator"
qr_img = qrcode.make(url)
qr_img.save("example_qr.png")
```

This generates a black-and-white QR code for the input URL and saves it as `example_qr.png`.

### Customizing Output Directory

To ensure your QR codes are saved in a specific directory:

```python
import os
import qrcode

output_dir = "./output"
os.makedirs(output_dir, exist_ok=True)
file_path = os.path.join(output_dir, "example_qr.png")

url = "https://github.com/kuranez/QR-Code-Generator"
qr_img = qrcode.make(url)
qr_img.save(file_path)
```

### Debugging Output

Check the current directory and files in your output location:

```python
print("Current working directory:", os.getcwd())
print("Contents of output directory:", os.listdir(output_dir))
```

### Displaying QR Codes in Jupyter

If using Jupyter, display the QR code image with Panel:

```python
import panel as pn
pn.extension()
qr_display = pn.pane.Image(file_path, width=500, height=500)
qr_display
```

---

## Interactive QR Code Generator App

### App Overview

The QR Code Generator App is a user-friendly web application built with [Panel](https://panel.holoviz.org/) and `qrcode`. It allows users to:

- Enter any URL
- Customize QR code colors
- Adjust advanced QR parameters
- Preview and download the generated QR code

### Core Features

- **URL Input**: Enter the link or text to encode.
- **Color Pickers**: Customize foreground (QR) and background colors.
- **Advanced Options**:
    - Version (size)
    - Error correction
    - Box size (pixel size)
    - Border width
- **Instant Preview**: See the QR code update dynamically.
- **Download**: Save the QR code as a PNG.

### Advanced Options Explained

**Version**

- Ranges from 1 (21x21 matrix, smallest) to 40 (177x177, largest).
- Higher versions store more data but make the code denser.

**Error Correction**

- Controls how much of the code can be obscured and still be scanned.
    - L: ~7% recovery
    - M: ~15% recovery (default)
    - Q: ~25% recovery
    - H: ~30% recovery (most robust, less capacity)

**Box Size**

- Size of each box (pixel) in the QR code image.

**Border**

- Width (in boxes) of the white border.
- Standard minimum is 4; increasing helps with scanning reliability.

### Component Structure

The app is modular and structured as follows:

1. **Initialization Layer**
    - Imports, Panel extension activation, output and asset directory setup.
2. **UI Widgets Layer**
    - URL input, color pickers, sliders/selects for advanced options.
3. **Logic Layer**
    - QR code generation function (reads widget values, creates PNG).
4. **Output Layer**
    - Preview pane for QR code, download button.
5. **Presentation Layer**
    - Layout with `pn.Column` and/or `MaterialTemplate` for a modern look.

#### Example: Main App Layout (Panel)

```python
app = pn.Column(
    "## QR Code Generator",
    url_input, 
    pn.Row(fill_color_picker, back_color_picker),
    pn.pane.Markdown("### Advanced Options:"),
    version_input,
    error_correction_input,
    box_size_input,
    border_input,
    generate_button,
    download_button,
    qr_display
)
```

Or, for a more sophisticated UI, use Panel's `MaterialTemplate`:

```python
template = pn.template.MaterialTemplate(
    title='QR Code Generator',
    sidebar=[...],  # advanced options, info, links
)
template.main.append(
    pn.Column(
        pn.pane.Markdown("### Enter a URL to generate a QR code:"),
        pn.Row(url_input, fill_color_picker, back_color_picker),
        pn.Row(generate_button, download_button),
        qr_display
    )
)
template.servable()
```

---

## Deploying the App

You can deploy the QR Code Generator App either by installing dependencies and running Panel directly, or by running everything in a Docker container.

### Install Requirements

First, ensure you have Python 3.8+ and `pip` installed.  
Install the required Python packages:

```bash
pip install -r app/requirements.txt
```

### Running with Panel

After installing requirements, launch the Panel server:

```bash
cd app
panel serve qr-code-generator.py --address 0.0.0.0 --port 5010 --allow-websocket-origin=*
```

- By default, the app will be available at [http://localhost:5010](http://localhost:5010).
- You can change the port or adjust other options as needed.

**Tip:**  
On your own server, add `--prefix=/qr-code-generator` if you want the app at a subpath.

### Docker Deployment

A `Dockerfile` is included for easy deployment.  
Build and run the app with:

```bash
docker build -t qr-code-generator .
docker run -p 5010:5010 qr-code-generator
```

- The app will be served at [http://localhost:5010/qr-code-generator](http://localhost:5010/qr-code-generator).
- You can deploy this on any machine with Docker installed.

**Environment Variables:**  
You can set environment variables like `PYTHONDONTWRITEBYTECODE` and `PYTHONUNBUFFERED` (already configured in the Dockerfile).

---

## References

- [qrcode library documentation](https://pypi.org/project/qrcode/)
- [Panel documentation](https://panel.holoviz.org/)
- [Project GitHub](https://github.com/kuranez/QR-Code-Generator)

---

## Quick Start

- Try the [minimal script](#minimal-example) to generate a QR code in seconds.
- Use the [interactive app](#interactive-qr-code-generator-app) for full customization.
- [Deploy the app](#deploying-the-app) on your machine or server.

---

**Author**: [kuranez](https://github.com/kuranez)  
**License**: MIT  