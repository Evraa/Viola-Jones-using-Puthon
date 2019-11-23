from auxilaryFunctions import *
from Haar import HaarFeatures

#zero mean and unit variane images
#get the integral image
#apply the 160K haar features
    #add for each feature vector the new image's value
#result: 160K vector --> contains #of pictures elements

faces_path = "D:/Part C/College Stuff/3A/Image Processing/IP project/dataset/Small Images/faces_rgb_small_2/"
non_faces_path = "D:/Part C/College Stuff/3A/Image Processing/IP project/dataset/Small Images/non_faces_rgb_small/"
faces = os.listdir(faces_path)
non_faces = os.listdir(non_faces_path)

for face in faces:
    img_path = faces_path + face
    img = io.imread(img_path)
    print (img)
    norm_img = normalizeImages(img)
    ii_image = integralImage(norm_img)
    HaarFeatures(ii_image)
    print ("HI")

