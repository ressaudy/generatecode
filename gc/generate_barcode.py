
import barcode
from barcode.writer import ImageWriter

def generate_barcode(data, filename):
    """
    Generate a barcode image from the given data and save it to a file.

    Args:
        data (str): The data to encode in the barcode.
        filename (str): The filename to save the barcode image (without extension).
    """
    # Use Code128 barcode format
    CODE128 = barcode.get_barcode_class('code128')
    
    # Generate barcode with ImageWriter to create an image file (PNG)
    code128 = CODE128(data, writer=ImageWriter)

    # Save barcode as PNG file
    fullname = code128.save(filename)
    print(f"Barcode saved to {fullname}")

if __name__ == "__main__":
    sample_data = "123456789012"
    output_file = "barcode"
    generate_barcode(sample_data, output_file)