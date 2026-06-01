import streamlit as st
from utils.prediction import predict_waste
from utils.database import insert_record
from PIL import Image
import datetime

st.set_page_config(page_title="EcoSort AI", layout="wide")

st.title("🌱 EcoSort AI - Smart Waste Classification System")

st.write("Upload an image of waste to classify and get recycling recommendations.")

uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    label, confidence = predict_waste(image)

    st.success(f"Detected Waste: {label}")
    st.info(f"Confidence: {confidence}%")

    # CO2 calculation
    co2_saved = 0

    if label == "plastic":
        co2_saved = 0.08
        rec = "Recycle in plastic bin"
    elif label == "paper":
        co2_saved = 0.05
        rec = "Recycle paper waste"
    elif label == "glass":
        co2_saved = 0.12
        rec = "Send to glass recycling"
    else:
        rec = "Dispose properly"

    st.subheader("♻ Recycling Recommendation")
    st.write(rec)

    st.subheader("🌍 Environmental Impact")
    st.write(f"CO₂ Saved: {co2_saved} kg")

    # Save to database
    insert_record(
        label,
        confidence,
        co2_saved,
        datetime.datetime.now()
    )

st.sidebar.title("Navigation")
st.sidebar.info("EcoSort AI helps reduce waste and improve recycling using AI.")
