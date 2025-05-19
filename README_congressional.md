
# Congressional NLP Analysis

## Project Overview
This project focuses on analyzing US Congressional statements related to foreign policy and political stance. The project includes data simulation (mock scraping), NLP-based topic modeling (LDA), sentiment analysis, and visualization of sentiment trends over time.

## Project Structure
```
congressional_nlp_analysis/
│
├── README.md                    # Project description and usage
├── requirements.txt             # Dependencies for Python environment
├── data/                        # Placeholder for raw and processed data
│   └── mock_congressional_data.csv
│
├── src/                         # Source code
│   ├── data_scraping.py         # Mock data scraping logic
│   ├── nlp_analysis.py          # Topic modeling and sentiment analysis
│   └── visualization.py         # Plot generation and visualization
│
└── main.py                      # Main script to execute the analysis pipeline
```

## Installation
```
pip install -r requirements.txt
```

## Usage
To run the full analysis pipeline:
```
python main.py
```

## Data Description
The project uses mock congressional statement data with the following columns:
- Statement: The speech or legislative statement content.
- Date: Date of the statement.
- Speaker: The speaker or representative.

## Analysis Steps
1. **Data Scraping and Preprocessing**
2. **Topic Modeling (LDA)**
3. **Sentiment Analysis**
4. **Visualization of Trends**

## Results
- Identified key policy topics in congressional statements.
- Analyzed sentiment shifts over time.

## License
MIT License
