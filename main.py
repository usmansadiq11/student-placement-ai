import pandas as pd
from src.data_preprocessing import preprocess_data
from src.feature_engineering import create_features
from src.train_model import train_model
from src.evaluate_model import evaluate_model
from src.predict import make_prediction

def main():
    # Load dataset
    data = pd.read_csv('dataset/placement_data.csv')
    
    # Preprocess data
    processed_data = preprocess_data(data)
    
    # Create features
    features = create_features(processed_data)
    
    # Train model
    model = train_model(features)
    
    # Evaluate model
    evaluate_model(model, features)
    
    # Example prediction (replace with actual input data)
    sample_student_data = {
        'CGPA': 8.5,
        'Programming Skills': 4,
        'Internship Experience': 1,
        'Communication Skills': 4,
        'Projects Completed': 3,
        'Attendance': 90,
        'Backlogs': 0
    }
    
    prediction = make_prediction(model, sample_student_data)
    print(f'Prediction for the sample student: {"Placed" if prediction else "Not Placed"}')

if __name__ == "__main__":
    main()