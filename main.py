from fastapi import FastAPI, UploadFile, File
from tensorflow import keras
from PIL import Image
import numpy as np
import io

app = FastAPI(
    title="Fire Smoke Normal Detection API",
    description="CNN-based Fire, Smoke and Normal Image Classification API",
    version="1.0.0"
)

IMG_SIZE = (224, 224)
CLASS_NAMES = ["Fire", "Normal", "Smoke"]

# Load trained model
model = keras.models.load_model("fire_smoke_detector.keras")


@app.get("/")
def home():
    return {
        "message": "Fire Smoke Detection API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "model": "loaded"
    }


@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    image_bytes = await file.read()

    image = Image.open(
        io.BytesIO(image_bytes)
    ).convert("RGB")

    image = image.resize(IMG_SIZE)

    image_array = keras.utils.img_to_array(image)

    image_array = np.expand_dims(
        image_array,
        axis=0
    )

    probabilities = model.predict(
        image_array,
        verbose=0
    )[0]

    predicted_index = int(
        np.argmax(probabilities)
    )

    predicted_class = CLASS_NAMES[predicted_index]

    confidence = float(
        probabilities[predicted_index]
    )

    return {
        "prediction": predicted_class,
        "confidence": round(confidence * 100, 2),
        "probabilities": {
            CLASS_NAMES[i]: round(float(probabilities[i]) * 100, 2)
            for i in range(len(CLASS_NAMES))
        }
    }
