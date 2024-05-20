import pickle
from tensorflow.keras.models import load_model
import cv2
import numpy as np
from keras.models import load_model

model = load_model("./models/cnn.h5")
classes = pickle.load(open("./models/classes.sav", "rb"))


class Tensor:
    def __init__(self, image):
        self.image = image

    def predict_image(self):
        self.image = np.asarray(bytearray(self.image), dtype=np.uint8)
        self.image = cv2.imdecode(self.image, cv2.IMREAD_COLOR)
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        self.image = cv2.resize(self.image, dsize=(224, 224))
        self.image = self.image.astype("float32")
        self.image /= 255.0
        self.image = self.image[None, ...]
        result = model.predict(self.image)
        pred = result.argmax()
        return [classes[pred], int(result[0][pred] * 100)]
