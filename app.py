from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load model and scaler
with open("knn_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

@app.route('/')
def home():
    return render_template("home.html", prediction=None)

@app.route('/predict', methods=['POST'])
def predict():
    user_id = int(request.form['user_id'])
    gender = request.form['gender']
    age = int(request.form['age'])
    salary = int(request.form['salary'])

    gender_encoded = 1 if gender.lower() == "male" else 0
    input_df = pd.DataFrame([[user_id, gender_encoded, age, salary]],
                            columns=["User ID", "Gender", "Age", "EstimatedSalary"])

    scaled_input = scaler.transform(input_df)
    result = model.predict(scaled_input)[0]
    prediction = "Purchased ✅" if result == 1 else "Not Purchased ❌"

    return render_template("home.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)