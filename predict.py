import numpy as np
from skimage.io import imread

import tensorflow as tf
from tensorflow import keras

label_list = ["bolt", "locating pin", "nut", "washer"]

filepath = input("Enter relative file path: ")
inp = imread(filepath, as_gray=True)
if inp.shape != (224,224):
    print("Error: Image size has to be 224x224 pixels")
else:
    inp_arr = inp.reshape((1,224,224,1))

    model = keras.models.load_model("finalmodel.h5")

    outp_arr = model.predict([inp_arr])
    outp_label = label_list[np.argmax(outp_arr)]
    print("The predicted fastener type is :", outp_label)


