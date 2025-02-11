import qrcode
import argparse

def setup_argparse():
    parser = argparse.ArgumentParser(description='QR Code Generator')
    parser.add_argument('--data_to_be_encoded', type=str, help='Data to be encoded')
    return parser.parse_args()

def main():
    args = setup_argparse()

    if not args.data_to_be_encoded:
        print("Error: --data_to_be_encoded is required")
        return
    else:
        print(f"Generating QR Code for {args.data_to_be_encoded}")

        # Create a QR code object with a larger size and higher error correction
        qr = qrcode.QRCode(version=3, box_size=20, border=10, error_correction=qrcode.constants.ERROR_CORRECT_H)

        # Define the data to be encoded in the QR code
        data = args.data_to_be_encoded

        # Add the data to the QR code object
        qr.add_data(data)

        # Make the QR code
        qr.make(fit=True)

        # Create an image from the QR code with a black fill color and white background
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Save the QR code image
        img.save("outputs/qr_code.png")

if __name__ == "__main__":
    main()
