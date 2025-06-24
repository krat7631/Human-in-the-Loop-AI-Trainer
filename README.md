# 🧠 Human-in-the-Loop AI Trainer

A full-stack machine learning platform that lets humans correct model predictions, provide real-time feedback, and retrain classifiers on the fly. Built for transparency, continuous learning, and practical ML workflows.

---

## 🚀 Features

- ✍️ Text classification (toxic vs non-toxic) using TF-IDF + Logistic Regression  
- 🧩 Feedback loop: submit corrections when model is wrong  
- 🔁 Retraining button integrates feedback to improve the model  
- 📊 Streamlit UI with live confidence scores and results  
- 🔌 FastAPI backend with prediction, feedback, and retrain endpoints  

---

## 📦 Requirements

Make sure you have Python 3.8+ installed.  
Install the required packages via:

```bash
pip install -r requirements.txt
```

### `requirements.txt` contents:

```text
fastapi
uvicorn
scikit-learn
pandas
numpy
joblib
streamlit
requests
```

---

## 📂 Project Structure

```
human_in_the_loop_ai/
├── backend/
│   ├── app.py               # FastAPI server
│   ├── model.py             # Model logic (train/load/predict)
│   └── feedback_loop.py     # Feedback saving
├── frontend/
│   └── app.py               # Streamlit UI
├── data/
│   ├── comments.csv         # Initial dataset
│   └── user_feedback.csv    # Dynamic user feedback
├── requirements.txt         # Dependencies
```

---

## 🛠️ Getting Started

```bash
# Install dependencies
pip install -r requirements.txt

# Start the backend server
python -m uvicorn backend.app:app --reload

# In a new terminal, start the frontend
python -m streamlit run frontend/app.py
```

---

## 🧠 How It Works

1. User enters a text comment (e.g., Reddit, YouTube)  
2. Model classifies it as **Toxic (1)** or **Non-Toxic (0)**  
3. User provides feedback if the prediction is wrong  
4. Press **Retrain** to incorporate human corrections into a better model  

---

## ✅ Example Use Cases

- Moderation tools for forums or customer support  
- AI safety workflows with human feedback  
- Model transparency and explainability demonstrations  
- Teaching active learning concepts  

---

## 🌱 Suggested Improvements

This project is designed to be extended. Some ideas we encourage others to build upon:

- 🤖 Upgrade to BERT/DistilBERT for better NLP performance  
- 🔁 Implement active learning with uncertainty sampling  
- 📈 Track model metrics with MLflow or DVC  
- 🔍 Add SHAP/LIME explainability for model transparency  
- 🧠 Include multimodal inputs (images, audio)  

> These aren't oversights, but open invitations for contributors and students to evolve this into a research-level or production-grade system.

---

## 🤝 Contributing

We welcome improvements, issues, and forks. This project is a solid foundation — help us push the boundaries of real-world, human-centric machine learning!

---

## 📄 License

MIT License. Feel free to use, modify, and share with attribution.
