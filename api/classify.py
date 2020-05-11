import tensorflow as tf
import matplotlib.pyplot as pyplot
import matplotlib.image as mpimg
from tensorflow.keras.utils import CustomObjectScope

def Classify(filename):

    with CustomObjectScope({'softmax_v2': tf.keras.activations.softmax}):
        model = tf.keras.models.load_model('network.h5')

    img = mpimg.imread(filename)
    prediction = model.predict(img.reshape(1, 28, 28, 1))
    
    return prediction.argmax()