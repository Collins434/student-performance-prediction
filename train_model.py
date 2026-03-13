
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import joblib

data = pd.read_csv("student_data.csv")

data["Internet_Access"] = data["Internet_Access"].map({"Yes":1,"No":0})
data["Study_Environment"] = data["Study_Environment"].map({"Poor":0,"Average":1,"Good":2})

X = data.drop("Final_Result", axis=1)
y = data["Final_Result"]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

model = LogisticRegression()
model.fit(X_train, y_train)

joblib.dump(model, "student_model.pkl")

print("Model trained and saved as student_model.pkl")
