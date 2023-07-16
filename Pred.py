import cv2 as cv
import tensorflow as tf

Categories = []

def prepare(filepath):
    img_size = 300
    img_array = cv.imread(filepath, cv.IMREAD_GRAYSCALE)
    new_array = cv.resize(img_array, (img_size,img_size))
    return new_array.reshape(-1, img_size,img_size,3)

model = tf.keras.models.load_model("model_01-0.44.h5")

prediction = model.predict([prepare(r"C:\Users\acer\Desktop\Garbage Automation\New\metal.jpg")])
print(prediction)

