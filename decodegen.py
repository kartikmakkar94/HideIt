from PIL import Image
import numpy as np
import binascii

srcImage = input("Enter path of image with hidden data(PNG image only)\n")

srcImg = Image.open(srcImage)
srcData = np.array(srcImg)

if srcImg.format.upper() != 'PNG':
	print("Use PNG images only")
	exit()

print("Image read Successfully\n")

srcData = srcData.flatten()

generatedFile = input("Enter name of file to be generated having hidden data\n")

n = int((bin(srcData[0])[2:].zfill(8))[-3:], 2) + 1;

hiddenDataSize = ''

i = 1
while len(hiddenDataSize) < 64:
	binary = bin(srcData[i])[2:].zfill(8)
	hiddenDataSize += binary[-n:]
	i += 1

hiddenData = ''
if (len(hiddenDataSize)%64!=0):
	hiddenData = hiddenDataSize[-(len(hiddenDataSize)%64):]

hiddenDataSize = int(hiddenDataSize[:64], 2)

while len(hiddenData) < hiddenDataSize:
	binary = bin(srcData[i])[2:].zfill(8)
	hiddenData += binary[-n:]
	i += 1

hiddenData = hiddenData[:hiddenDataSize]

with open(generatedFile, "wb") as f:
	i=0
	while i < len(hiddenData):
		data = hiddenData[i:i+8]
		data = '{0:02x}'.format(int(data, 2))
		byte = binascii.unhexlify(data)
		f.write(byte)
		i += 8

print("Done!")