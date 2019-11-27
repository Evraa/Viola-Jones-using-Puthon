from auxilaryFunctions import np
from auxilaryFunctions import integralImage

'''
include the basic haar feature
'''
#Global Variables
features = np.array([
    [1,2],
    [2,1],
    [1,3],
    [3,1],
    [2,2]
])

# calculating the integral image
def calIntegralImage(integralImg,i,j,w,h): # i,j of the index to be calculated while w,h is the size of the feature image
    topLeft = 0
    top = 0
    left = 0
    if(i - w >= 0 and j - h >= 0):
        topLeft = integralImg[i - w,j - h]
    if(i - w >= 0):
        top = integralImg[i - w,j]
    if(j - h >= 0):
        left = integralImg[i ,j - h]
    print(integralImg[i,j],' ',left,' ',top,' ',topLeft)
    result = integralImg[i,j] - left - top + topLeft
    return result

#Main Function:
'''
making the viola jones features and counting them
'''


def HaarFeatures(image=None):
    fileInput = open("HaarF.txt","w+") # assuming the image name would be stored in HaarF.txt
    integralInput = integralImage(fileInput) # integral input would hold the intergal of the input image
    featuresVec = np.zeros(161000) # vector that would hold the 160K features of the 24x24 image
    featuresVecCounter = 0 # to move through the indeces
    
    '''
    getting all the features of the shape 1x2

    '''
    
    x = features[0] # x would hold feature 1x2

    #values = np.zeros([1,30000])
    for i in range(1,int(24/2)+1): # from i = 1 to i = 12
        for j in range(1,24+1): # from i = 1 to i = 24
            currentFeat = np.zeros((x[0]*j,x[1]*i))
            for c in range(0,24+1-x[1]*i):
                for r in range(0,24+1-x[0]*j):
                    white = calIntegralImage(integralInput,x[0]*j + r - 1,int(x[1]*i/2) + c - 1,currentFeat.shape[0],int(currentFeat.shape[1]/2))
                    black = calIntegralImage(integralInput,x[0]*j + r - 1,x[1]*i + c - 1,currentFeat.shape[0],int(currentFeat.shape[1]/2))
                    featuresVec[featuresVecCounter] = white-black
                    featuresVecCounter = featuresVecCounter + 1
                
            
    #fileInput.close()
    #return values
    '''
    getting all the features of the shape 2x1

    '''
    x = features[1] # x would hold feature 2x1

    for i in range(1,int(24/2)+1): # from i = 1 to i = 12
        for j in range(1,24+1): # from i = 1 to i = 24
            currentFeat = np.zeros((x[0]*i,x[1]*j))
            for c in range(0,24+1-x[1]*j):
                for r in range(0,24+1-x[0]*i):
                    white = calIntegralImage(integralInput,int(x[0]*i/2) + r - 1,x[1]*j + c - 1,int(currentFeat.shape[0]/2),currentFeat.shape[1])
                    black = calIntegralImage(integralInput,x[0]*i + r - 1,x[1]*j + c - 1,int(currentFeat.shape[0]/2),currentFeat.shape[1])
                    featuresVec[featuresVecCounter] = white-black
                    featuresVecCounter = featuresVecCounter + 1
                
    '''
    getting all the features of the shape 1x3

    '''
    x = features[2] # x would hold featue 1x3

    for i in range(1,int(24/3)+1): # from i = 1 to i = 8
        for j in range(1,24+1): # from i = 1 to i = 24
            currentFeat = np.zeros((x[0]*j,x[1]*i))
            for c in range(0,24+1-x[1]*i):
                for r in range(0,24+1-x[0]*j):
                    white = calIntegralImage(integralInput,x[0]*j + r - 1,int(x[1]*i/3) + c - 1 ,currentFeat.shape[0],int(currentFeat.shape[1]/3))
                    black = calIntegralImage(integralInput,x[0]*j + r - 1, int(x[1]*i*(2/3)) + c - 1,currentFeat.shape[0],int(currentFeat.shape[1]/3))
                    white = white + calIntegralImage(integralInput,x[0]*j + r - 1,x[1]*i + c - 1,currentFeat.shape[0],int(currentFeat.shape[1]/3))
                    featuresVec[featuresVecCounter] = white-black
                    featuresVecCounter = featuresVecCounter + 1
       
    '''
    getting all the features of the shape 3x1

    '''
    x = features[3] # x would hold feature 3x1

    for i in range(1,int(24/3)+1): # from i = 1 to i = 8
        for j in range(1,24+1): # from i = 1 to i = 24
            currentFeat = np.zeros((x[0]*i,x[1]*j))
            for c in range(0,24+1-x[1]*j):
                for r in range(0,24+1-x[0]*i):
                    white = calIntegralImage(integralInput,int(x[0]*i/3) + r - 1, x[1]*j + c - 1 ,int(currentFeat.shape[0]/3),currentFeat.shape[1])
                    black = calIntegralImage(integralInput,int(x[0]*i*(2/3)) + r - 1, x[1]*j + c - 1,int(currentFeat.shape[0]/3),currentFeat.shape[1])
                    white = white + calIntegralImage(integralInput,x[0]*i + r - 1,x[1]*j + c - 1,int(currentFeat.shape[0]/3),currentFeat.shape[1])
                    featuresVec[featuresVecCounter] = white-black
                    featuresVecCounter = featuresVecCounter + 1
           

    '''
    getting all the features of the shape 2x2

    '''
    x = features[4] # x would hold feature 2x2

    for i in range(1,int(24/2)+1): # from i = 1 to i = 12
        for j in range(1,int(24/2)+1): # from i = 1 to i = 12
            currentFeat = np.zeros((x[0]*i,x[1]*j))
            for c in range(0,24+1-x[1]*j):
                for r in range(0,24+1-x[0]*i):
                    white = calIntegralImage(integralInput,int(x[0]*i/2) + r - 1,int(x[1]*j/2) + c - 1,int(currentFeat.shape[0]/2),int(currentFeat.shape[1]/2))
                    white = white + calIntegralImage(integralInput,x[0]*i + r - 1, x[1]*j + c - 1,int(currentFeat.shape[0]/2),int(currentFeat.shape[1]/2))
                    black = calIntegralImage(integralInput,x[0]*i - 1 + r,int(x[1]*j/2) + c - 1,int(currentFeat.shape[0]/2),int(currentFeat.shape[1]/2))
                    black = black + calIntegralImage(integralInput,int(x[0]*i/2)- 1 + r,x[1]*j + c - 1,int(currentFeat.shape[0]/2),int(currentFeat.shape[1]/2))
                    featuresVec[featuresVecCounter] = white-black
                    featuresVecCounter = featuresVecCounter + 1
           
    fileInput.close()
    return featuresVec
    
if __name__ == '__main__':
    HaarFeatures()