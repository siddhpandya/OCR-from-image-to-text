import cv2
import pytesseract
import numpy as np
from PIL import ImageGrab
import time 
pytesseract.pytesseract.tesseract_cmd = 'D:/Tesseract-OCR/tesseract.exe'
cap = cv2.VideoCapture(1)
cap.set(3,640)
cap.set(4,480)
def captureScreen(bbox=(300,300,1500,1000)):
    capScr = np.array(ImageGrab.grab(bbox))
    capScr = cv2.cvtColor(capScr, cv2.COLOR_RGB2BGR)
    return capScr
while True:
    _,img = cap.read()
    boxes = pytesseract.image_to_data(img)
    for a,b in enumerate(boxes.splitlines()):
            #print(b)
            if a!=0:
                b = b.split()
                if len(b)==12:
                    x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
                    cv2.putText(img,b[11],(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,0.4,(50,50,255),2)
                    cv2.rectangle(img, (x,y), (x+w, y+h), (50, 50, 255), 2)
    cv2.imshow("live_word_detection",img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
    cv2.waitKey(1)
