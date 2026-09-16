# Plant Disease Prediction and Cure Recommendation 🌾

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)](https://tensorflow.org/)
[![Deep Learning](https://img.shields.io/badge/Deep%20Learning-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)](#)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Computer Vision](https://img.shields.io/badge/Computer%20Vision-FF6F00?style=for-the-badge&logo=opencv&logoColor=white)](#)

---

## 📌 Project Overview

A **deep learning system that classifies plant diseases from leaf images** and recommends appropriate cures/treatments — built to help farmers and gardeners quickly identify plant health issues and take action.

This project uses a **Convolutional Neural Network (CNN)** trained to classify plant leaf images across **38 disease categories** spanning multiple crop species, then maps the predicted disease to relevant treatment recommendations.

---

## 🧠 Model Details

| Aspect           | Details                        |
| ---------------- | ------------------------------- |
| **Architecture** | Convolutional Neural Network (CNN) |
| **Framework**    | TensorFlow / Keras              |
| **Classes**      | 38 (multiple plant species & diseases) |
| **Accuracy**     | 96% on test set                 |
| **Input**        | RGB leaf images (224×224 px)   |
| **Output**       | Disease class + cure recommendation |

---

## 🎯 Key Features

✅ **Image-based plant disease classification**
- Processes leaf images uploaded by users
- Real-time inference with sub-second predictions
- Handles various lighting conditions and angles

✅ **Multi-class classification (38 categories)**
- Covers multiple plant species:
  - Tomato, Potato, Corn, Grape, Apple, Pepper, Cherry, Squash, Cucumber, Orange
- Disease detection including:
  - Fungal infections
  - Bacterial infections
  - Viral infections
  - Nutrient deficiencies
  - Healthy leaf detection

✅ **Automated cure/treatment recommendation mapping**
- Maps predicted disease to appropriate treatments
- Includes organic and conventional options
- Severity-based recommendations

✅ **Interactive web interface**
- No setup required for end users
- Simple drag-and-drop image upload
- Real-time results and recommendations
- Mobile-friendly responsive design

---

## 🏗️ System Architecture

```
User Upload
    ↓
[Image Preprocessing]
  - Resize to 224×224
  - Normalize pixels
  - Apply augmentation
    ↓
[CNN Model]
  - Feature extraction
  - Disease classification
  - Confidence score
    ↓
[Treatment Mapper]
  - Disease → Cure database
  - Generate recommendations
    ↓
[Web Interface]
  - Display results
  - Show confidence
  - Provide guidance
```

---

## 📁 Repository Structure

```
Plant-disease-prediction-and-cure-recommendation/
│
├── model/
│   ├── trained_cnn_model.h5      # Trained model weights
│   ├── model_architecture.json   # Model structure
│   └── class_labels.json         # Disease class mapping
│
├── data/
│   ├── training_data/            # Training images (organized by class)
│   ├── test_data/                # Test images
│   └── disease_cures.json        # Disease-to-cure mapping
│
├── app.py                         # Streamlit web application
├── inference.py                   # Model inference pipeline
├── image_preprocessing.py         # Image processing utilities
├── recommendation_engine.py       # Cure recommendation logic
│
├── requirements.txt               # Python dependencies
├── .gitignore
└── README.md                      # Documentation
```

---

## 🛠️ Technical Stack

| Category              | Technologies         |
| ---------------------- | --------------------- |
| **Programming Language** | Python 3.8+         |
| **Deep Learning**      | TensorFlow, Keras     |
| **Web App**            | Streamlit             |
| **Image Processing**   | OpenCV, PIL/Pillow    |
| **Data Handling**      | NumPy, Pandas         |
| **Visualization**      | Matplotlib, Plotly    |

---

## ⚙️ Installation & Setup

### Prerequisites

Install **Python 3.8+**

### Step 1: Clone Repository

```bash
git clone https://github.com/RaghavendraDivate/Plant-disease-prediction-and-cure-recommendation.git
cd Plant-disease-prediction-and-cure-recommendation
```

### Step 2: Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

**Dependencies:**
```
tensorflow>=2.10.0
keras>=2.10.0
streamlit>=1.20.0
opencv-python>=4.7.0
pillow>=9.5.0
numpy>=1.24.0
pandas>=1.5.0
matplotlib>=3.7.0
```

---

## ▶️ Running the Application

### Start the Web App

```bash
streamlit run app.py
```

This launches the interactive interface at: **http://localhost:8501**

### Using the Application

1. **Upload Image**
   - Click "Upload a plant leaf image"
   - Select a JPG/PNG file (recommended: 224×224 px or larger)

2. **Get Prediction**
   - Click "Analyze Leaf"
   - Model processes the image
   - Displays disease classification with confidence score

3. **View Recommendations**
   - See predicted disease name
   - View cure/treatment recommendations
   - Get severity assessment
   - Read prevention tips

---

## 📊 How It Works

### 1. Image Upload
User uploads a photo of a plant leaf through the Streamlit interface

### 2. Preprocessing
- Image resized to 224×224 pixels
- Pixel values normalized to [0, 1]
- Applied data augmentation (rotation, zoom, brightness)

### 3. CNN Classification
- Preprocessed image passed to trained CNN
- Convolutional layers extract features
- Fully connected layers produce class probabilities
- Returns top predicted disease class + confidence score

### 4. Treatment Mapping
- Predicted disease class looked up in cure database
- Matching treatment recommendations retrieved
- Recommendations organized by:
  - Treatment type (organic/conventional)
  - Application method
  - Frequency
  - Expected recovery time

### 5. Results Display
- Disease name and confidence % shown
- Cure recommendations displayed
- Similar disease suggestions provided
- Prevention tips included

---

## 🎓 Skills Demonstrated

✅ **Convolutional Neural Networks (CNNs)**
- Architecture design and implementation
- Transfer learning and fine-tuning
- Image feature extraction

✅ **Image Classification**
- Multi-class image classification
- Handling imbalanced datasets
- Data augmentation techniques
- Model evaluation metrics

✅ **Deep Learning Frameworks**
- TensorFlow/Keras model development
- Model training and validation
- Hyperparameter tuning
- Model serialization and deployment

✅ **Web Application Development**
- Streamlit app development
- User interface design
- Real-time inference integration
- File upload handling

✅ **End-to-End ML Deployment**
- From model training to production app
- Interactive user-facing application
- Deployment-ready structure

---

## 🚀 Model Performance

| Metric               | Value      |
| -------------------- | ---------- |
| **Test Accuracy**    | 96%        |
| **Inference Time**   | <500ms     |
| **Model Size**       | ~150 MB    |
| **Supported Classes**| 38         |

---

## 🔧 Configuration

### Model Settings (in `app.py`)

```python
MODEL_PATH = "model/trained_cnn_model.h5"
CURES_DB_PATH = "data/disease_cures.json"
IMAGE_SIZE = (224, 224)
CONFIDENCE_THRESHOLD = 0.5
```

### Customization

- **Add new diseases:** Update `disease_cures.json`
- **Improve accuracy:** Retrain with more diverse images
- **Add languages:** Modify the UI text in `app.py`
- **Deploy to cloud:** Use Streamlit Cloud, Heroku, or AWS

---

## 📈 Future Enhancements

🔄 **Model Improvements**
- Fine-tune with additional crop varieties
- Implement ensemble methods
- Add severity/stage classification
- Multi-leaf analysis

🌐 **Feature Additions**
- Mobile app (Flutter/React Native)
- Offline mode capability
- Batch image processing
- Disease progression tracking
- Weather-based recommendations

📊 **Data & Analytics**
- User feedback loop for model improvement
- Regional disease prevalence tracking
- Seasonal disease patterns
- Treatment effectiveness logging

🔒 **Deployment**
- REST API for integration
- Database for user history
- Admin dashboard
- Multi-language support

---

## ⚠️ Important Disclaimer

**This is an academic/portfolio project (mini project).** 

Predictions and cure recommendations are for **informational and demonstrative purposes only** and should **NOT replace professional agricultural expertise or professional diagnosis**.

**Before applying any treatment:**
1. Consult with local agricultural extension services
2. Verify with professional plant pathologists
3. Consider local climate and crop varieties
4. Follow recommended safety guidelines
5. Use appropriate protective equipment

---

## 📚 Resources & References

- [TensorFlow/Keras Documentation](https://www.tensorflow.org/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Plant Diseases Database](https://plantvillage.psu.edu/)
- [CNN for Image Classification](https://cs231n.github.io/convolutional-networks/)
- [Transfer Learning Guide](https://www.tensorflow.org/tutorials/images/transfer_learning)

---

## 📝 License

This project is for educational purposes.

---

**Built to demonstrate deep learning for agricultural applications. Use responsibly! 🌱**
