try:
    from PIL import Image
except ImportError:
    import Image
import pyautogui as pg
import pytesseract
import random
import string
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
import cv2
import mss.tools as mt
from mss import mss
def do_ocr(filename):
    return(pytesseract.image_to_string(Image.open(filename)))
def screenshot(filename):
    with mss() as sct:
        screen = sct.shot(output=filename)
    return(screen)
screenshot("screen.png")
imageObject  = Image.open("screen.png")
imageObject.crop((750,300,1150,450)).save('isdq2.png')
