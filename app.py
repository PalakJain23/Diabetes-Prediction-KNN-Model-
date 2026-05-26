from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load files
model = pickle.load(open("knn_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    values = [
        float(request.form['pregnancies']),
        float(request.form['glucose']),
        float(request.form['bloodpressure']),
        float(request.form['skin']),
        float(request.form['insulin']),
        float(request.form['bmi']),
        float(request.form['dpf']),
        float(request.form['age'])
    ]

    # Convert & scale
    final_data = scaler.transform(np.array([values]))

    # Predict
    pred = model.predict(final_data)[0]
    result = "Diabetic" if pred == 1 else "Not Diabetic"

    return render_template("index.html", prediction_text=f"Result: {result}")

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)