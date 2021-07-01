import pyautogui
from PIL import Image,ImageGrab
import time
from numpy import asarray
import glob 
import sys
from PIL import Image
import pytesseract as pt
import os
import requests
i = 0

def takeScreenshot():
    image = ImageGrab.grab().convert('L')
    global i
    # image.show()
    # return image
    image.save(f"/home/rakesh/Desktop/sav/img{i}.png")
def main():
    path ="/home/rakesh/Desktop/sav/"
    tempPath ="/home/rakesh/Desktop/output"
    
    for imageName in os.listdir(path):
        inputPath = os.path.join(path, imageName)
        img = Image.open(inputPath)
        text = pt.image_to_string(img, lang ="eng")  
        fullTempPath = os.path.join(tempPath,imageName+".txt")
        file1 = open(fullTempPath, "w")
        file1.write(text)
        file1.close() 
  
def server():
    path ="/home/rakesh/Desktop/sav/"
    tempPath ="/home/rakesh/Desktop/output"
    imga1 = os.path.join(path,f"img{i}.png")
    imga2 = Image.open(imga1)
    text = pt.image_to_string(imga2,lang="eng")

    # send imga1 and text to server as post request 
    payload = {"images":open(imga1,'rb')} 
    data = {'title':text}
    r = requests.post('https://tryingtoupload123.herokuapp.com/api/',files = payload,data = data)
    print(r.text)


if __name__=='__main__':
    while True:
        time.sleep(5)
        image = takeScreenshot()
        # main()
        server()
        i +=1