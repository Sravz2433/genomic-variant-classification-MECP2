import streamlit as st
import pandas as pd
import pickle
import numpy as np

# Set page title
st.title('ML Model Prediction App')

# Load the saved model
@st.cache_resource
def load_model():
    try:
        with open('models/xgboostmodel.pkl', 'rb') as file:
            model = pickle.load(file)
        return model
    except FileNotFoundError:
        st.error("Model file not found. Please make sure 'model.pkl' exists in the same directory.")
        return None

model = load_model()

# Create input form based on your model requirements
st.header('Enter Input Features')
    # Numeric inputs
feature1 = st.number_input('canonical SPDI', value=0.0)  
    # Add checkboxes for binary features
st.subheader('Molecular Features')
checkbox1 = st.checkbox('Feature 4')
checkbox2 = st.checkbox('Feature 5')
checkbox3 = st.checkbox('Feature 6')
    
    # Dropdown for categorical feature
feature5 = st.selectbox('Feature 7', options=[0, 1, 2, 3])
# Create prediction button
if st.button('Predict'):
    if model:
        # Create input array for prediction
        input_data = np.array([[feature1, checkbox1, checkbox2, checkbox3, feature5]])
        
        # Make prediction
        prediction = model.predict(input_data)
        
        # Display result
        st.success(f'Prediction: {prediction[0]}')
        
        # Optional: Display probability if it's a classification model
        if hasattr(model, 'predict_proba'):
            probabilities = model.predict_proba(input_data)
            st.write('Prediction Probabilities:')
            st.write(probabilities[0])