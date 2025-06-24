import streamlit as st
import requests

st.set_page_config(page_title="Human-in-the-Loop AI Trainer")
st.title("🧠 Human-in-the-Loop AI Trainer")

text_input = st.text_area("✏️ Enter a comment to classify:")

if st.button("🚀 Classify"):
    if text_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        response = requests.post("http://127.0.0.1:8000/predict", json={"texts": [text_input]})
        if response.ok:
            result = response.json()
            prediction = result["predictions"][0]
            confidence = max(result["probabilities"][0])
            st.success(f"**Prediction**: {'Toxic' if prediction == 1 else 'Non-Toxic'}")
            st.info(f"**Confidence**: {confidence:.2f}")

            if st.radio("Was this correct?", ["Yes", "No"]) == "No":
                label = st.radio("Then what is the correct label?", [0, 1])
                if st.button("Submit Feedback"):
                    requests.post("http://127.0.0.1:8000/feedback", json={"text": text_input, "label": label})
                    st.success("✅ Feedback submitted!")

if st.button("🔁 Retrain Model with Feedback"):
    response = requests.post("http://127.0.0.1:8000/retrain")
    if response.ok:
        st.success("Model retrained successfully!")
