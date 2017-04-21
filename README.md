# HideIt
Uses last bit steganography technique to hide a file in a PNG image. An image is represented as 8-bit RGB values for each pixel in the Image.<br/><br/>
If 1 or 2 lower order bits of an image are altered, then there is no change in the image which is noticable by naked eye.<br/><br/>
So using this to our advantage, we can hide data from another file in these 1 or 2 lower order bits without any noticable change or increase in size.<br/><br/>
Let say we have a 1280x720 image, so number of pixels in it are 921600. Also, the image has 3 channels i.e RGB, so actually the image is made up of 921600*3 = 2764800 8-bit values. If we use 2 lower order bits from each of these values, then we can hide a file of size upto 2764800*2 = 5529600 or 5.53 Megabits(Mb), thats a very large space for text data and some small size images can also be hidden.<br/><br/>
As the number of bits used increase or the size of image increases, we can hide even more data in the image but the disadvantage of this is that the change might be noticable.

<h4>Main Image</h4>
<img width=60% src='samples/1.png' title="Main Image"/>
<h4>Hidden Image</h4>
<img width=50% src='samples/101.png' title="Hidden Image"/>
<h4>Images with hidden data</h4>

Using 2 LSBs for hiding data             |  Using 4 LSBs for hiding data
:--------------------------------------:|:------------------------------------:
![](/samples/hide2.png)                 |  ![](/samples/hide4.png)

Using 6 LSBs for hiding data             |  Using 8 bits for hiding data
:--------------------------------------:|:------------------------------------:
![](/samples/hide6.png)                 |  ![](/samples/hide8.png)

# How to use
To encode a file in a PNG image, run the following commands<br/>
```
> python3 encodegen.py 
Enter path of image in which to hide data(PNG image only)
[Path of Image]
Enter path of file whose data is to be hidden
[Path of file]
Enter the name of new image file to be generated with hidden data
[Path of new Image(do not add file extension eg. /home/kartik/Downloads/newImg)]
Enter the number of bits of image to be used to hide data(Maximum 8)
[Enter no. of LSBs to use]
Image read successfully
File read Successfully

Hiding Data....
Done!
```