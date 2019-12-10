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
#  