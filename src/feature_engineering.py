import pandas as pd

def create_interaction_features(df):
    df['cgpa_internship'] = df['CGPA'] * df['Internship_Experience']
    df['cgpa_projects'] = df['CGPA'] * df['Projects_Completed']
    return df

def create_skill_level_features(df):
    df['programming_skill_level'] = df['Programming_Skills'].apply(lambda x: 1 if x >= 8 else (0.5 if x >= 5 else 0))
    return df

def feature_engineering(df):
    df = create_interaction_features(df)
    df = create_skill_level_features(df)
    return df

if __name__ == "__main__":
    # This file is intended to be imported as a module, so no execution code is included here.
    pass