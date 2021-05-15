import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imshow

imdata = np.load("images.npy")
labeldata = np.load("labels.npy")

print(imdata.shape)
print(labeldata.shape)

index = int(input("Enter image index: "))
while index >= 0 and index < imdata.shape[0]:
    print(labeldata[index])
    imshow(imdata[index])
    plt.show()
    index = int(input("Enter image index: "))

print("Index out of bound: Script ended")
