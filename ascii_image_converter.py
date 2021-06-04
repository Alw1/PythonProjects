#Alex Wyatt 2021

"""
A small Python script that takes an image and converts it's pixels into ASCII characters.
NOTE: Does not fully work yet; the function that converts RGB tuples to a brightness value
needs to be finetuned to differentiate pixels better. Code to change the size of image and better display it in the terminal will also need to be added later.
"""

from PIL import Image

filename = input("Enter filename of picture: ")#picture must be in same directory as this script 
im = Image.open(filename)
ascii_vals = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

def get_pixel_matrix(img): # converts each pixel in the picture into a tuple with the RGB value of the pixel (R,G,B)
    im.thumbnail(im.size)
    pixels = list(im.getdata())
    return [pixels[i:i+im.width] for i in range(0, len(pixels), im.width)]

def brightness_matrix(pixel_matrix): # Converts each RGB tuple into a brightness value between 0-255
    matrix = []
    for row in pixel_matrix:
        brightness_value = []
        for y in row:
             brightness = (0.21*y[0] + 0.72*y[1] + 0.07*y[2])#averages rgb value of a pixel and returns average brightness
        brightness_value.append(brightness)
        matrix.append(brightness_value)
    return matrix

def convert_to_ascii(brightness_matrix,ascii_vals): # Converts the array filled with the brightness values into ascii symbols 
    a = []
    for row in brightness_matrix:
        b = []
        for value in row:
           value = (65 * value) / 255 
           v = ascii_vals[int(value)] * 3
        b+=v
        a.append(b)
    return a

def print_ascii(ascii_array):
    f = []
    g = []
    for row in ascii_array:
        for array in row:
            for value in array:
                g+= value
        f.append(g)
    print(g)



bright = brightness_matrix(get_pixel_matrix(filename))
ascii_array = convert_to_ascii(bright, ascii_vals)
print_ascii(ascii_array)
