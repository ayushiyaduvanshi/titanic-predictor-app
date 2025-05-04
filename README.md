# 🚢 Titanic Survival Predictor App

This is a Streamlit web application that predicts the survival of Titanic passengers based on their details like age, sex, ticket class, fare, and more. The model is trained on the Titanic dataset using a Random Forest Classifier.

---

## 🌟 Features

- Interactive web interface using Streamlit
- Predicts survival based on user input
- Built with a trained and optimized machine learning model
- Easy to deploy and use

---

## 🔧 Technologies Used

- Python 3.12+
- Streamlit
- Scikit-learn
- NumPy
- Joblib

---

## 📁 Project Structure

```
├── app.py                # Streamlit app
├── model.pkl             # Trained machine learning model
├── requirements.txt      # Python dependencies
```

---

## 🚀 How to Run Locally

1. Clone this repository:

```bash
git clone https://github.com/ayushiyaduvanshi/titanic-predictor-app.git
cd titanic-predictor-app
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
streamlit run app.py
```

---

## 🌐 Live Demo

Check out the app live on [Streamlit Cloud](https://titanic-predictor-app.streamlit.app)

---

## 📸 App Preview

![image](https://github.com/user-attachments/assets/26d50376-e8ab-4301-bc8f-a2ffdf9e9c80)


---

## 🧠 Model Info

The model used is a **Random Forest Classifier** trained using `GridSearchCV` for hyperparameter tuning. It was trained on the preprocessed Titanic dataset using features:

- Pclass
- Sex
- Age
- SibSp
- Parch
- Fare
- Embarked

---

## 🙌 Acknowledgements

- [Kaggle Titanic Dataset](https://www.kaggle.com/c/titanic)
- Streamlit for making ML deployment simple

---

## 📬 Contact

Made by Ayushi Yaduvanshi  
🔗 [LinkedIn](https://www.linkedin.com/in/ayushi-yaduvanshi/)

