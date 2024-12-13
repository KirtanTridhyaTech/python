# app.py
import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Load your dataset
data = pd.read_csv('your_data.csv')

# Create widgets for filtering data
# Slider for selecting a range of values
min_value = st.slider('Select minimum value', min_value=0, max_value=100, value=20)
max_value = st.slider('Select maximum value', min_value=0, max_value=100, value=80)

# Selectbox for choosing a category
category = st.selectbox('Select a category', options=data['category_column'].unique())

# Checkbox for additional filtering
show_only_selected = st.checkbox('Show only selected category')

# Filter the data based on user input
filtered_data = data[(data['value_column'] >= min_value) & (data['value_column'] <= max_value)]
if show_only_selected:
    filtered_data = filtered_data[filtered_data['category_column'] == category]

# Display filtered data
st.write(filtered_data)

# Prepare data for linear regression
X = filtered_data[['feature1', 'feature2']]  # Replace with your feature columns
y = filtered_data['target']  # Replace with your target column

# Train the model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

# User input for prediction
input_feature1 = st.number_input('Input feature 1', value=0.0)
input_feature2 = st.number_input('Input feature 2', value=0.0)

# Make prediction
if st.button('Predict'):
    prediction = model.predict([[input_feature1, input_feature2]])
    st.write(f'Predicted value: {prediction[0]}')