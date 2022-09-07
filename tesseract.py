from PIL import Image
from pytesseract.pytesseract import *
image_file = "temp.png"
im = Image.open(image_file)
text = image_to_string(im)
print(text)
