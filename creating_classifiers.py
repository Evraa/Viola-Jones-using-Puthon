from auxilaryFunctions import *
from Haar import HaarFeatures

#zero mean and unit variane images
#get the integral image
#apply the 160K haar features
    #add for each feature vector the new image's value
#result: 160K vector --> contains #of pictures elements

N_features = 162336
face_img = 100
non_face_img = 100
M_imgs = face_img + non_face_img

def CREATE_FEATURES():
    #3edl 3l path-->
    faces_path = "D:/Part C/College Stuff/3A/Image Processing/IP project/dataset/Small Images/faces_rgb_small/"
    non_faces_path = "D:/Part C/College Stuff/3A/Image Processing/IP project/dataset/Small Images/non_faces_rgb_small/"
    faces = os.listdir(faces_path)
    non_faces = os.listdir(non_faces_path)
    
    X = np.zeros((M_imgs,N_features))
    i=0
    feat_path = "D:/Part C/College Stuff/3A/Image Processing/IP project/Code/Small_features/HaarF_img_"
    '''
    for face in faces:
        print ("Image: ",i,face)
        img_str= feat_path + str(i+1) + ".txt"
        fileInput = open(img_str,"w+") # assuming the image name would be stored in HaarF.txt   
        
        img_path = faces_path + face
        img = io.imread(img_path)
        norm_img = normalizeImages(img)
        ii_image = integralImage(norm_img)
        X[i,:] = HaarFeatures(ii_image)
        for j in range (N_features):
            fileInput.write(str(X[i,j]))
            fileInput.write("\n")
        fileInput.close()
        i+=1
        '''
    '''
    for non_face in non_faces:
        print ("Image: ",i)
        img_str= feat_path + str(i+1) +".txt"
        fileInput = open(img_str,"w+") # assuming the image name would be stored in HaarF.txt    
        img_path = non_faces_path + non_face
        img = io.imread(img_path)
        norm_img = normalizeImages(img)
        ii_image = integralImage(norm_img)
        X[i,:] = HaarFeatures(ii_image)
        for j in range (N_features):
            fileInput.write(str(X[i,j]))
            fileInput.write("\n")
        fileInput.close()
        i+=1
    print ("Finished with i = " , i)
'''
def read_dataset(number_of_imgs=None):
    if number_of_imgs  != None:
        M_imgs = number_of_imgs

    
    Ys = np.ones([M_imgs,1])
    for i in range (non_face_img,M_imgs):
        Ys[i,0] = -1
    
    Features_path = "D:/Part C/College Stuff/3A/Image Processing/IP project/Code/Small_features/"
    features = os.listdir(Features_path)
    Xs = np.zeros([M_imgs,N_features])
    
    
    i = 0
    print(len(features))
    for feat in features:
        if (i%25 == 0):
            print ("image: ",i)
        feature_file = Features_path + feat
        file_output = open(feature_file,"r")
        all_lines = file_output.readlines()
        all_lines_Array = np.asarray(all_lines)
        vec_lines = all_lines_Array.astype('float64')
        Xs[i,:] = vec_lines
        i+=1
    return Xs,Ys

if __name__ == "__main__":
    #read_dataset(100)
    CREATE_FEATURES()

