import numpy as np
import binascii
from PIL import Image

srcImage = input("Enter path of image in which to hide data(PNG image only)\n")

hiddenFile = input("Enter path of file whose data is to be hidden\n")

imageWithHiddenData = input("Enter the name of new image file to be generated with hidden data\n")
imageWithHiddenData += '.png'

n = np.uint8(int(input("Enter the number of bits of image to be used to hide data(Maximum 8)\n")))

if n > 8 or n < 1:
	print("Enter a value between 1 to 8")
	exit()

srcImg = Image.open(srcImage)

if srcImg.format.upper() != 'PNG':
	print("Use PNG images only")
	exit()

srcData = np.array(srcImg)

print("Image read successfully")

hiddenData = ''

row = len(srcData)
col = len(srcData[0])
height = len(srcData[0][0])

srcData = srcData.flatten()

with open(hiddenFile, "rb") as f:
	byte = f.read(1)
	while byte:
		hexadecimal = binascii.hexlify(byte)
		decimal = int(hexadecimal, 16)
		binary = bin(decimal)[2:].zfill(8)
		hiddenData += binary
		byte = f.read(1)

print("File read Successfully\n")

hiddenDataSize = bin(len(hiddenData))[2:].zfill(64)
noOfBitsUsed = bin(n-1)[2:].zfill(3)
hiddenData = hiddenDataSize + hiddenData

hiddenData += "0"*(n-(len(hiddenData)%n))

if len(hiddenData) > n*(len(srcData)-1):
	print("Size of image is small for hiding the data")
	exit(0)

print("Hiding Data....")

srcData[0] &= 248
srcData[0] |= np.uint8(int("00000" + noOfBitsUsed, 2))

i=1
j=0
setToZero = np.uint8(255 << n)
while i < len(srcData) and j < len(hiddenData):
	srcData[i] &= setToZero
	bits = np.uint8(int("0"*(8-n) + hiddenData[j:j+n], 2))
	srcData[i] |= bits
	i += 1
	j += n

srcData = np.reshape(srcData, [row, col, height])

img = Image.fromarray(srcData)
img.save(imageWithHiddenData)

print("Done!")