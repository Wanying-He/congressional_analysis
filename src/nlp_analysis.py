
# nlp_analysis.py
# Author: Yetta

import pandas as pd
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

def preprocess(text):
    """Tokenize and clean the text."""
    tokens = word_tokenize(text.lower())
    return ' '.join(tokens)

def topic_modeling(df, n_topics=2):
    """Perform LDA topic modeling on the statements."""
    print("[INFO] Preprocessing data...")
    df['Processed'] = df['Statement'].apply(preprocess)

    print("[INFO] Vectorizing text...")
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(df['Processed'])

    print("[INFO] Performing LDA...")
    lda = LatentDirichletAllocation(n_components=n_topics, random_state=42)
    lda.fit(X)

    print("[INFO] Topics identified:")
    for idx, topic in enumerate(lda.components_):
        print(f"Topic {idx}: ", [vectorizer.get_feature_names_out()[i] for i in topic.argsort()[-5:]])
    
    return lda, vectorizer

if __name__ == "__main__":
    df = pd.read_csv('../data/mock_congressional_data.csv')

    lda_model, vectorizer = topic_modeling(df)
