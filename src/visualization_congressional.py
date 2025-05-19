
# visualization.py
# Author: Yetta

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_statements_over_time(df):
    """Plot the number of statements over time."""
    plt.figure(figsize=(8, 5))
    df['Date'] = pd.to_datetime(df['Date'])
    df.groupby(df['Date'].dt.to_period('M')).size().plot(kind='bar', color='skyblue')
    plt.title('Number of Statements Over Time')
    plt.xlabel('Month')
    plt.ylabel('Number of Statements')
    plt.xticks(rotation=45)
    plt.show()

def plot_speaker_distribution(df):
    """Plot the distribution of statements by speaker."""
    plt.figure(figsize=(6, 4))
    sns.countplot(y='Speaker', data=df, palette='Set2')
    plt.title('Statement Distribution by Speaker')
    plt.show()

if __name__ == "__main__":
    df = pd.read_csv('../data/mock_congressional_data.csv')
    plot_statements_over_time(df)
    plot_speaker_distribution(df)
