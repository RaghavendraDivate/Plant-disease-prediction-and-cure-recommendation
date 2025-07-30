

import streamlit as st
import tensorflow as tf
import numpy as np

# TensorFlow Model Prediction
def model_prediction(test_image):
    model = tf.keras.models.load_model("trained_model.keras")
    image = tf.keras.preprocessing.image.load_img(test_image, target_size=(128, 128))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr])  # Convert single image to batch
    predictions = model.predict(input_arr)
    return np.argmax(predictions)  # Return index of max element

# Sidebar
st.sidebar.title("Dashboard")
app_mode = st.sidebar.selectbox("Select Page", ["Home", "About", "Disease Recognition"])
result_index = 0

# Main Page
if app_mode == "Home":
    st.header("PLANT DISEASE RECOGNITION SYSTEM")
    image_path = "home_page.jpeg"
    st.image(image_path, use_column_width=True)
    st.markdown("""
    Welcome to the Plant Disease Recognition System! 🌿🔍
    We aim to support farmers and gardeners by identifying plant diseases quickly and effectively. Let's work together to protect crops and ensure healthier harvests!

    ### How It Works
    1. Upload Image
    Navigate to the Disease Recognition page and upload a photo of the plant showing signs of disease.

    2. Image Analysis
    Our system uses cutting-edge algorithms to analyze the image and detect potential plant diseases.

    3. Get Results
    Review the analysis results along with actionable recommendations.

    4. Get Started
    Go to the Disease Recognition page in the sidebar, upload an image, and experience the benefits of our system firsthand!

    ### About Us :
    Visit the About page to learn more about the project, meet our team, and discover our mission to promote sustainable agriculture.
    """)

# About Project
elif app_mode == "About":
    st.header("About")
    st.markdown("""
                #### About Dataset
                This dataset is recreated using offline augmentation from the original dataset. The original dataset can be found on this GitHub repo.
                This dataset consists of about 87K RGB images of healthy and diseased crop leaves, categorized into 38 different classes. The total dataset is divided into an 80/20 ratio of training and validation set preserving the directory structure.
                A new directory containing 33 test images is created later for prediction purposes.
                #### Content
                1. train (70295 images)
                2. test (33 images)
                3. validation (17572 images)
                """)

