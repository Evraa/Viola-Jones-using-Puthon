import skimage.io as io
from skimage.exposure import histogram
from skimage.color import rgb2gray,rgb2hsv
from skimage.util import random_noise
from skimage.filters import median
from skimage.feature import canny

import matplotlib.pyplot as plt
from matplotlib.pyplot import bar
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

# Convolution: If not needed, delete it later
from scipy.signal import convolve2d
from scipy import fftpack
import math

#Used for Adaboost classifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import datasets

import numpy as np
from PIL import Image, ImageOps





# Show the figures / plots inside the notebook
def show_images(images,titles=None):
    #This function is used to show image(s) with titles by sending an array of images and an array of associated titles.
    # images[0] will be drawn with the title titles[0] if exists
    # You aren't required to understand this function, use it as-is.
    n_ims = len(images)
    if titles is None: titles = ['(%d)' % i for i in range(1,n_ims + 1)]
    fig = plt.figure()
    n = 1
    for image,title in zip(images,titles):
        a = fig.add_subplot(1,n_ims,n)
        if image.ndim == 2: 
            plt.gray()
        plt.imshow(image)
        a.set_title(title)
        plt.axis('off')
        n += 1
    fig.set_size_inches(np.array(fig.get_size_inches()) * n_ims)
    plt.show() 
    

def showHist(img):
    # An "interface" to matplotlib.axes.Axes.hist() method
    plt.figure()
    imgHist = histogram(img, nbins=256)
    
    bar(imgHist[1].astype(np.uint8), imgHist[0], width=0.8, align='center')

def Grey_img(image):
    size = image.shape
    if (len(size) == 3):
        grey_image = rgb2gray(image)
    else:
        grey_image = image/255
    return grey_image

#Resizing images for datasets
def resizeBy24x24(img_dest, new_name):
    img = Image.open(img_dest)
    img_down = img.resize((24, 24), Image.ANTIALIAS)
    ext = ".jpg"
    img_down.save(new_name + ext)
    img = io.imread(new_name + ext)
    img = rgb2gray(img)
    return img

