
import streamlit as st
import numpy as np
import joblib
model = joblib.load("model.pkl")

st.title("🚢 Titanic Survival Predictor")
st.write("Enter passenger details below to predict survival:")

# Input fields
pclass = st.selectbox("Passenger Class", [1, 2, 3])
sex = st.selectbox("Sex", ["Male", "Female"])
age = st.slider("Age", 0, 80, 25)
sibsp = st.number_input("Number of Siblings/Spouses Aboard (SibSp)", min_value=0, max_value=10, value=0)
parch = st.number_input("Number of Parents/Children Aboard (Parch)", min_value=0, max_value=10, value=0)
fare = st.slider("Fare Paid", 0.0, 500.0, 32.0)
embarked = st.selectbox("Port of Embarkation", ["Cherbourg", "Queenstown", "Southampton"])

# Preprocessing
sex = 1 if sex == "Male" else 0
embarked_map = {"Cherbourg": 0, "Queenstown": 1, "Southampton": 2}
embarked = embarked_map[embarked]

# Predict
features = np.array([[pclass, sex, age, sibsp, parch, fare, embarked]])

if st.button("Predict Survival"):
    prediction = model.predict(features)
    result = "🎉 Survived" if prediction[0] == 1 else "💀 Did Not Survive"
    st.subheader(f"Prediction: {result}")
