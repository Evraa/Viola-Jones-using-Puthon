from auxilaryFunctions import np
from auxilaryFunctions import calIntegralImage
from auxilaryFunctions import Grey_img,integralImage,Image,np,io,get_integral_image
from classifiers import getLayers
import time,math

def computerFeatureFunc(box,featureChosen,integralImg):
    #scaling features
    boxSize = box[0]
    # @ TODO the calFeatures file
    #featureChosen = features[featureIndex] # features should be from the calFeatures file 
    pattern = featureChosen[0]
    areaPos_i = box[1]
    areaPos_j = box[2]
    sampleSize = 24
    scale = np.sqrt(boxSize) / sampleSize
    
    #scaling the i and j of the feature
    i = featureChosen[1]
    j = featureChosen[2]
    i = int(scale*i + 0.5)
    j = int(scale*j + 0.5)

    #abs_i and abs_j will be used to calculate the integral image result
    #indicate the feature position inside the real frame
    abs_i = areaPos_i + i
    abs_j = areaPos_j + j


    #getting the haar feature width and height
    #we will check on the feature pattern to get the width
    width = featureChosen[4] + featureChosen[5] + featureChosen[6] if pattern <= 2 else featureChosen[6]
    width += featureChosen[5] if pattern == 5 else 0 # as feature five width is at 5,6
    #we will check on the feature pattern to get the height
    height = featureChosen[3] if pattern <= 2 else featureChosen[3] + featureChosen[4]
    # feature five height is at 3,4 while feature three and four their heights is at 3,4,5
    height += featureChosen[5] if (pattern > 2 and pattern < 5) else 0 

    #original area of the feature
    originArea = width*height

    #scaling the width and the height of the feature
    width = int(scale*width + 0.5)
    height = int(scale*height + 0.5)

    #scaling the feature pattern one i.e. 1x2 feature
    if(pattern == 1):
        '''
        the height of the feature may exceeds the box's size - i as
        boxSize - i is the maximum side the feature's height can hold
        '''
        height = height if height < (np.sqrt(boxSize) - i) else (np.sqrt(boxSize) - i) 
        
        '''
        the width of the feature may exceeds the box's size - j as
        boxSize - j is the maximum side the feature's width can hold
        '''
        #we should make sure that width is divisible by 2 after scaling
        width = width if width % 2 == 0 else width + 1
        
        while (width > np.sqrt(boxSize) - j):
            width -= 2
            
        #the increment slice which would indicate the size of the white and black areas
        increment = int(width / 2)
        #then calculate the integral image
        #summation of the white area
        white = calIntegralImage(integralImg,abs_i,abs_j,increment,height)
        #summation of the black area
        black = calIntegralImage(integralImg,abs_i,abs_j+increment,increment,height)
        featureResult = (white-black)
        #rescale the feature to its original scale
        #multiply the originArea by 2
        reScale = originArea/(width*height)
        
        featureResult = featureResult * reScale
        return featureResult

    #scaling the feature pattern two i.e. 1x3 feature
    elif(pattern == 2):
        '''
        the height of the feature may exceeds the box's size - i as
        boxSize - i is the maximum side the feature's height can hold
        '''
        height = height if height < (np.sqrt(boxSize) - i) else (np.sqrt(boxSize) - i) 
        #we should make sure that width is divisible by 3 after scaling
        width = width if width % 3 == 0 else ((width + 2 if width % 3 == 1 else width + 1)) 

        '''
        the width of the feature may exceeds the box's size - j as
        boxSize - j is the maximum side the feature's width can hold
        '''
        while (width > np.sqrt(boxSize) - j):
            width -= 3
            
        #the increment slice which would indicate the size of the white and black areas
        increment = int(width / 3)
        
        #then calculate the integral image
        #summation of the first white area
        white = calIntegralImage(integralImg,abs_i,abs_j,increment,height)
        #summation of the black area
        black = calIntegralImage(integralImg,abs_i,abs_j+increment,increment,height)
        #summation of the second and the first white area
        white = white + calIntegralImage(integralImg,abs_i,abs_j+2*increment,increment,height)
        featureResult = (white-black)
        #rescale the feature to its original scale
        #multiply the originArea by 3
        reScale = originArea/(width*height)

        featureResult = featureResult * reScale
        return featureResult

    #scaling the feature pattern one i.e. 2x1 feature
    elif(pattern == 3):
        
        '''
        the width of the feature may exceeds the box's size - j as
        boxSize - j is the maximum side the feature's width can hold
        '''
        width = width if width < (np.sqrt(boxSize) - j) else (np.sqrt(boxSize) - j)
        
        '''p
        the height of the feature may exceeds the box's size - i as
        boxSize - i is the maximum side the feature's height can hold
        '''
        #we should make sure that height is divisible by 2 after scaling
        height = height if height % 2 == 0 else height + 1
        
        while (height > np.sqrt(boxSize) - i):
            height -= 2
            
        #the increment slice which would indicate the size of the white and black areas
        increment = int(height / 2)
        
        #then calculate the integral image
        #summation of the white area
        white = calIntegralImage(integralImg,abs_i,abs_j,width,increment)
        #summation of the black area
        black = calIntegralImage(integralImg,abs_i+increment,abs_j,width,increment)
        featureResult = (white-black)
        #rescale the feature to its original scale
        #multiply the originArea by 2
        reScale = originArea/(width*height)
        
        featureResult = featureResult * reScale
        return featureResult
        
    #scaling the feature pattern one i.e. 3x1 feature
    elif(pattern == 4):
        
        '''
        the width of the feature may exceeds the box's size - j as
        boxSize - j is the maximum side the feature's width can hold
        '''
        width = width if (width < (np.sqrt(boxSize) - j)) else (np.sqrt(boxSize) - j) 
        
        '''
        the height of the feature may exceeds the box's size - i as
        boxSize - i is the maximum side the feature's height can hold
        '''
        #we should make sure that height is divisible by 3 after scaling
        height = height if height % 3 == 0 else ((height + 2 if height % 3 == 1 else height + 1))
        
        while (height > np.sqrt(boxSize) - i):
            height -= 3
            
        #the increment slice which would indicate the size of the white and black areas
        increment = int(height / 3)
        
        #then calculate the integral image
        #summation of the first white area
        white = calIntegralImage(integralImg,abs_i,abs_j,width,increment)
        #summation of the black area
        black = calIntegralImage(integralImg,abs_i+increment,abs_j,width,increment)
        #summation of the second and the first white area
        white = white + calIntegralImage(integralImg,abs_i+2*increment,abs_j,width,increment)
        featureResult = (white-black)
        #rescale the feature to its original scale
        #multiply the originArea by 2
        reScale = originArea/(width*height)

        featureResult = featureResult * reScale
        return featureResult

    #scaling the feature pattern one i.e. 2x2 feature
    else:
        
        '''
        the width of the feature may exceeds the box's size - j as
        boxSize - j is the maximum side the feature's width can hold
        '''
        #we should make sure that width is divisible by 2 after scaling
        width = width if width % 2 == 0 else width + 1
        
        while (width > np.sqrt(boxSize) - j):
            width -= 2
        
        '''
        the height of the feature may exceeds the box's size - i as
        boxSize - i is the maximum side the feature's height can hold
        '''
        #we should make sure that height is divisible by 2 after scaling
        height = height if height % 2 == 0 else height + 1
        
        while (height > np.sqrt(boxSize) - i):
            height -= 2
            
        #the increment slices which would indicate the size of the white and black areas
        incrementH = int(height / 2) # increment Height
        incrementW = int(width / 2) # increment Width
        
        #then calculate the integral image
        
        #summation of the first white area
        white = calIntegralImage(integralImg,abs_i,abs_j,incrementW,incrementH)
        #summation of the first and the second white areas
        white = white + calIntegralImage(integralImg,abs_i+incrementH,abs_j+incrementW,incrementW,incrementH)
        
        #summation of the black area
        black = calIntegralImage(integralImg,abs_i+incrementH,abs_j,incrementW,incrementH)
        #summation of the second and the first black area
        black = black + calIntegralImage(integralImg,abs_i,abs_j+incrementW,incrementW,incrementH)
        
        featureResult = (white-black)
        #rescale the feature to its original scale
        reScale = originArea/(width*height)

        featureResult = featureResult * reScale
        return featureResult

