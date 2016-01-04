README.md
Kuriakose Sony Theakanath

========
OVERVIEW
========

To use the code run:

python main.py

With a size.png image on the same folder as main.py and a rectefied folder in the same directory as main.py.

To adjust the parameters, scroll to the bottom of the main.py and then uncomment the code as follows. Then add in the paramters as needed. 

===================
EXPLANATION OF CODE
===================

There's two functions:

depthRefocusing(path, SCALE). This takes in two parameters, the path which is the pictures to combine and then the SCALE. SCALE is the amount to shift the images. To test this out please put a number between -2 and 4. This would focus the image on different parts of the screen. In this function it iteretes through the contents of the folder and then calculates the shift. From that it averages the images based on the shift and moves the current image accordingly. The saved image is in the same folder as main.py

aperture(path, num). Takes in two parameters. Path just like depthRefocusing and num, the number of images to average. This function is simple, it takes all of the images in the folder and the averages them, saving the image in the root directory as main.py