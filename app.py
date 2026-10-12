
import streamlit as st
import joblib

st.set_page_config(page_title="Emotion Detection", page_icon="😊")

@st.cache_resource
def load_model():
    return joblib.load("emotion_model.pkl")

model = load_model()

st.title("😊 Emotion Detection")
st.write("Enter a sentence to predict its emotion.")

text = st.text_area(
    "Your text",
    placeholder="I am feeling very happy today!"
)

if st.button("Detect Emotion"):
    if text.strip():
        emotion = model.predict([text])[0]
        st.success(f"Predicted Emotion: {str(emotion).title()}")
    else:
        st.warning("Please enter some text.")
