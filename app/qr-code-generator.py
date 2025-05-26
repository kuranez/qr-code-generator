import os
import qrcode
import panel as pn

# Activate Panel extension (necessary in Jupyter notebooks)
pn.extension()

# Output directory and file path
output_dir = "./output"
os.makedirs(output_dir, exist_ok=True)
file_path = os.path.join(output_dir, "qr_code.png")

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
        'Low (7%)': qrcode.constants.ERROR_CORRECT_L,
        'Medium (15%)': qrcode.constants.ERROR_CORRECT_M,
        'Quartile (25%)': qrcode.constants.ERROR_CORRECT_Q,
        'High (30%)': qrcode.constants.ERROR_CORRECT_H
    },
    value=qrcode.constants.ERROR_CORRECT_H  # Default to highest correction
)
box_size_input = pn.widgets.IntSlider(name='Box Size (pixels)', start=1, end=20, value=10, step=1)
border_input = pn.widgets.IntSlider(name='Border (minimum 4)', start=1, end=10, value=4, step=1)

# Placeholder Image
qr_display = pn.pane.Image(width=500, height=500)

# Generate QR Code on click
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
    img = qr.make_image(fill_color=fill_color, back_color=back_color).convert('RGB')
    img.save(file_path)
    qr_display.object = None  # Clear previous image (helps prevent caching)
    qr_display.object = file_path  # Update the display

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
    sidebar=[pn.pane.Markdown("### Advanced Options:"),
             version_input,
             error_correction_input,
             box_size_input,
             border_input,
             pn.pane.Markdown("### Info:"),
             pn.pane.Markdown("[https://github.com/kuranez/QR-Code-Generator](https://github.com/kuranez/QR-Code-Generator)"),
            ],
)

template.main.append(
    pn.Column(
        pn.Row(url_input, fill_color_picker,back_color_picker),
        pn.Row(generate_button, download_button),
        qr_display
    )
)

template.servable();