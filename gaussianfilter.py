import numpy as np
import scipy.ndimage as ndimage
import matplotlib.pyplot as plt

img = ndimage.imread('woman.jpeg')
plt.imshow(img, interpolation='nearest')
plt.show()
# Note the 0 sigma for the last axis, we don't wan't to blurr the color planes together!
img = ndimage.gaussian_filter(img, sigma=(5, 5, 0), order=0)
plt.imshow(img, interpolation='nearest')
plt.show()




#import cv2
#import numpy as np
#from matplotlib import pyplot as plt

#img = cv2.imread('woman.jpeg')

#blur = cv2.blur(img,(5,5))

#plt.subplot(121),plt.imshow(img),plt.title('Original')
#plt.xticks([]), plt.yticks([])
#plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
#plt.xticks([]), plt.yticks([])
#plt.show()