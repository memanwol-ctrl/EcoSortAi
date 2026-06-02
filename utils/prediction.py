import random

classes = [
    "Plastic",
    "Paper",
    "Glass",
    "Metal",
    "Cardboard",
    "Organic Waste",
    "General Trash"
]

def predict_waste(image):
    prediction = random.choice(classes)
    confidence = random.randint(85, 99)

    return {
        "category": prediction,
        "confidence": confidence,
        "recyclable": prediction != "General Trash"
    }
