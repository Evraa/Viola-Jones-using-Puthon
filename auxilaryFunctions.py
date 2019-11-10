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

'''
#to convert images from/to numpy array
def to_float_array(img: Image.Image) -> np.ndarray:
    return np.array(img).astype(np.float32) / 255.

def to_image(values: np.ndarray) -> Image.Image:
    return Image.fromarray(np.uint8(values * 255.))
'''

#Class for stumps
class DecisionStump():
    def __init__(self):
        # Determines if sample shall be classified as -1 or 1 given threshold
        self.polarity = 1
        # The index of the feature used to make classification
        self.feature_index = None
        # The threshold value that the feature should be measured against
        self.threshold = None
        # Value indicative of the classifier's accuracy
        self.alpha = None

#Class for Adaboost
class Adaboost:
    #M: is the #of base learners
    def __init__(self,M):
        self.M = M
    def fit(self,X,Y):
        #Variables for decision stumps and their corresponding alphas
        self.models = []
        self.alphas = []
        #n: #od examples 
        N, _ = X.shape
        #W: array of weights fo each example, initialized with uniform equal values for all of them
        W = np.ones(N) / N 
        #We create punch of M stumps
        for m in range(self.M):
            tree = DecisionTreeClassifier(max_depth=1)
            tree.fit(X,Y,sample_weight=W)
            P = tree.predict(X)
        #Calculate the error
        err = W.dot(P != Y)
        alpha = 0.5*(np.log(1-err) - np.log(err))
        #Store theri alphas
        W = W*np.exp(-alpha*Y*P)
        W = W/W.sum()
        #And then store these stumps
        self.models.append(tree)
        self.alphas.append(alpha)

    def predict(self,X):
        #we need to return accuracy here
        N, _= X.shape
        FX = np.zeros(N)
        for alpha, tree in zip(self.alphas ,self.models):
            FX += alpha*tree.predict(X)
                #First return the accuracy
        return np.sign(FX), FX

    def score(self,X,Y):
        P,FX = self.predict(X)
        L = np.exp(-Y*FX).mean()
        return np.mean(P == Y) , L


if __name__ == '__main__':
    #First we get the data
    dataSet = datasets.load_digits()
    X = dataSet.data
    Y = dataSet.target
    digit1 = 1
    digit2 = 8
    idx = np.append(np.where(Y == digit1)[0], np.where(Y == digit2)[0])
    Y = dataSet.target[idx]
    # Change labels to {-1, 1}
    Y[Y == digit1] = -1
    Y[Y == digit2] = 1
    X = dataSet.data[idx]

    #80% is training data and 20% is testing
    Ntrain  = int(0.8*len(X))
    Xtrain,Ytrain = X[:Ntrain], Y[:Ntrain]
    Xtest,Ytest = X[Ntrain:], Y[Ntrain:]
    
    #T = # od iterations
    
    T = 200
    train_errors = np.empty(T)
    test_losses = np.empty(T)
    test_errors = np.empty(T)
    for num_trees in range(T):
        if num_trees == 0:
            train_errors [num_trees] = None
            test_errors [num_trees] = None
            test_losses [num_trees] = None
            continue
        if num_trees % 20 == 0:
            print (num_trees)
        model = Adaboost(num_trees)
        model.fit(Xtrain, Ytrain)
        acc , loss = model.score(Xtest,Ytest)
        acc_train, _ = model.score(Xtrain ,Ytrain)

        train_errors [num_trees] = 1 - acc_train
        test_errors [num_trees] = 1 - acc
        test_losses [num_trees] = loss
        
        if num_trees == T-1:
            print("Finalt train error" , 1 - acc_train)
            print("Finalt test error" , 1 - acc)

    plt.plot(test_errors , label="test errors")
    plt.plot(test_losses , label="test loss")
    plt.legend()
    plt.show()

    plt.plot(train_errors , label="train errors")
    plt.plot(test_errors , label="test errors")
    plt.legend()
    plt.show()

    
        