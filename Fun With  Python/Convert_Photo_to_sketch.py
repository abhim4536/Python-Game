from tkinter import ttk
from tkinter import *
import cv2
from tkinter.filedialog import *

root = Tk()
root.withdraw
o_file = askopenfilename(initialdir = os.getcwd(), title = "Select Image File", filetypes = (("jpg file", "*.jpg"), ("png file", "*.png"),("jpeg file", "*.jpeg"), ("All file", "*.*")))
image = cv2.imread(o_file)
grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(grey_img)
blur = cv2.GaussianBlur(invert, (21,21),0)
invertedblur = cv2.bitwise_not(blur)
sketch = cv2.divide(grey_img, invertedblur, scale=256.0)
keep = cv2.imwrite("sketch1.jpg", sketch)
cv2.imshow('sketch1.jpg',keep)
cv2.waitKey(0)
cv2.destroyAllWindows()
