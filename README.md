# Plant Disease Prediction and Cure Recommendation

A deep learning system that classifies plant diseases from leaf images and recommends appropriate cures/treatments — built to help farmers and gardeners quickly identify plant health issues and take corrective action.

---

## 📌 Project Overview

This project uses a Convolutional Neural Network (CNN) trained to classify plant leaf images across 38 disease categories (spanning multiple crop species), then maps the predicted disease to relevant cure/treatment recommendations. Deployed as an interactive Streamlit web app for easy, real-time use.

### Key Capabilities

* Image-based plant disease classification
* 38-class classification covering multiple plant species and diseases (including healthy leaf detection)
* Cure/treatment recommendation mapping based on predicted disease
* Interactive, no-setup web interface via Streamlit

---

# 🧠 Model Details

| Aspect           | Details                        |
| ---------------- | ------------------------------- |
| **Architecture** | Convolutional Neural Network (CNN) |
| **Framework**    | TensorFlow / Keras              |
| **Classes**      | 38 (multiple plant species & diseases) |
| **Accuracy**     | 96% on test set                 |

---

# 🏗️ Repository Architecture

```text
Plant-disease-prediction-and-cure-recommendation/
│
├── model/
│   └── Trained CNN model files
│
├── app.py
│   └── Streamlit application entry point
│
├── requirements.txt
│   └── Python dependencies
│
└── README.md
    └── Project documentation
```

---

# 🛠️ Technical Stack

| Category              | Technologies         |
| ---------------------- | --------------------- |
| **Programming Language** | Python              |
| **Deep Learning**      | TensorFlow, Keras     |
| **Web App**            | Streamlit             |

---

# ⚙️ Getting Started

## Prerequisites

Install **Python 3.8+**.

Install the required packages:

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the App

```bash
streamlit run app.py
```

This launches the interactive web interface where you can upload a leaf image and receive a disease prediction along with cure recommendations.

---

# 📊 How It Works

1. **Image Upload** — user uploads a photo of a plant leaf
2. **Preprocessing** — image is resized and normalized for model input
3. **Classification** — CNN predicts the disease class (or healthy) from 38 possible categories
4. **Cure Recommendation** — predicted disease is mapped to relevant treatment/remedy suggestions
5. **Display** — results shown in the Streamlit interface

---

# 🎓 Skills Demonstrated

This project demonstrates practical knowledge of:

* Convolutional Neural Networks (CNNs)
* Image classification
* TensorFlow / Keras model development
* Multi-class classification (38 classes)
* Streamlit application development
* End-to-end ML deployment (model → interactive app)

---

# 🚀 Project Objective

The objective of this project is to demonstrate an **end-to-end image classification pipeline**, from model training through deployment as an interactive, user-facing application, applied to a real-world agricultural use case.

---

## 📌 Disclaimer

This is an **academic / portfolio project** (mini project). Predictions and cure recommendations are for informational and demonstrative purposes only and should not replace professional agricultural or horticultural advice.
