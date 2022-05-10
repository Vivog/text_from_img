import pytesseract
from PIL import Image

img = Image.open('test_img.jpg')
file_name = img.filename
file_name = file_name.split('.')[0]
# For Windows
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
# In Tesseract Docs
custom_config = r'--oem 3 --psm 6'

text = pytesseract.image_to_string(img, config=custom_config)
with open(f'{file_name}.txt', 'w', encoding='utf-8') as file_text:
    file_text.write(text)