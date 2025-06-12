# app/qr-code-generator.py

# QR Code Generator Application
# This script creates a simple QR code generator using the Panel library and qrcode package.
# It allows users to input a URL, customize QR code appearance, and download the generated QR code image.

# Imports

# os for file path management
import os
# io for handling in-memory file operations
import io
# qrcode for generating QR codes
import qrcode
# qrcode.constants for error correction constants
from qrcode.constants import ERROR_CORRECT_L, ERROR_CORRECT_M, ERROR_CORRECT_Q, ERROR_CORRECT_H
# Panel for creating the web application
import panel as pn

# Activate Panel extension (necessary in Jupyter notebooks)
pn.extension()

# File Paths
# output/ # Ensure the output directory exists
output_dir = os.path.join(os.path.dirname(__file__), "output")
os.makedirs(output_dir, exist_ok=True)
# qr_code.png # Path to save the generated QR code image
file_path = os.path.join(output_dir, "qr_code.png")
# assets/ # Ensure the assets directory exists
assets_dir = os.path.join(os.path.dirname(__file__), "assets")
os.makedirs(assets_dir, exist_ok=True)
# logo.png and qrapp.png # Paths to the logo and image assets
logo_path = os.path.join(assets_dir, "logo.png")
image_path = os.path.join(assets_dir, "qrapp.png")

# Input Widgets
url_input = pn.widgets.TextInput(name='URL', value="https://github.com/kuranez/QR-Code-Generator")
generate_button = pn.widgets.Button(name='Generate QR Code', button_type='primary')

fill_color_picker = pn.widgets.ColorPicker(name='QR Color', value='#000000')  # Black by default
back_color_picker = pn.widgets.ColorPicker(name='Background Color', value='#ffffff')  # White by default

# Advanced Options
version_input = pn.widgets.IntSlider(name='Version (1-40)', start=1, end=40, value=1, step=1)
error_correction_input = pn.widgets.Select(
    name='Error Correction',
    options={
        'Low (7%)': ERROR_CORRECT_L,
        'Medium (15%)': ERROR_CORRECT_M,
        'Quartile (25%)': ERROR_CORRECT_Q,
        'High (30%)': ERROR_CORRECT_H
    },
    value=ERROR_CORRECT_H  # Default to highest correction
)
box_size_input = pn.widgets.IntSlider(name='Box Size (pixels)', start=1, end=20, value=10, step=1)
border_input = pn.widgets.IntSlider(name='Border (minimum 4)', start=1, end=10, value=4, step=1)

# Placeholder Image
qr_display = pn.pane.PNG(width=500, height=500)

# Generate QR Code on click
download_buf = io.BytesIO()
def get_file():
    return download_buf.getvalue()


download_button = pn.widgets.FileDownload(
    filename="qr_code.png", 
    button_type="success",
    file=get_file
)

def generate_qr(event):
    url = url_input.value
    version = int(version_input.value)
    error_correction = int(error_correction_input.value)
    box_size = int(box_size_input.value)
    border = int(border_input.value)
    fill_color = fill_color_picker.value
    back_color = back_color_picker.value

    # Create QR code with specified options
    qr = qrcode.QRCode(
        version=version,
        error_correction=error_correction,
        box_size=box_size,
        border=border,
    )

    qr.clear()  # Clear any previous data to ensure a fresh QR code
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    
    # Save the QR code image to a file
    # img.save(file_path)

    # Save to an in-memory buffer for download and display
    download_buf.seek(0)
    download_buf.truncate()
    img.save(download_buf, format='PNG')
    download_buf.seek(0)

    # Update the QR display pane with the new image
    qr_display.object = download_buf.getvalue()


# Bind function to button clock
generate_button.on_click(generate_qr)

# Download Button
download_button = pn.widgets.FileDownload(
    filename="qr_code.png", 
    button_type="success",
    file=file_path
)

# Layout widgets
app = pn.Column(
    "## QR Code Generator",
    url_input, 
    pn.Row(fill_color_picker,back_color_picker),
    pn.pane.Markdown("### Advanced Options:"),
    version_input,
    error_correction_input,
    box_size_input,
    border_input,
    generate_button,
    download_button,
    qr_display
)

# Display App
# app

template = pn.template.MaterialTemplate(
    title='QR Code Generator',
    logo=logo_path,
    sidebar=[pn.pane.Markdown("### Advanced Options:"),
             version_input,
             error_correction_input,
             box_size_input,
             border_input,
             pn.Spacer(),
             pn.pane.Markdown("### Info:"),
             pn.pane.Markdown("This is a simple QR Code Generator application built with **`panel`** and **`qrcode`** library."),
             pn.pane.Markdown("You can generate QR codes for any URL and customize their appearance."),
             pn.pane.Markdown("In addition to the basic options, you can also adjust the version, error correction level, box size, and border size of the QR code."),
             pn.pane.Markdown("**Check the documentation for more details.**"),
             pn.Spacer(),
             pn.pane.Markdown("### Source Code:"),
             pn.pane.Markdown("[https://github.com/kuranez/QR-Code-Generator](https://github.com/kuranez/QR-Code-Generator)"),
             pn.layout.HSpacer(),
             pn.pane.PNG(image_path, width=320, height=320, align='center'),
             pn.layout.HSpacer()
            ],
)

template.main.append(
    pn.Column(
        pn.pane.Markdown("### Enter a URL to generate a QR code:"),
        pn.Row(url_input, fill_color_picker,back_color_picker),
        pn.Row(generate_button, download_button),
        qr_display
    )
)

template.servable();