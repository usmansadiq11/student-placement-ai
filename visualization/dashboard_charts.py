import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_cgpa_distribution(data):
    plt.figure(figsize=(10, 6))
    sns.histplot(data['CGPA'], bins=20, kde=True)
    plt.title('CGPA Distribution')
    plt.xlabel('CGPA')
    plt.ylabel('Frequency')
    plt.grid()
    plt.show()

def plot_skills_correlation(data):
    plt.figure(figsize=(12, 8))
    correlation_matrix = data.corr()
    sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', square=True)
    plt.title('Correlation Heatmap')
    plt.show()

def plot_placement_rate(data):
    placement_counts = data['Placed'].value_counts()
    plt.figure(figsize=(8, 5))
    sns.barplot(x=placement_counts.index, y=placement_counts.values, palette='viridis')
    plt.title('Placement Rate')
    plt.xlabel('Placed')
    plt.ylabel('Number of Students')
    plt.xticks(ticks=[0, 1], labels=['Not Placed', 'Placed'])
    plt.grid()
    plt.show()

def main():
    data = pd.read_csv('../dataset/placement_data.csv')
    plot_cgpa_distribution(data)
    plot_skills_correlation(data)
    plot_placement_rate(data)

if __name__ == "__main__":
    main()