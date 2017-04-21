import numpy as np
from PIL import Image

srcImage = input("Enter path of image to shift\n")

n = int(input("Enter number of bytes to shift the image(Maximum 8)\n"))

if n > 8 or n < 1:
	print("Enter a value between 1 to 8")
	exit()

shiftedImg = input("Enter the name of resultant shifted image\n")

srcImg = Image.open(srcImage)
srcData = np.array(srcImg)

print("Image read successfully")

row = len(srcData)
col = len(srcData[0])
height = len(srcData[0][0])

srcData = srcData.flatten()

for i in range(len(srcData)):
	srcData[i] <<= np.uint(n)

srcData = np.reshape(srcData, [row, col, height])

img = Image.fromarray(srcData)
img.save(shiftedImg)

print("Done!")