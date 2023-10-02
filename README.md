# Image_processing

I used matplotlib.image ,matplotlib.pyplot ,numpy ,scipy.ndimage and convolve.
Basically the main thing which I learned is making the convolution matrix logic.

What is Convolution ?
Convolution is a mathematical operation commonly used in image processing, signal processing, and various other fields of mathematics and engineering. 
In the context of image processing, convolution is often used for applying various image filters, such as blurring, sharpening, edge detection, and more

I this project I have an Image, on which I have to apply different filters such as Blur, sharp, Identity, emboss etc. by using the convolution matrices.

Identity :- The identity matrix retains the original image doing no change to any pixel.
[[0,0,0],
[0,1,0],
[0,0,0]]



Blur Image :- Applying Convolution effect 
[[1,2,2],
[2,4,2],
[1,2,1]]

How Blurring Occurs?
Blurring in image processing involves a 3x3 convolution matrix that slides over the image, calculating a weighted average of pixel values in its vicinity. 
This operation replaces each pixel with a blend of itself and nearby pixels. The blurring effect is achieved by prioritizing nearby pixels over distant ones in the convolution matrix.


Emboss Image matrix :- 
[[-2,1,0],
[-1,1,1],
[0,1,2]]

Sharp Image matrix :- 
[[0,-1,0],
[-1,5,-1],
[0,-1,0]]


