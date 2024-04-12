import tensorflow as tf
from tensorflow.keras.models import load_model
import os

os.chdir(r"D:\All Projects\ML\ADHD\Diagnosing-ADHD-With-ConvLSTM-master\Notebooks")

# Load the Keras model
model = load_model("my_model.h5")

# Convert the model to the TensorFlow Lite format with quantization
converter = tf.compat.v1.lite.TFLiteConverter.from_keras_model_file("my_model.h5")

# Set the optimization flag
converter.optimizations = [tf.lite.Optimize.DEFAULT]

# Add SELECT_TF_OPS to the supported ops
converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS, tf.lite.OpsSet.SELECT_TF_OPS]

# Disable lowering tensor list ops
converter._experimental_lower_tensor_list_ops = False

# Convert the model
tflite_model = converter.convert()

# Save the model to disk
open("model.tflite", "wb").write(tflite_model)