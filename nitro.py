from autocorrect import spell
try:
    from PIL import Image
except ImportError:
    import Image
import pyautogui as pg
pg.FAILSAFE = False
import pytesseract
import random
import string
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
import cv2
import mss.tools as mt
from mss import mss
def correct(queue):
    queue.translate(str.maketrans('', '', string.punctuation))
    str_list = queue.split()
    result_list = []
    for word in str_list:
        sympos = []
        if (word.translate(str.maketrans('', '', string.punctuation)) == word):
            result_list.append(word)
        else:
            _word = list(word)
            for symbol in string.punctuation:
                for char in range(len(_word)):
                    if _word[char] == symbol:
                        sympos.append([char, symbol])
            adj = 0
            for item in sympos:
                _word.pop(item[0]-adj)
                adj+=1
            _word = list(spell(''.join(_word)))
            for item in sympos:
                _word.insert(item[0],item[1])
            result_list.append("".join(_word))
    queue = " ".join(result_list)
    queue+=random.choice(string.ascii_letters)
    queue+=random.choice(string.ascii_letters)
    return queue
def do_ocr(filename):
    return((pytesseract.image_to_string(Image.open(filename))))
def screenshot(filename):
    with mss() as sct:
        screen = sct.shot(output=filename)
    return(screen)
print("[Debug] Starting OCR Racer in 2 seconds")
import time
#time.sleep(2)
end = False
refresh = ['%','%','%']
while True:
    pg.scroll(1000)
    screenshot("screen.png")
    imageObject  = Image.open("screen.png")
    imageObject.crop((700,840,1210,868)).save('line.png') # THESE VALUES MUST CHANGE
    #imageObject.crop((700,868,1210,896)).save('isend.png') # THESE VALUES MUST CHANGE
    
    #end = open("isend.png","rb").read() == open("endstate.png","rb").read()
    
    imageObject.crop((670,410,1230,470)).save('race.png')
    if(open("race.png","rb").read() == open("RESULTS.png","rb").read()):
        print('[Debug] Race End Detected')
        pg.press("enter")
        time.sleep(2)
        pg.scroll(1000)
        while True:
            screenshot("screen.png")
            imageObject  = Image.open("screen.png")
            imageObject.crop((700,840,1210,868)).save('waiting.png') # THESE VALUES MUST CHANGE
            if (open("waiting.png","rb").read() != open("wait.png","rb").read()):
                break
    imageObject.crop((700,840,1210,868)).save('line.png') # THESE VALUES MUST CHANGE
    queue = do_ocr("line.png")
    queue = queue.replace('’',"'")
    #print(queue)
    refresh.pop(0)
    refresh.append(queue)
    queue = correct(queue)
    pg.typewrite(queue, interval=random.uniform(0.03, 0.045))
    if (random.randint(1,5)==3):
        pg.typewrite(random.choice(string.ascii_letters)+random.choice(string.ascii_letters))
    pg.press('space')
    pg.scroll(1000)
    time.sleep(0.2)#750,300,1150,520
    if (len(set(refresh))==1 and (refresh[0] != 'Please wait. Typing content will')):
        print("[Debug] Failsafe Triggered")
        print(refresh)
        pg.press('f5')
        time.sleep(3)
        refresh = ['%','%','%']
    else:
        screenshot("screen.png")
        imageObject  = Image.open("screen.png")
        imageObject.crop((750,300,1150,520)).save('isdq.png')
        if (open("isdq.png","rb").read() == open("dq.png","rb").read()):
            pg.press('f5')
            time.sleep(3)
        else:
            refresh = ['%','%','%']
