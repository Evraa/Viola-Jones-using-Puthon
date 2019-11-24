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
def HaarFeatures(image=None):
    fileInput = open("HaarF.txt","w+")
    x = features[0]
    values = np.zeros([1,30000])
    k = 0
    for i in range(1,int(24/2)+1): # from i = 1 to i = 13
        for j in range(1,24+1): # from j = 1 to j = 24
            # p_x = 0
            # p_y = 0
            # #I think now u got the idea, tommorrow, work with muhammed on it 
            # j_half = int(j/2)
            # my_point_x = 11
            # my_point_y = 11

            # bottom = j_half + my_point_y - 1
            # up =  my_point_y - j_half - 2
            # right = my_point_x + i    
            # left = my_point_x - i
            # #print (image)
            # if(up<0):
            #     up_middle = 0
            #     up_left = 0
            #     up_right = 0
            # else:
            #     up_middle = image[my_point_x,up]
            #     up_left = image[left,up]
            #     up_right = image[right,up]
            
            # bottom_middle = image[my_point_x,bottom] 
            # bottom_left = image[left,bottom]
            # bottom_right = image[right,bottom]

            # area1 = bottom_middle - up_middle - bottom_left + up_left
            # area2 = bottom_right - up_right - bottom_middle + up_middle
            # S = area1 - area2
            # values[0,k] = S
            # k +=1
            # fileInput.write(str(S) + "\n")
            
    fileInput.close()
    return values
    '''
    getting all the features of the shape 2x1
    '''
    x = features[1]
    for i in range(1,int(24/2)+1): # from i = 1 to i = 12
        for j in range(1,24+1): # from i = 1 to i = 24
            currentFeat = np.zeros((x[0]*i,x[1]*j))
            currentFeat[0:int(x[0]*i/2),:] = 1 # the first vertical half
            currentFeat[int(x[0]*i/2):,:] = -1 # the second vertical half
            
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
           
    fileInput.close()

    
if __name__ == '__main__':
    HaarFeatures()