from auxilaryFunctions import *
from Haar import HaarFeatures

#zero mean and unit variane images
#get the integral image
#apply the 160K haar features
    #add for each feature vector the new image's value
#result: 160K vector --> contains #of pictures elements

N_features = 162336
face_img = 13233
non_face_img = 9856
M_imgs = face_img + non_face_img

# def CREATE_FEATURES():
#     #3edl 3l path-->
#     faces_path = "MY DATABASE/faces_13233/"
#     non_faces_path = "MY DATABASE/non_faces_9856/"

#     faces = os.listdir(faces_path)
#     non_faces = os.listdir(non_faces_path)
    
#     i=0
#     face_feat_path = "Features/faces_feat/"
#     non_face_feat_path = "Features/non_faces_feat/"

#     for face in faces:
#         print ("Image: ",i,face)
#         img_str= face_feat_path + str(i) + ".txt"
#         fileInput = open(img_str,"w+") # assuming the image name would be stored in HaarF.txt   
        
#         img_path = faces_path + face
#         img = io.imread(img_path)

#         norm_img = normalizeImages(img)
#         ii_image = integralImage(norm_img)
#         vec = HaarFeatures(ii_image)
#         #This line deletes the image
#         #os.remove(img_path)
#         for j in range (N_features):
#             fileInput.write(str(vec[j]))
#             fileInput.write("\n")
#         fileInput.close()
#         i+=1
        
#     for non_face in non_faces:
#         print ("Image: ",i,non_face)
#         img_str= non_face_feat_path + str(i+1) +".txt"
#         fileInput = open(img_str,"w+") # assuming the image name would be stored in HaarF.txt    
#         img_path = non_faces_path + non_face
#         img = io.imread(img_path)
#         norm_img = normalizeImages(img)
#         ii_image = integralImage(norm_img)
#         vec = HaarFeatures(ii_image)
#         for j in range (N_features):
#             fileInput.write(str(vec[j]))
#             fileInput.write("\n")
#         fileInput.close()
#         i+=1
        
#     print ("Finished with i = " , i, "i supposed to equal: ",M_imgs)

def read_dataset():
    Ys = np.ones([M_imgs,1])
    for i in range (face_img,M_imgs):
        Ys[i,0] = -1
    
    Features_path = "Features/faces_feat/"
    features = os.listdir(Features_path)
    Xs = np.zeros([M_imgs,N_features])
    
    
    i = 0
    print(len(features))
    for feat in features:
        if (i%2000 == 0):
            print ("reading image: ",i)
        feature_file = Features_path + feat
        file_output = open(feature_file,"r")

        all_lines = file_output.readlines()
        all_lines_Array = np.asarray(all_lines)
        vec_lines = all_lines_Array.astype('float64')

        Xs[i,:] = vec_lines
        i+=1
        

    Features_path = "Features/non_faces_feat/"
    features = os.listdir(Features_path)

    for feat in features:
        if (i%2000 == 0):
            print ("reading image: ",i)
        feature_file = Features_path + feat
        file_output = open(feature_file,"r")
        all_lines = file_output.readlines()
        all_lines_Array = np.asarray(all_lines)
        vec_lines = all_lines_Array.astype('float64')
        Xs[i,:] = vec_lines
        i+=1
    
    return Xs,Ys



