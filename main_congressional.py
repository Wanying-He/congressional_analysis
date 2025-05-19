
# main.py
# Author: Yetta

from data_scraping import load_data
from nlp_analysis import topic_modeling
from visualization import plot_statements_over_time, plot_speaker_distribution

# Step 1: Load Data
print("[INFO] Loading data...")
df = load_data('./mock_congressional_data.csv')

# Step 2: Perform NLP Analysis
print("[INFO] Performing topic modeling...")
lda_model, vectorizer = topic_modeling(df)

# Step 3: Visualize Results
print("[INFO] Generating visualizations...")
plot_statements_over_time(df)
plot_speaker_distribution(df)

print("[INFO] Analysis complete.")
