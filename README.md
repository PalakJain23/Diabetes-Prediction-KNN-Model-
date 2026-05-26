# 🩺 Diabetes Prediction using Machine Learning (KNN Model)

A complete Machine Learning + Flask web application that predicts whether a person is **Diabetic** or **Non-Diabetic** using the **K-Nearest Neighbors (KNN)** algorithm.

This project is built with:
- Machine Learning (KNN)
- Data Preprocessing
- Flask Backend
- HTML/CSS Frontend

---

# 🚀 Project Overview

Diabetes is a common chronic condition influenced by features like:
- glucose level  
- BMI  
- insulin  
- age  
- pregnancies  
- blood pressure  

This project uses an ML model trained on the **PIMA Indian Diabetes Dataset** to classify a patient as:

| Class | Meaning |
|---|---|
| Diabetic | High likelihood of diabetes |
| Non-Diabetic | Normal / Low risk |

---

# 🎯 Objective

The main goals of this project:

✅ Predict diabetes using medical input values  
✅ Understand and apply the KNN algorithm  
✅ Learn end-to-end ML workflow  
✅ Build a fully deployed ML-powered web app  
✅ Integrate frontend + backend using Flask  

---

# 🧠 Machine Learning Workflow

```text
Dataset (PIMA Diabetes)
        ↓
Data Cleaning & Scaling
        ↓
Feature Selection
        ↓
Train-Test Split
        ↓
KNN Classification Model
        ↓
Prediction
        ↓
Flask Deployment


📂 Project Structure
Diabetes-Prediction/
│
├── app.py
├── model.pkl
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
📁 File Explanation
File Name	Purpose
app.py	Flask backend + prediction logic
model.pkl	Trained KNN diabetes model
index.html	Frontend UI
style.css	UI styling
requirements.txt	Required dependencies
README.md	Project documentation
📊 Dataset Information

Dataset used:

PIMA Indian Diabetes Dataset

Attributes include:

Pregnancies
Glucose
Blood Pressure
Skin Thickness
Insulin
BMI
Diabetes Pedigree Function
Age

Example:

Feature	Value
Glucose	148
BMI	33.6
Pregnancies	2
Age	50
⚙ Technologies Used
Python
Flask
Scikit-learn
HTML5
CSS3
Pickle (Model Saving)
🔧 Installation & Setup
git clone https://github.com/your-username/diabetes-prediction-app.git
cd diabetes-prediction-app

Create a virtual environment (optional):

python -m venv venv

Activate:

Windows

venv\Scripts\activate

Mac/Linux

source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Run the app:

python app.py

App will run at:
👉 http://127.0.0.1:5000/

🌐 Web Interface

Includes:

Clean card-based UI
Smooth input boxes
Styled submit button
Instant prediction output

User enters medical data → clicks Predict → receives Diabetic / Non-Diabetic result.

🚀 Future Enhancements
Add Logistic Regression, SVM comparison
Add charts/graphs for better visualization
Deploy on Render / Railway / AWS
Add patient history storage
🤝 Contributing

Contributions and suggestions are welcome!
Feel free to open issues or submit pull requests.


---

If you want, I can also:

✅ :contentReference[oaicite:0]{index=0},  
✅ :contentReference[oaicite:1]{index=1},  
✅ :contentReference[oaicite:2]{index=2},  
✅ :contentReference[oaicite:3]{index=3},  
✅ Or :contentReference[oaicite:4]{index=4}.

