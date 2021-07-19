# Fasteners Image Classification
This project aims to design, build, train and tune a CNN to classify a set of images belonging to the different classes of mechanical fasteners; namely nuts, bolts, washers and locating pins. The repo has 3 files, named and described as follows:

* `data_storage.py` : python script that takes the image files and converts them into NumPy arrays that are the stored into `.npy` files to allow for immediate loading and use in the notebook. Check before running to ensure the file paths used are according to your folder structure and storage
* `chech_data.py` : after the `images.npy` and `labels.npy` files are created using the script above, this script can be run them and ensure everything is stored and can be retrieved easily. Takes an index as input and outputs the corresponding label and image
* `modelling.ipynb` : created in Google Colab and implements the deep learning algorithm for our presented problem. It has descriptions and notes throughout to report on the *what, how and why* of the model.
* `finalmodel.h5` : the final trained model, to be used for application oriented scripts or deployment in some other project. File size is too large, so GitHub will not display a preview.
* `predict.py` : python script that takes the relative path of a test image as input then loads in the trained model (`finalmodel.h5` in our case) to make a prediction. The predicted label is then displayed.
* `test1.png` & `test2.jpg` : images to test the `predict.py` script. The first is a picture of a nut taken directly from our dataset while the second is a picture of a bolt taken from Google Images (i.e. true unseen data). Both images are in the required dimension of 224x224 pixels.

### Data:

The data used here was obtained from the GitHub repo titled ["Mech-parts-classification-seq-model"](https://github.com/Promech2020/Mech-parts-classification-seq-model) of [Pro-Mech Minds](https://www.promechminds.com/). When the Shell script (given in the repo) is run, a zipped folder by the name `blnw-images-224.zip` is downloaded. Extract it to a folder named `data` with your project folder. Your `data_storage.py` should be stored in your project folder. Verify that opening the extracted folder shows 4 subfolders with the name of the respective class.

Or, you could ignore the above instructions and make necessary changes to the script and notebook according to your liking.

### Dependencies:

python = 3.7.4  
tensorflow = 2.4.0  
jupyterlab = 2.2.8  
matplotlib = 3.3.1  
numpy = 1.19.1  
pandas = 1.1.1  
scikit-image = 0.18.1  
scikit-learn = 0.24.1  

### Note:
All references to external resources are present as links in the respective words or phrases instead of a traditional reference section.  

### Possible Updates:
The script for predicting the label for a test image only takes images of the expected dimension (224x224) as input. It can be modified such that it only accepts square images and then scales them down to the required dimension. Solutions for doing the same with rectangular images (width not equal to height) can also be tried and implemented accordingly.