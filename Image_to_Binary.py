import numpy as np
import cv2

# Load the image in grayscale mode
img = cv2.imread('"C:\Users\shrip\Desktop\Sagar\Internship\Projects\Image Encryption\Input Image.jpg"', 0)

# Get the dimensions of the image
h, w = img.shape

# Initialize counters
z = 0
c = 0

# Open the file in append mode
with open("Binary.txt", "a") as f:
    print("opened file")
    for i in range(h):
        for j in range(w):
            a = img[i, j]
            binary_str = format(a, '08b')  # Convert the pixel value to an 8-bit binary string
            f.write(binary_str)
            c += 8
            z += 1
            if z == 8:
                f.write('\n')
                z = 0
                print("complete")
                
print("Process completed")
