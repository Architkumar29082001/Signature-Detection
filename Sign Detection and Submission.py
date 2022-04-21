import easyocr
import cv2
from matplotlib import pyplot as plt
import numpy as np
import os
from PIL import Image
import math
IMAGE_PATH=input()
size = os.path.getsize(IMAGE_PATH)
size/=1024
roundsize=round(size,3)
reader = easyocr.Reader(['en'], gpu=True)

try:
    result = reader.readtext(IMAGE_PATH)
    print("It's a Signature")
    print("Select Exam type :")
    print("1)JEE")
    print("2)VITEEE")
    print("3)GATE")
    Exam_type = input()
    if Exam_type == "JEE":
        if roundsize < 30 and roundsize>4:
            print("The file submitted succesfully ")

        else:
            print("Uploaded file size: ", roundsize)
            print("File size is to large, Compressing the file  under 4Kb to 30Kb ")
            foo = Image.open(IMAGE_PATH)
            x, y = foo.size
            x2, y2 = math.floor(x - 600), math.floor(y - 1100)
            foo = foo.resize((x2, y2), Image.ANTIALIAS)
            foo.save("D:\coding\OCR testing\Compressed Photo\image_scaled2.jpg", quality=95)
            print("File Compressed and Submitted succesfully")

    elif Exam_type == "VITEEE":
        if roundsize < 200 and roundsize>10:
            print("The file submitted succesfully ")

        else:
            print("Uploaded file size: ", roundsize)
            print("File size is to large, Compressing the file under 10Kb to 200Kb ")
            foo = Image.open(IMAGE_PATH)
            x, y = foo.size
            x2, y2 = math.floor(x - 600), math.floor(y - 1250)
            foo = foo.resize((x2, y2), Image.ANTIALIAS)
            foo.save("D:\coding\OCR testing\Compressed Photo\image_scaled2.jpg", quality=95)
            print("File Compressed and Submitted succesfully")
    elif Exam_type == "GATE":
        if roundsize < 200 and roundsize>10:
            print("The file submitted succesfully ")
        else:
            print("Uploaded file size: ", roundsize)
            print("File size is to large, Compressing the file under 10Kb to 200Kb ")
            foo = Image.open(IMAGE_PATH)
            x, y = foo.size
            x2, y2 = math.floor(x - 600), math.floor(y - 1100)
            foo = foo.resize((x2, y2), Image.ANTIALIAS)
            foo.save("D:\coding\OCR testing\Compressed Photo\image_scaled2.jpg", quality=95)
            print("File Compressed and Submitted succesfully")
    else:
        print("Enter Valid Exam name ")
except Exception as e:
    if(e=="Unknown exception from OpenCV code"):
        print("Image")
    else:
        print(e)








