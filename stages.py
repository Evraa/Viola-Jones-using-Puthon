#This function shpuld take a window with size e x e
# apply on it some funcitons:
# 1-Grey Scale
# 2-Integral Image
# 3-Pass that image through multiple stages,
#   for each stage it will be tested on some classifiers
#   these classifiers have the feature index, its threshold, its alpha and its polarity
#   so we should take that feature and apply it on the integral image
# 4- when it fails any Layer of classifiers, we should consider that window as FALSE
# 5- If it passed, then its a face

from auxilaryFunctions import Grey_img,integralImage,Image,np,io,get_integral_image
from classifiers import getLayers
from computeFeature import computerFeatureFunc
import time,math
if __name__ == "__main__":
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
        feature_value = (computerFeatureFunc([200*200,0,0],feature_id,iimg))
        #Still didint add the tweak value
        if feature_value > feature[8]: 
            vote = feature[9]
        else:
            vote = -feature[9]
        
        #no 0.5 since only sign matters
        prediction = vote*math.log(1/feature[7] -1)
        print (prediction)
        