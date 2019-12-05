from auxilaryFunctions import os,resizeBy24x24,io,rgb2gray
import scipy.misc
save_path = "D:/Part C/College Stuff/3A/Image Processing/IP project/MY DATABASE/non_face_divided/"
non_faces_path = "D:/Part C/College Stuff/3A/Image Processing/IP project/dataset/non_faces_dataset/"
entries = os.listdir(non_faces_path)

def partition_2(image, size,name):
    n,m = image.shape
    step_n = n//size
    step_m = m//size
    #print (n,m,step_n,step_m)
    for j in range(size):
        for i in range(size):
            img_part = image[i*step_n:(i+1)*step_n , j*step_m:(j+1)*step_m]
            #print (img_part.shape)
            ext = ".jpg"
            scipy.misc.toimage(img_part).save(save_path + str(name) +'_'+ str(i)+'_'+str(j) +'_'+ ext)
'''
i = 0
for entry in entries:
    img_path = non_faces_path + entry
    image = io.imread(img_path)
    image = rgb2gray(image)
    partition_2(image,4,i)
    i+=1
'''
if __name__ == "__main__":
    i = 0
    entries = os.listdir(save_path)
    last_path = "D:/Part C/College Stuff/3A/Image Processing/IP project/MY DATABASE/non_faces_9856/"
    for entry in entries:
        #entry is a file name
        img_path = save_path + entry
        img_down = resizeBy24x24(img_path)
        ext = ".jpg"
        img_down.save(last_path + str(i) + ext)
        i+=1
        if (i%1000 == 0):
            print (i)