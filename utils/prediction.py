import numpy as np
from PIL import Image
from utils.model_loader import model

labels = ["plastic", "paper", "glass", "metal", "organic", "trash"]

def predict_waste(image):
    image = image.resize((224, 224))
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)

    prediction = model.predict(image)
    class_index = np.argmax(prediction)

    label = labels[class_index]
    confidence = round(float(np.max(prediction)) * 100, 2)

    return label, confidence
