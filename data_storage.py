import os
import numpy as np
from skimage.io import imread, imshow
import matplotlib.pyplot as plt

mainpath = os.getcwd() + r"\data\blnw-images-224"
i=0
labels=dict()
datalist = []
labellist = []

for foldername in os.listdir(mainpath):
    subpath = mainpath + "\\" + foldername + "\\"
    labels[i] = foldername
    #print(subpath)
    #filelen = len(os.listdir(subpath))
    #print(filelen)
    #print(labels)
    
    for filename in os.listdir(subpath):
        filepath = subpath + filename
        #print(filepath)

        image = imread(filepath,as_gray=True)
        #print(image.shape)
        #imshow(image)
        #plt.show()
        #break

        datalist.append(image)
        labellist.append(i)

    i = i+1


#print(len(datalist))
#print(len(labellist))

datanp = np.array(datalist)
labelnp = np.array(labellist)
#print(datanp.shape, '\t', labelnp.shape)

np.save('images',datanp)
print("Image data saved")

np.save('labels',labelnp)
print("Label data saved")
print("Label dictionary reference: ", labels)


        
