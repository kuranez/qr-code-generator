## Advanced QR Code Options


### Version

- Ranges from 1 (21x21 matrix, smallest) to 40 (177x177, largest).
- Higher versions store more data but make the code denser.

### Error Correction

- Controls how much of the code can be obscured and still be scanned.
    - L: ~7% recovery
    - M: ~15% recovery (default)
    - Q: ~25% recovery
    - H: ~30% recovery (most robust, less capacity)


### Box Size

- Size of each box (pixel) in the QR code image.
- Controls the output image resolution.


### Border

- Width (in boxes) of the white border.
- Standard minimum is 4; increasing helps with scanning reliability.