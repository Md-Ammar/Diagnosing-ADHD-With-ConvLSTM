import numpy as np
import tensorflow.keras as keras
from scipy.ndimage import zoom
import os
import nibabel as nib   
from scipy.ndimage import zoom


# Image Preprocessing Methods
def preprocess_image(img_path):
    time_length = 177
    img = nib.load(img_path)

    pp_img = None
    if img.shape[3] > time_length:
        pp_img = truncate_image(img)
    elif img.shape[3] < time_length:
        pp_img = pad_image(img)
    else:
        pp_img = img.get_fdata()

    # For each image at the index-th time step, do this
    new_x=28/49
    new_y=28/58
    new_z=28/47

    new_img = []
    for index in range(time_length):
        z_img = zoom(pp_img[:,:,:,index], (new_x,new_y,new_z), order=1)
        new_img.append(z_img.reshape((28,28,28,1)))

    f_img = np.array(new_img)
    return f_img

def truncate_image(img):
    time_length = 177
    return img.get_fdata()[:,:,:,:time_length]

def pad_image(img):
    x_dim = 49
    y_dim = 58
    z_dim = 47
    time_length = 177
    img_padding = np.expand_dims(np.zeros((x_dim,y_dim,z_dim)), axis=3)
    amt_to_fill = time_length - img.get_fdata().shape[3]
    padded_img = img.get_fdata()
    for _ in range(amt_to_fill):
        padded_img = np.append(arr=padded_img, values=img_padding, axis=3)

    return padded_img

# Load the model
model = keras.models.load_model(r'D:\All Projects\ML\ADHD\Diagnosing-ADHD-With-ConvLSTM-master\Notebooks\my_model.h5')

# Load the model
model = keras.models.load_model(r'D:\All Projects\ML\ADHD\Diagnosing-ADHD-With-ConvLSTM-master\Notebooks\my_model.h5')

# Make a prediction
prediction = model.predict(img)

# Print the prediction
print(prediction)

# Save the prediction
np.save('prediction.npy', prediction)

# Path: requirements.txt
# tensorflow==2.4.1
# nibabel==3.2.1
# scipy==1.6.2
# numpy==1.20.2
