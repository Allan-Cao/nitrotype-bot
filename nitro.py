try:
    from PIL import Image
except ImportError:
    import Image
import pyautogui as pg
pg.FAILSAFE = False
import pytesseract
import random
#from autocorrect import spell
import string
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
import cv2
import mss.tools as mt
from mss import mss
def do_ocr(filename):
    return((pytesseract.image_to_string(Image.open(filename))))
def screenshot(filename):
    with mss() as sct:
        screen = sct.shot(output=filename)
    return(screen)
print("[Debug] Starting OCR Racer in 2 seconds")
import time
time.sleep(2)
end = False

while True:
    if end:
        time.sleep(4)
        pg.press("enter")
        time.sleep(5)
        pg.scroll(1000)
        while True:
            screenshot("screen.png")
            imageObject  = Image.open("screen.png")
            imageObject.crop((700,840,1210,868)).save('waiting.png') # THESE VALUES MUST CHANGE
            if (open("waiting.png","rb").read() != open("wait.png","rb").read()):
                break
    screenshot("screen.png")
    imageObject  = Image.open("screen.png")
    imageObject.crop((700,840,1210,868)).save('line.png') # THESE VALUES MUST CHANGE
    imageObject.crop((700,868,1210,896)).save('isend.png') # THESE VALUES MUST CHANGE
    pg.scroll(1000)
    end = open("isend.png","rb").read() == open("endstate.png","rb").read()
    queue = do_ocr("line.png")
    #print(queue)
    pg.typewrite(queue, interval=random.uniform(0.05, 0.06))
    pg.press('space')
    #pg.scroll(1000)
    pg.typewrite(",.'pgy")
    time.sleep(0.2)
