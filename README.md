# HideIt
Uses last bit steganography technique to hide a file in a PNG image. An image is represented as 8-bit RGB values for each pixel in the Image.
If 1 or 2 lower order bits of an image are altered, then there is no change in the image which is noticable by naked eye.
So using this to our advantage, we can hide data from another file in these 1 or 2 lower order bits without any noticable change or increase in size.
Let say we have a 1280x720 image, so number of pixels in it are 921600. Also, the image has 3 channels i.e RGB, so actually the image is made up of 921600*3 = 2764800 8-bit values. If we use 2 lower order bits from each of these values, then we can hide a file of size upto 2764800 * 2 = 5529600 or 5.53 Megabits(Mb), thats a very large space for text data and some small size images can also be hidden.
As the number of bits used increase or the size of image increases, we can hide even more data in the image but the disadvantage of this is that the change might be noticable.

![Main Image](/samples/1.png?raw=true "Original Image")
![Hidden Image](/samples/101.png?raw=true "Hidden Image")
![2-bits](/samples/hide2.png?raw=true "Using 2 LSBs for hiding data")
![4-bits](/samples/hide4.png?raw=true "Using 4 LSBs for hiding data")
![6-bits](/samples/hide6.png?raw=true "Using 6 LSBs for hiding data")
![8-bits](/samples/hide8.png?raw=true "Using 8 bits for hiding data")
<img width=50% src='samples/hide2.png' title="Using 2 LSBs for hiding data"/>