import streamlit as st
from utils.prediction import predict_waste
from utils.database import insert_record
from PIL import Image
import datetime

st.set_page_config(page_title="EcoSort AI", layout="wide")

st.title("🌱 EcoSort AI - Smart Waste Classification System")

st.write("Upload an image of waste to classify and get recycling recommendations.")

uploaded_file = st.file_uploader(
    "Upload Image",
    type=["jpg", "png", "jpeg"]
)

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    result = predict_waste(image)

    label = result["category"]
    confidence = result["confidence"]
    recyclable = result["recyclable"]

    st.success(f"Waste Type: {label}")
    st.info(f"Confidence: {confidence}%")

    if recyclable:
        st.success("♻ Recyclable")
    else:
        st.warning("🗑 Non-Recyclable")

    # CO2 calculation
    co2_saved = 0

    if label.lower() == "plastic":
        co2_saved = 0.08
        rec = "Recycle in plastic bin"
    elif label.lower() == "paper":
        co2_saved = 0.05
        rec = "Recycle paper waste"
    elif label.lower() == "glass":
        co2_saved = 0.12
        rec = "Send to glass recycling"
    elif label.lower() == "metal":
        co2_saved = 0.10
        rec = "Send to metal recycling facility"
    elif label.lower() == "organic waste":
        co2_saved = 0.03
        rec = "Use composting methods"
    else:
        rec = "Dispose properly"

    st.subheader("♻ Recycling Recommendation")
    st.write(rec)

    st.subheader("🌍 Environmental Impact")
    st.write(f"CO₂ Saved: {co2_saved} kg")

    insert_record(
        label,
        confidence,
        co2_saved,
        datetime.datetime.now()
    )

st.sidebar.title("Navigation")
st.sidebar.info(
    "EcoSort AI helps reduce waste and improve recycling using AI."
)
