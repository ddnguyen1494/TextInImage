import os
import sys
from PIL import Image
from bitarray import bitarray

HELP_MESSAGE = """
    Name:
        Steganography -- Embed/Extract text in image.

    Description:
        * The steganography utility either extracts text from image and print to standard output or embed text file in images.
        * The input image should be in jpg format.
        * Output is either the embedded message or a new image in png format.

    Usage:
        python StegaImage.py -x input_image: Extract message from input_image
        python StegaImage.py -e input_text_file input_image: Embed input_text_file in input_image

    Example:
        python StegaImage.py -x ./TestImages/meme.png
        python StegaImage.py -e StegaImage.py ./TestImages/meme.jpg
    """

def replace_least_sig_bit(band, bit):
    """Return band after replacing least significant bit"""
    band = band & 0b11111110
    return int(band | int(bit))

def get_least_sig_bit(band):
    """Return the least significant bit in color value"""
    mask = 0x1
    last_bit = band & mask
    return str(last_bit)

def get_bit_string_from_pixels(start_index, num_bits_needed, pixels):
    """Loop through the list of pixels beginning at start index and return
    a string of bits with number of bits needed"""
    bit_string = ""
    bit_count = 1
    for i in range(start_index, 0, -1):
        for band in (pixels[i]):
            bit_string += get_least_sig_bit(band)
            if bit_count == num_bits_needed:
                return bit_string
            bit_count += 1

def write_bits_to_pixels(start_index, bit_array, pixels):
    """Write bits to pixels"""
    for i in range(start_index, 0, -1):
        rgb = list()
        for band in pixels[i]:
            if len(bit_array) == 0:
                rgb.append(band)
            else:
                rgb.append(replace_least_sig_bit(band, bit_array.pop(0)))
        pixels[i] = tuple(rgb)
        if len(bit_array) == 0:
            return


def extract_message(image_path):
    """Extracting text from image then print to console
    Args:
        image_path (str): relative or absolute path to the image from command line
    Return:
        None
    """
    if not image_path.lower().endswith(".png"):
        print("Format not supported. Use \"python3 StegaImage.py -h\" for help.")
        return
    image = Image.open(image_path)
    pixels = list(image.getdata())
    num_pixels = len(pixels)

    #extract total number of bits from last 11 pixels
    bits = get_bit_string_from_pixels(num_pixels - 1, 32, pixels)
    text_length = int(bits, 2)
    print(text_length)

    #getting the actual message by reading "text_length" number of bits
    bits = get_bit_string_from_pixels(num_pixels - 12, text_length, pixels)
    bit_array = bitarray(bits)
    print(bit_array.tostring())


def embed_message(textfile_path, image_path):
    """Embed specified text in image
    Args:
        textfile_path (str): text file (.txt)
        image (str): image file path (.jpeg)
    Return:
        None
    """
    if (not image_path.lower().endswith((".jpeg", ".jpg"))):
        print("Format not supported. Use \"python3 StegaImage.py -h\" for help.")
        return

    with open(textfile_path, 'r') as myfile:
        text = myfile.read()

    #getting number of pixels
    image = Image.open(image_path)
    pixels = list(image.getdata())
    num_pixels = len(pixels)
    bin_text_length = bin(len(text) * 8)[2:].zfill(32)
    bitarray_text_len = bitarray(bin_text_length)

    #writing the number of bits to last 11 pixels
    write_bits_to_pixels(num_pixels - 1, bitarray_text_len, pixels)
    bitarray_text = bitarray()
    bitarray_text.fromstring(text)

    #writing the text to image
    write_bits_to_pixels(num_pixels - 12, bitarray_text, pixels)
    base = os.path.basename(image_path)
    name = base.split('.')[0]
    image.putdata(pixels)
    image.save(name + '.png')
    

def main(argv):
    """Process arguments and calling approriate methods to handle task"""  
    if len(argv) < 2 or argv[1] == "-h":
        print(HELP_MESSAGE)
    elif argv[1] == "-x" and leng(argv) == 3 :
        extract_message(argv[2])
    elif argv[1] == "-e" and len(argv) == 4:
        embed_message(argv[2], argv[3])
    else:
        print(HELP_MESSAGE)

if __name__ == "__main__":
    main(sys.argv)
