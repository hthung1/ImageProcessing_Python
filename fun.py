import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image, ImageFilter, ImageEnhance

class fun():
    def dao_anh(img):
        return 255-img

    def anh_Xam(img):
        image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        return image

    def histogram(img):
        histr = cv2.calcHist([img],[0],None,[256],[0,256])
        plt.plot(histr)
        plt.show()

    def canny_edge_detection(img,threshold1,threshold2):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        image = cv2.Canny(gray, threshold1, threshold2)
        return image

    def blur(img,value):
        kernel_size = (value + 1, value + 1)
        image = cv2.blur(img, kernel_size)
        return image
    def brightness(img,val):
        while True:
            hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            hsv = np.array(hsv, dtype=np.float64)
            val = val/100 
            hsv[:, :, 1] = hsv[:, :, 1] * val
            hsv[:, :, 1][hsv[:, :, 1] > 255] = 255
            hsv[:, :, 2] = hsv[:, :, 2] * val
            hsv[:, :, 2][hsv[:, :, 2] > 255] = 255
            hsv = np.array(hsv, dtype=np.uint8)
            res = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
            print(res)
            return res
    def contrast(img,contrast):
        if contrast != 131:
            f = 131*(contrast + 127)/(127*(131-contrast))
            alpha_c = f
            gamma_c = 127*(1-f)
            buf = cv2.addWeighted(img, alpha_c, img, 0, gamma_c)
            return buf