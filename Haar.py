from auxilaryFunctions import np

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

#Main Function:
'''
making the viola jones features and counting them
'''
'''
getting all the features of the shape 1x2
'''
def HaarFeatures():
    fileInput = open("HaarF.txt","w+")
    x = features[0]
    for i in range(1,int(24/2)+1): # from i = 1 to i = 12
        for j in range(1,24+1): # from i = 1 to i = 24
            currentFeat = np.zeros((x[0]*j,x[1]*i))
            currentFeat[:,0:int(x[1]*i/2)] = 1 # the first vertical half
            currentFeat[:,int(x[1]*i/2):] = -1 # the second vertical half
            arr = currentFeat.flatten()
            strg = str(arr)
            fileInput.write(strg)
            fileInput.write("\n")
            fileInput.write("\n")
    
    '''
    getting all the features of the shape 2x1
    '''
    x = features[1]
    for i in range(1,int(24/2)+1): # from i = 1 to i = 12
        for j in range(1,24+1): # from i = 1 to i = 24
            currentFeat = np.zeros((x[0]*i,x[1]*j))
            currentFeat[0:int(x[0]*i/2),:] = 1 # the first vertical half
            currentFeat[int(x[0]*i/2):,:] = -1 # the second vertical half
            arr = currentFeat.flatten()
            strg = str(arr)
            fileInput.write(strg)
            fileInput.write("\n")
            fileInput.write("\n")
    '''
    getting all the features of the shape 1x3
    '''
    x = features[2]

    for i in range(1,int(24/3)+1): # from i = 1 to i = 8
        for j in range(1,24+1): # from i = 1 to i = 24
            currentFeat = np.zeros((x[0]*j,x[1]*i))
            currentFeat[:,0:int(x[1]*i/3)] = 1 # from 0 to the 1st third column 
            currentFeat[:,int(x[1]*i/3):int(x[1]*i*(2/3))] = -1 # from 1st to the 2nd third column
            currentFeat[:,int(x[1]*i*(2/3)):] = 1 # from 2nd to the 3rd third column
            arr = currentFeat.flatten()
            strg = str(arr)
            fileInput.write(strg)
            fileInput.write("\n")
            fileInput.write("\n")
    '''
    getting all the features of the shape 3x1
    '''
    x = features[3]

    for i in range(1,int(24/3)+1): # from i = 1 to i = 8
        for j in range(1,24+1): # from i = 1 to i = 24
            currentFeat = np.zeros((x[0]*i,x[1]*j))
            currentFeat[0:int(x[0]*i/3),:] = 1 # from 0 to the 1st third column 
            currentFeat[int(x[0]*i/3):int(x[0]*i*(2/3)),:] = -1 # from 1st to the 2nd third column
            currentFeat[int(x[0]*i*(2/3)):,:] = 1 # from 2nd to the 3rd third column
            arr = currentFeat.flatten()
            strg = str(arr)
            fileInput.write(strg)
            fileInput.write("\n")
            fileInput.write("\n")

    '''
    getting all the features of the shape 2x2
    '''
    x = features[4]

    for i in range(1,int(24/2)+1): # from i = 1 to i = 12
        for j in range(1,int(24/2)+1): # from i = 1 to i = 12
            currentFeat = np.zeros((x[0]*i,x[1]*j))
            currentFeat[0:int(x[0]*i/2),0:int(x[1]*j/2)] = 1 # 1st quarter
            currentFeat[0:int(x[0]*i/2),int(x[1]*j/2):] = -1 # 2nd quarter
            currentFeat[int(x[0]*i/2):,0:int(x[1]*j/2)] = -1 # 3rd quarter
            currentFeat[int(x[0]*i/2):,int(x[1]*j/2):] = 1 # 4th quarter
            arr = currentFeat.flatten()
            strg = str(arr)
            fileInput.write(strg)
            fileInput.write("\n")
            fileInput.write("\n")
    fileInput.close()

    
if __name__ == '__main__':
    HaarFeatures()