# lytro

Mimicking the Lytro camera effect by capturing multiple images over a plane orthogonal to the optical axis.

![Image](http://i.imgur.com/azQmcwK.gif)

## Background and Algorithm

We use the paper by Ren Ng of Stanford University (the founder of the Lytro camera and professor at Berkeley) [http://graphics.stanford.edu/papers/lfcamera/lfcamera-150dpi.pdf]. In this he describes the method of autofocusing to certain aspects of the image. The basic idea is that we can refocus to certain parts of an image by shifting an array of images (that are slightly shifted in an axis), by a predefined amount. As this amount changes, we can shift to a different part of an image. This is the basic idea of Lytro. They take several images at the same time, shifting each by a certain amount.

## Running Code

Note that there is no sample data as it takes around 1 GB of data. To access it view the Stanford Light Field Archive: http://lightfield.stanford.edu/lfs.html 

To run the code just run 
```
python main.py
```
With a size.png image on the same folder as main.py and a rectefied folder in the same directory as main.py.

To adjust the parameters, scroll to the bottom of the main.py and then uncomment the code as follows. Add in the paramters as needed. 
