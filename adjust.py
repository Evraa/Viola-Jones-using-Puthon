import os,copy
import numpy as np
from classifiers import getLayers

new_file = open("detect_3_modified_with_features.txt","w+")
features = open("160Kfeatures.txt","r")
fearuers_lines = features.readlines()
clfs = getLayers()

for clf in clfs:
    feature_index = clf[0]
    line = fearuers_lines[feature_index]

    string_line = "["
    string_line += (str(line))
    string_line = string_line.replace(" ", ', ')
    string_line = string_line.replace("\n", ', ') 
    string_line+= str(clf[1]) + ", " + str(clf[2])+", " + str(clf[3]) + " ], "
    new_file.write(string_line)
    new_file.write("\n")

new_file.close()
features.close()




# file_mod = open("detect_1_unmodified.txt","r")
# new_file = open("detect_2_modified.txt","w+")
# all_lines = file_mod.readlines()
# for line in all_lines:
#     string_line = ""
#     string_line+= line
#     #string_line =  np.asarray(line)
#     #string_line = string_line.astype('string')
#     list1 = list(string_line)
#     list1[0] = '['
#     list1[len(line) - 3] = ']'
#     string_line = ''.join(list1)
#     new_file.write(string_line)

# new_file.close()
# file_mod.close()

# all_lines_Array = np.asarray(all_lines)
# vec_lines = all_lines_Array.astype('float64') 
