import pickle
import pandas as pd

# Load model and scaler
with open("knn_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

# Input
user_id = int(input("Enter User ID: "))
gender = input("Enter Gender (Male/Female): ")
age = int(input("Enter Age: "))
salary = int(input("Enter Estimated Salary: "))

gender_encoded = 1 if gender.lower() == "male" else 0
input_df = pd.DataFrame([[user_id, gender_encoded, age, salary]],
                        columns=["User ID", "Gender", "Age", "EstimatedSalary"])

# Scale input
scaled_input = scaler.transform(input_df)

# Predict
prediction = model.predict(scaled_input)[0]
print("Prediction:", "Purchased ✅" if prediction == 1 else "Not Purchased ❌")