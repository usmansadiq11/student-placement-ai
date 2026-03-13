from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

# allow frontend connection
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# load trained model
model = joblib.load("../model/placement_model.pkl")


class StudentData(BaseModel):
    CGPA: float
    Programming_Skills: int
    Internship_Experience: int
    Communication_Skills: int
    Projects_Completed: int
    Attendance: int
    Backlogs: int


@app.post("/predict")
def predict(data: StudentData):

    features = np.array([[
        data.CGPA,
        data.Programming_Skills,
        data.Internship_Experience,
        data.Communication_Skills,
        data.Projects_Completed,
        data.Attendance,
        data.Backlogs
    ]])

    prediction = model.predict(features)[0]
    probability = int(model.predict_proba(features)[0][1] * 100)

    prediction_label = "Placed" if prediction == 1 else "Not Placed"

    # -------- AI Analysis -------- #

    strong = []
    weak = []
    suggestions = []

    if data.CGPA >= 8:
        strong.append("High CGPA")
    else:
        weak.append("Low CGPA")
        suggestions.append("Improve academic performance")

    if data.Programming_Skills >= 7:
        strong.append("Strong Programming Skills")
    else:
        weak.append("Weak Programming Skills")
        suggestions.append("Practice coding / DSA")

    if data.Projects_Completed >= 3:
        strong.append("Good Project Experience")
    else:
        weak.append("Few Projects")
        suggestions.append("Build more practical projects")

    if data.Communication_Skills >= 7:
        strong.append("Good Communication Skills")
    else:
        weak.append("Weak Communication")
        suggestions.append("Improve presentation & communication")

    if data.Attendance >= 75:
        strong.append("Good Attendance")
    else:
        weak.append("Low Attendance")

    if data.Backlogs > 0:
        weak.append("Existing Backlogs")
        suggestions.append("Clear academic backlogs")

    return {
        "prediction": prediction_label,
        "probability": probability,
        "strong_points": strong[:2],
        "weak_points": weak[:2],
        "suggestions": suggestions[:2]
    }