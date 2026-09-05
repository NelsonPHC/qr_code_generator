# QR Code Generator

A small Python CLI that generates QR code PNG images from URLs.

## Requirements

- Python 3.8+
- [`qrcode`](https://pypi.org/project/qrcode/) with Pillow support (`qrcode[pil]`)

## Installation

Install dependencies only:

```bash
pip install -r requirements.txt
```

Or install the project as an editable package to get the `qr-code-generator` command:

```bash
pip install -e .
```

## Usage

Generate a QR code by passing a URL:

```bash
python qrcode_generator.py --url "https://example.com"
```

After installing with `pip install -e .`, you can use the CLI entry point:

```bash
qr-code-generator --url "https://example.com"
```

### Options

| Option | Description | Default |
|--------|-------------|---------|
| `--url` | URL to encode in the QR code | Prompts interactively if omitted |
| `--output` | Output PNG filename | `qr_code.png` |

### Examples

Save to a custom filename:

```bash
python qrcode_generator.py --url "https://example.com" --output my_qr.png
```

Run without `--url` to enter a URL interactively:

```bash
python qrcode_generator.py
```

## Output

The tool writes a black-and-white PNG QR code to the file specified by `--output` (default: `qr_code.png`).
