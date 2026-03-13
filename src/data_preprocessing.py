import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder

def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

def clean_data(data):
    # Handle missing values
    data.fillna(data.mean(), inplace=True)
    return data

def encode_categorical(data, categorical_features):
    label_encoders = {}
    for feature in categorical_features:
        le = LabelEncoder()
        data[feature] = le.fit_transform(data[feature])
        label_encoders[feature] = le
    return data, label_encoders

def normalize_data(data, numerical_features):
    scaler = StandardScaler()
    data[numerical_features] = scaler.fit_transform(data[numerical_features])
    return data, scaler

def preprocess_data(file_path, categorical_features, numerical_features):
    data = load_data(file_path)
    data = clean_data(data)
    data, label_encoders = encode_categorical(data, categorical_features)
    data, scaler = normalize_data(data, numerical_features)
    return data, label_encoders, scaler

if __name__ == "__main__":
    file_path = '../dataset/placement_data.csv'
    categorical_features = ['programming_skills', 'internship_experience', 'communication_skills']
    numerical_features = ['CGPA', 'attendance', 'projects_completed', 'backlogs']
    
    processed_data, label_encoders, scaler = preprocess_data(file_path, categorical_features, numerical_features)
    print(processed_data.head())