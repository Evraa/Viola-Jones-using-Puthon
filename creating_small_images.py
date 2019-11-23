from auxilaryFunctions import os,resizeBy24x24

path = "D:/Part C/College Stuff/3A/Image Processing/IP project/dataset/non_faces_dataset/"
entries = os.listdir(path)
i = 0
rgb_path = "D:/Part C/College Stuff/3A/Image Processing/IP project/dataset/non_faces_rgb_small/"
for entry in entries:
    #entry is a file name
    img_path = path + entry
    img_down = resizeBy24x24(img_path)
    ext = ".jpg"
    img_down.save(rgb_path + str(i) + ext)
    i+=1