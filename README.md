# 🛒 Purchase Prediction App  

## 📌 **Overview**  
The **Purchase Prediction App** is a machine learning-based solution that predicts whether a user will purchase a product after seeing an advertisement on a social networking platform (like **Facebook, Instagram, or LinkedIn**).  

This app uses **demographic data** (Age, Gender, Salary) to identify purchase behavior, helping businesses **target ads effectively** and **optimize ad spending**.  

---

## 📝 **Problem Statement**  
- You are given a dataset of users with demographic information.  
- The task is to **predict whether a user will purchase** after seeing an advertisement.  
- Prediction is based on **Age** and **Estimated Salary**.  

---

## 📊 **Dataset Details**  
The dataset contains **5 columns**:  

- **UserID** → Unique identifier for each user  
- **Gender** → Male / Female  
- **Age** → Age of the user  
- **EstimatedSalary** → Estimated salary of the user  
- **Purchased** → Target (0 = Not Purchased, 1 = Purchased)  

### 🔎 Example Data:  
| UserID   | Gender | Age | EstimatedSalary | Purchased |
|----------|--------|-----|-----------------|-----------|
| 15624510 | Male   | 19  | 19000           | 0         |
| 15810944 | Male   | 35  | 20000           | 1         |
| 15668575 | Female | 26  | 43000           | 1         |
| 15603246 | Female | 27  | 57000           | 0         |
| 15840002 | Male   | 19  | 76000           | 0         |

---

## ⚙️ **Use Cases**  
Companies and ad platforms can use this model to:  

- 🎯 **Target Ads** → Show ads to users most likely to purchase  
- 💰 **Optimize Ad Spending** → Avoid uninterested users  
- 📈 **Audience Segmentation** → Group users by predicted buying behavior  

---

## 🛠️ **Tech Stack**  
- **Language**: Python 🐍  
- **Libraries**:  
  - `pandas` → Data manipulation  
  - `numpy` → Numerical operations  
  - `matplotlib`, `seaborn` → Visualization  
  - `scikit-learn` → Machine Learning (**KNN, Logistic Regression, Decision Tree**)  

---

## 🚀 **Features**  
✔️ Preprocess demographic data  
✔️ Train ML models (**KNN implemented**)  
✔️ Predict purchase likelihood  
✔️ Visualize KNN decision boundaries  
✔️ Export predictions  

---

## 📂 **Project Structure**  
