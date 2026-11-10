# app/qr-code-generator.py

# QR Code Generator Application
# This script creates a simple QR code generator using the Panel library and qrcode package.
# It allows users to input a URL, customize QR code appearance, and download the generated QR code image.

# Imports
# Path for Filepaths
from pathlib import Path
# io for handling in-memory file operations
import io
# qrcode for generating QR codes
import qrcode
# qrcode.constants for error correction constants
from qrcode.constants import ERROR_CORRECT_L, ERROR_CORRECT_M, ERROR_CORRECT_Q, ERROR_CORRECT_H
# Panel for creating the web application
import panel as pn

# File Paths

# Base directory of app.py
BASE_DIR = Path(__file__).parent

# Paths to assets and markdown files
logo_path = BASE_DIR / "assets" / "logo.png"
image_path = BASE_DIR / "assets" / "qrapp.png"
doc_path = BASE_DIR / "docs" / "documentation.md"
help_path = BASE_DIR / "docs" / "help" / "advanced-options.md"

# Read the documentation content
doc_content = doc_path.read_text(encoding="utf-8")
help_content = help_path.read_text(encoding="utf-8")

# Input Widgets
url_input = pn.widgets.TextInput(name='URL', value="https://github.com/kuranez/qr-code-generator")
generate_button = pn.widgets.Button(name='Generate QR Code', button_type='primary')

fill_color_picker = pn.widgets.ColorPicker(name='QR Color', value='#000000')  # Black by default
back_color_picker = pn.widgets.ColorPicker(name='BG Color', value='#ffffff')  # White by default

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
    callback=lambda: io.BytesIO(download_buf.getvalue()),
    # embed=True,  # Embed the file in the download button    
)

# Function to generate QR code
def generate_qr(event):
    url = url_input.value
    version = version_input.value
    error_correction = error_correction_input.value
    box_size = box_size_input.value
    border = border_input.value
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

    # Save to an in-memory buffer for download and display
    download_buf.seek(0)
    download_buf.truncate()
    img.save(download_buf, format='PNG')
    download_buf.seek(0)

    # Update the QR display pane with the new image
    qr_display.object = download_buf.getvalue()


# Bind function to button clock
generate_button.on_click(generate_qr)

# MD pane
doc_markdown = pn.pane.Markdown(doc_content, width=600, height=650)

# Create a FloatingPanel to wrap MD
doc_panel = pn.FloatPanel(
    doc_markdown,
    name="Documentation & Help",
    width=650,
    height=700,
    margin=20,
)

# Create buttons for docs
doc_button = pn.widgets.Button(
    name="Check the documentation 🢅",
    button_type="primary",
    # sizing_mode='stretch_width',
    width=300,
    align='center',
)

help_button = pn.widgets.Button(
    name="Help 🢅",
    button_type="primary",
    width=300,
    align='center',
)

# Initially hide the documentation panel
doc_panel.visible = False

# Toogle Help / Documentation Panel

def toggle_doc(event):
    # If doc already open, close it; otherwise switch to doc and show
    if doc_panel.visible and doc_markdown.object == doc_content:
        doc_panel.visible = False
    else:
        doc_markdown.object = doc_content
        doc_panel.visible = True

def toggle_help(event):
    # If help already open, close it; otherwise switch to help and show
    if doc_panel.visible and doc_markdown.object == help_content: 
        doc_panel.visible = False
    else:
        doc_markdown.object = help_content
        doc_panel.visible = True

# Callback for both buttons
doc_button.on_click(toggle_doc)
help_button.on_click(toggle_help)

# Layout widgets
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

template = pn.template.MaterialTemplate(
    title='QR Code Generator',
    logo=str(logo_path),
    sidebar=[pn.pane.Markdown("## Advanced Options:"),
             version_input,
             error_correction_input,
             box_size_input,
             border_input,
             help_button,
             pn.Row(),
             pn.pane.Markdown("## Info:"),
             pn.pane.Markdown("This is a simple QR Code Generator application built with **`panel`** and **`qrcode`** library. " \
             "You can generate QR codes for any URL and customize their appearance."),
             pn.pane.Markdown("In addition to the basic options, you can also adjust the version, error correction level, box size, and border size of the QR code."),
             pn.pane.Markdown("## Source `code`:"),
             pn.pane.Markdown("[https://github.com/kuranez/qr-code-generator](https://github.com/kuranez/qr-code-generator)"),
             doc_button,
             pn.Row(),
             pn.pane.PNG(image_path, width=300, height=300, align='center'),
            ],
)

# Add the main application layout to the template
template.main.append(
    pn.Row(
        pn.Column(
            pn.pane.Markdown("## Enter a `URL` to generate a QR code:"),
            pn.Row(url_input, fill_color_picker, back_color_picker),
            pn.Row(generate_button, download_button),
            qr_display,
            align='center',
        ),
        pn.Column(
            doc_panel,
        )
    )
)

# Serve the application
template.servable();

# Main function wrapper

def main():
    pn.serve(template, port=5010, show=True)


if __name__ == "__main__":
    main()