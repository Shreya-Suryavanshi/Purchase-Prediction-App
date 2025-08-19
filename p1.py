import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
import pickle

# Load dataset
data = pd.read_csv("sna_aug25.csv")

# Encode Gender
data["Gender"] = LabelEncoder().fit_transform(data["Gender"])  # Male=1, Female=0

# Features and target
X = data[["User ID", "Gender", "Age", "EstimatedSalary"]]
y = data["Purchased"]

# Scale features
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# Choose k
k = int(len(data) ** 0.5)
if k % 2 == 0:
    k += 1

# Train KNN model
model = KNeighborsClassifier(n_neighbors=k, metric="euclidean")
model.fit(X_scaled, y)

# Save model and scaler
with open("knn_model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("scaler.pkl", "wb") as f:
    pickle.dump(scaler, f)