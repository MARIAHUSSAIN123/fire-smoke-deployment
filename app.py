import streamlit as st
import numpy as np
from tensorflow import keras
from PIL import Image

st.set_page_config(page_title="Fire / Smoke / Normal Detection", page_icon="🔥")

IMG_SIZE = (224, 224)
class_names = ["Fire", "Normal", "Smoke"]


@st.cache_resource
def load_model():
    return keras.models.load_model("fire_smoke_detector.keras")


model = load_model()

st.title("🔥 Fire / Smoke / Normal Detection — Live Demo")
st.write(
    "Upload an image to check if it shows fire, smoke, or a normal scene. "
    "Model: MobileNetV2 (Transfer Learning)."
)

uploaded_file = st.file_uploader(
    "Upload an image (CCTV / surveillance frame)", type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    img = Image.open(uploaded_file).convert("RGB")
    st.image(img, caption="Uploaded image", use_column_width=True)

    resized = img.resize(IMG_SIZE)
    arr = keras.utils.img_to_array(resized)
    arr = np.expand_dims(arr, axis=0)
    probs = model.predict(arr, verbose=0)[0]

    result = {class_names[i]: float(probs[i]) for i in range(len(class_names))}
    sorted_result = dict(sorted(result.items(), key=lambda x: x[1], reverse=True))

    st.subheader("Prediction")
    for label, prob in sorted_result.items():
        st.write(f"**{label}**: {prob * 100:.1f}%")
        st.progress(prob)
