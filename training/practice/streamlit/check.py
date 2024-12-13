import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Sample data for demonstration
data = {
    'bedrooms': [1, 2, 3, 4, 5],
    'square_footage': [500, 800, 1200, 1500, 2000],
    'price': [100000, 150000, 200000, 250000, 300000]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Train a linear regression model
X = df[['bedrooms', 'square_footage']]
y = df['price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

# Streamlit app layout
st.title("House Price Prediction App")

# Input widgets for user input
bedrooms = st.number_input("Number of Bedrooms", min_value=1, max_value=10, value=3)
square_footage = st.number_input("Square Footage", min_value=500, max_value=5000, value=1500)

# Predicting the price
if st.button("Predict Price"):
    input_data = [[bedrooms, square_footage]]
    predicted_price = model.predict(input_data)
    st.success(f"The predicted house price is: ${predicted_price[0]:,.2f}")