# Prediction Page
elif app_mode == "Disease Recognition":
    st.header("Disease Recognition")
    test_image = st.file_uploader("Choose an Image:")

    # Display image when uploaded
    if test_image:
        st.image(test_image, width=400, use_column_width=True)

    # Predict button
    if st.button("Predict"):
        # st.snow()
        st.write("Our Prediction")
        result_index = model_prediction(test_image)

        # Reading Labels
        class_name = ['Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy',
                      'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew', 
                      'Cherry_(including_sour)___healthy', 'Corn_(maize)___Cercospora_leaf_spot_Gray_leaf_spot', 
                      'Corn_(maize)___Common_rust_', 'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy', 
                      'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 
                      'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot',
                      'Peach___healthy', 'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 
                      'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy', 
                      'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew', 
                      'Strawberry___Leaf_scorch', 'Strawberry___healthy', 'Tomato___Bacterial_spot', 
                      'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold', 
                      'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites_Two-spotted_spider_mite', 
                      'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus',
                      'Tomato___healthy']

        # Disease Cure Recommendations
        disease_cure = [
            ["1. Apply fungicides such as Mancozeb or Captan.",
         "2. Remove fallen leaves to prevent reinfection.",
         "3. Use resistant apple varieties."],
        ["1. Prune infected branches and dispose of them.",
         "2. Apply fungicides like Pyraclostrobin or Thiophanate-methyl.",
         "3. Remove and destroy infected fruit."],
        ["1. Remove infected leaves and branches.",
         "2. Apply fungicides like Chlorothalonil.",
         "3. Plant resistant apple varieties."],
        ["1. No treatment necessary; maintain proper care including watering and pruning."],
        ["1. No treatment necessary; continue proper care."],
        ["1. Apply fungicides like Sulfur or Myclobutanil.",
         "2. Prune to improve airflow and reduce humidity around the tree.",
         "3. Remove and destroy infected plant material."],
        ["1. No treatment necessary; continue with standard care practices."],
        ["1. Apply fungicides such as Chlorothalonil or Propiconazole.",
         "2. Remove and destroy infected plant debris.",
         "3. Use resistant corn varieties."],
        ["1. Apply fungicides such as Azoxystrobin.",
         "2. Remove and destroy infected leaves.",
        "3. Use resistant corn varieties."],
        ["1. Apply fungicides such as Propiconazole or Tebuconazole.",
        "2. Remove infected plant material.",
         "3. Use resistant corn varieties."],
        ["1. No treatment necessary; continue proper care practices."],
        ["1. Apply fungicides like Myclobutanil.",
         "2. Prune and remove infected fruit.",
         "3. Practice crop rotation to reduce disease buildup."],
        ["1. Remove infected plant material.",
         "2. Use resistant grape varieties.",
         "3. Apply fungicides like Chlorothalonil."],
        ["1. Remove infected leaves and debris.",
         "2. Apply fungicides like Mancozeb.",
         "3. Ensure proper spacing for air circulation."],
        ["1. No treatment necessary; continue with regular care and management."],
        ["1. Use insecticides to control the spread of citrus psyllids.",
         "2. Remove and destroy infected trees.",
         "3. There is no cure, so early detection and prevention are key."],
        ["1. Apply copper-based bactericides.",
         "2. Prune infected branches.",
        "3. Use resistant peach varieties."],
        ["1. No treatment necessary; maintain regular care practices."],
        ["1. Apply copper-based bactericides.",
         "2. Remove and destroy infected plant material.",
         "3. Rotate crops and use resistant varieties."],
        ["1. No treatment necessary; regular watering and care."],
        ["1. Apply fungicides like Chlorothalonil or Mancozeb.",
         "2. Remove and destroy infected plant debris.",
         "3. Use resistant potato varieties."],
        ["1. Apply fungicides like Metalaxyl or Mancozeb.",
         "2. Remove and destroy infected leaves and tubers.",
         "3. Use resistant varieties and practice proper irrigation."],
        ["1. No treatment necessary; regular care and pest management."],
        ["1. No treatment necessary; ensure proper care practices."],
        ["1. Apply fungicides like Sulfur or Myclobutanil.",
         "2. Remove and destroy infected leaves.",
         "3. Improve airflow around plants to reduce humidity."],
        ["1. Apply copper-based bactericides.",
         "2. Remove infected leaves and plant debris.",
         "3. Practice proper spacing to improve air circulation."],
        ["1. No treatment necessary; regular care including watering and weeding."],
        ["1. Apply copper-based bactericides.",
         "2. Remove and destroy infected plant material.",
         "3. Rotate crops to reduce the spread of bacteria."],
        ["1. Apply fungicides like Chlorothalonil or Mancozeb.",
         "2. Remove and destroy infected plant material.",
         "3. Use resistant tomato varieties."],
        ["1. Apply fungicides like Metalaxyl or Mancozeb.",
         "2. Remove and dispose of infected plant material.",
         "3. Use resistant varieties of tomatoes."],
        ["1. Apply fungicides like Mancozeb or Azoxystrobin.",
         "2. Improve air circulation around plants.",
         "3. Remove infected leaves and debris."],
        ["1. Apply fungicides like Chlorothalonil or Mancozeb.",
         "2. Remove infected leaves and improve airflow.",
         "3. Use resistant tomato varieties."],
        ["1. Apply miticides such as Spiromesifen or Avid.",
         "2. Spray plants with water to dislodge mites.",
         "3. Remove and destroy infected plant material."],
        ["1. Apply fungicides such as Chlorothalonil or Mancozeb.",
         "2. Remove infected plant material.",
         "3. Ensure proper spacing and airflow."],
        ["1. Use insecticides to control whiteflies.",
         "2. Remove infected plants and prevent reinfection.",
         "3. Use resistant tomato varieties."],
        ["1. Remove and destroy infected plants.",
         "2. Use virus-resistant tomato varieties.",
         "3. Disinfect tools and equipment to prevent spread."],
        ["1. No treatment necessary; maintain regular care and pest management."]
        ]

        # Displaying prediction and cure recommendation
        st.success(f"Model is predicting it's a {class_name[result_index]}")

        # Getting the cure recommendations
        cure_recommendation = disease_cure[result_index]
        formatted_recommendation = "\n".join(cure_recommendation)

        # Displaying cure recommendation in separate lines
        st.success(f"Cure Recommendation:\n{formatted_recommendation}")
