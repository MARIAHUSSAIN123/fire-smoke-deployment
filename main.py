from fastapi import FastAPI, File, UploadFile
from tensorflow import keras
from PIL import Image
import numpy as np
import io

app = FastAPI(title="Fire Smoke Detection API")

IMG_SIZE = (224, 224)
class_names = ["Fire", "Normal", "Smoke"]

model = keras.models.load_model("fire_smoke_detector.keras")


@app.get("/")
def home():
    return {
        "message": "Fire Smoke Detection API is running"
    }


@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    image_bytes = await file.read()

    img = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    img = img.resize(IMG_SIZE)

    arr = keras.utils.img_to_array(img)
    arr = np.expand_dims(arr, axis=0)

    probs = model.predict(arr, verbose=0)[0]

    result = {
        class_names[i]: float(probs[i])
        for i in range(len(class_names))
    }

    predicted_class = class_names[np.argmax(probs)]
    confidence = float(np.max(probs))

    return {
        "prediction": predicted_class,
        "confidence": confidence,
        "probabilities": result
    }
