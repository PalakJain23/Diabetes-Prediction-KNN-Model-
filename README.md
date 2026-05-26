🩺 Diabetes Prediction Web App (KNN Model)

A simple yet elegant Flask-based web application that predicts whether a patient is diabetic using the K-Nearest Neighbors (KNN) machine-learning algorithm.
The app takes medical inputs such as glucose level, BMI, insulin, age, etc., and returns a Diabetes / Non-Diabetic prediction.

✨ Features
✔️ Clean & classy UI
✔️ Machine Learning (KNN) model
✔️ Built using Flask
✔️ Easy form input for medical data
✔️ Real-time predictions
✔️ Custom CSS styling
📂 Project Structure
Diabetes-Prediction/
│
├── app.py
├── model.pkl
├── static/
│   └── style.css
├── templates/
│   └── index.html
├── README.md
└── requirements.txt
🔧 Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/diabetes-prediction-app.git
cd diabetes-prediction-app
2️⃣ Create Virtual Environment (optional)
python -m venv venv
source venv/bin/activate   # for Windows → venv\Scripts\activate
3️⃣ Install Required Libraries
pip install -r requirements.txt
4️⃣ Run the Application
python app.py

The app will run at:

http://127.0.0.1:5000/
🧠 Machine Learning Model (KNN)

The model is trained using the PIMA Indian Diabetes Dataset, containing features:

Pregnancies
Glucose
Blood Pressure
Skin Thickness
Insulin
BMI
Diabetes Pedigree Function
Age

After training, the model is saved as:

model.pkl

and loaded by Flask during prediction.

🌐 Web Interface

The interface contains:

Stylish card-based layout
Floating minimalistic input boxes
Glowing submit button
Instant prediction box

Users enter health metrics → click Predict → immediately see whether they are Diabetic or Non-Diabetic.


🚀 Future Enhancements
Add Logistic Regression or SVM model switch
Store prediction history
Add charts/graphs
Deploy on Render / Railway / AWS
🤝 Contributing

Pull requests and suggestions are always welcome.
Feel free to open an issue for improvements.
