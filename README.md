## NLP 332 Final Project: Analyzing AI-Related Job Anxiety & Future Optimism on Reddit
This repository contains the full workflow, data preparation, exploratory analysis, sentiment modeling, and topic modeling for the project:

### Final Report:
Analyzing AI-Related Job Anxiety and Future Optimism on Reddit
(see: /reports/final_report.pdf)
### Notebook:
All steps from corpus creation → preprocessing → EDA → LSA topic modeling → sentiment analysis
(see: /notebooks/final_notebook.ipynb)

### Project Overview
This project analyzes 10,000 Reddit posts discussing AI, automation, career changes, layoffs, and future optimism. 
##### The main goals:
- Identify linguistic patterns in AI-related job anxiety
- Compare career-fear vs. future-hope communities
- Model sentiment polarity & subjectivity
- Extract dominant themes using LSA topic modeling
- Build interpretable NLP pipelines for downstream tasks

# Repository Structure
data/              # raw + cleaned dataset
notebooks/         # Colab/ Jupyter files
src/               # Python modules for preprocessing, EDA, models
reports/           # Milestone + Final Report

#### Key Features
1. Corpus Creation
10,000 Reddit posts balanced between 2 labels: CAREER_ANXIETY, FUTURE_HYPE
2. Text Preprocessing Pipeline
- Contraction expansion
- Tokenization
- Lemmatization (spaCy)
- Stemming (Snowball)
- Normalization & Reddit-artifact cleaning
- Lexical diversity computation
- Vocabulary reduction
3. Exploratory Data Analysis
Frequency distributions
Zipf-like token distribution
Review length statistics by label
Context windows ("AI", "job", "scared")
Concordance plots
4. Sentiment Modeling
TextBlob Polarity + Subjectivity
VADER compound scores
5. Topic Modeling
LSA (TruncatedSVD)
Coherence evaluation
Top-word visualization

#### Installation
pip install -r requirements.txt
▶️ Running the Pipeline
python src/preprocessing.py
python src/eda.py
python src/sentiment.py
python src/topic_modeling.py

##### Authors
Dolma Rawat 
Rohini Vishwanathan 
Yashas Basavaraju Mahesh
Aashish Sunar 
Course: IST 332 — Natural Language Processing



