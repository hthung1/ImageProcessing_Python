from re import S
from PIL import Image, ImageEnhance
import cv2

#read the image
img = cv2.imread('doi.png')
contrast =133
f = 131*(contrast + 127)/(127*(131-contrast))
alpha_c = f
gamma_c = 127*(1-f)

buf = cv2.addWeighted(img, alpha_c, img, 0, gamma_c)
cv2.imshow(buf)