import numpy as np
import cv2

# Open the file and read its contents
with open("C:\Users\shrip\Desktop\Sagar\Internship\Projects\Image Encryption\Enigma.txt" "r") as f:
    lines = f.readlines()

# Initialize variables
a1, a2, b = 0, 0, 0
c = 128
z1 = 0
arr = np.zeros((1024, 1024), dtype=np.uint8)  # Ensure the array has the correct data type

# Process each line in the file
for line in lines:
    for x in line.strip():  # strip() to remove any extraneous whitespace
        b += c * int(x)
        c //= 2
        if c == 0:
            c = 128
            arr[a1, a2] = b
            b = 0
            z1 += 1
            if a2 == 1023:
                if a1 == 1023:
                    a1 = 123456  # Unique value to break the loop
                else:
                    a1 += 1
                a2 = 0
            else:
                a2 += 1
            if z1 == 8:
                z1 = 0
                break
    if a1 == 123456:
        break

# Display the image
cv2.imshow("image", arr)
cv2.waitKey(0)
cv2.destroyAllWindows()