#return rects
stepSizeW = 20
stepSizeH = 20
minSize = 24
sizeStep = 6
class Rect:
    def __init_(self, startBox, endBox):
        self.startBox = startBox
        self.endBox = endBox
def detect_face(frame, frameWidth, frameHeight):
    rects = []
    startBox = (0,0)
    endBox = (startBox[0]+minSize, startBox[1]+minSize)
    minFrame = frameWidth if frameWidth < frameHeight else frameHeight
    for b in range(minSize,minFrame,step=sizeStep):
        for w in range(frameWidth-b,step=stepSizeW):
            for h in range(frameHeight-b, step=stepSizeH):
                startBox = (w,h)
                endBox = (w+b, h+b)
                rect_object = Rect(startBox, endBox)
                if(cascading(rect_object)):
                    rects.append([rect_object])
    return rects

def cascading(rect_object):
    isFace = False
    start = time.time()
    #Read an image and convert it into Gray
    img = io.imread("img2.JPG")
    img = Grey_img(img)
    iimg = get_integral_image(img)
    
    end1 = time.time()
    print ("Reading img and getting its integral: ",end1-start)
    
    Layers = getLayers()
    
    end2 = time.time()
    print ("Obtaining Layers in: ",end2-end1)
    stage =[]
    layer = Layers[0]
    for feature in layer:
        feature_id = feature[0:7]
        areaBox = (rect_object.endBox[0] - rect_object.startBox[0]) ** 2
        BoxI = rect_object.startBox[1]
        BoxJ = rect_object.startBox[0]
        feature_value = (computerFeatureFunc([areaBox,BoxI,BoxJ],feature_id,iimg))
        #Still didint add the tweak value
        if feature_value > feature[8]: 
            vote = feature[9]
        else:
            vote = -feature[9]
        
        #no 0.5 since only sign matters
        prediction = vote*math.log(1/feature[7] -1)
        print (prediction)
    return isFace