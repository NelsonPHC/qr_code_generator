# This application expects the 'qrcode' package (with 'pil' support) to be pre-installed:
# pip install qrcode[pil]

import qrcode
import argparse
import os

def generate_qr_code_app(url, output_filename="qr_code.png"):
    """
    Generates a QR code from a URL and saves it to a file.
    """
    if not url:
        print("Error: A URL must be provided to generate a QR code.")
        return

    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        # Save the image directly to the specified file
        img.save(output_filename, format='PNG')

        print(f"Generated QR code for: {url}")
        print(f"QR code saved to: {output_filename}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a QR code from a URL.")
    parser.add_argument("--url", help="The URL to generate the QR code for.")
    parser.add_argument("--output", default="qr_code.png",
                        help="Output filename for the QR code image (default: 'qr_code.png').")

    # Use parse_args() for general Python applications; parse_known_args() is for environments like Colab/Jupyter.
    args = parser.parse_args()

    target_url = args.url

    if not target_url:
        # Fallback to interactive input if no URL was provided via --url argument
        print("No URL provided via '--url' argument.")
        target_url = input("Please enter the URL to generate a QR code for: ")
        if not target_url:
            print("No URL entered. Exiting.")
            exit() # Terminate if no URL is provided interactively

    generate_qr_code_app(target_url, args.output)