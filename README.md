## IST 332 NLP Final Project: AI Job Anxiety & Future Optimism on Reddit

This repository contains an end-to-end NLP pipeline to study how people discuss AI and work on Reddit, focusing on **emotional orientation** (Career Anxiety vs. Future Hype/Optimism vs. Uncertainty).  

**Final report:** `reports/final_report.pdf`  
**Main notebook:** `notebooks/final_notebook.ipynb`  

---

## Project overview
We analyze a Reddit corpus of ~10,000 posts/comments about AI, automation, layoffs, job search, career transitions, and future-of-work narratives.  

### Objectives
- Quantify and compare emotional orientations toward AI and work (Career Anxiety / Future Hype / Uncertainty).
- Run sentiment analysis to measure polarity and intensity at scale.
- Extract themes using topic modeling (classical + embedding-based).
- Train supervised models to predict emotional category from text.

---

## Methods implemented
### 1) Corpus creation
- Collected public Reddit posts + comments from AI- and career-focused subreddits.
- Stored data as a structured CSV (text + label + type).

### 2) Text preprocessing
Typical steps used in the pipeline include:
- Contraction expansion, lowercasing, punctuation/digit cleanup
- Tokenization, stopword filtering (+ Reddit artifact cleanup)
- Lemmatization + stemming for normalized representations
- Cleaned text field used downstream for EDA/modeling

### 3) Sentiment analysis
- VADER sentiment scoring (compound score as a main polarity signal)
- Complementary polarity/subjectivity checks (optional)

### 4) Topic modeling & semantic structure
Multiple approaches are used to compare interpretability vs. semantic depth:
- LDA topic modeling (with coherence-based selection of topic count)
- NMF topic modeling (TF–IDF-based, strong interpretability)
- Word embedding clustering: Word2Vec, FastText, GloVe (KMeans + 2D visualization)
- Sentence embeddings: BERT + 2D projection (e.g., UMAP) for post-level semantic clustering

### 5) Supervised learning (multi-class)
We frame prediction as:  
`0 = Career Anxiety`, `1 = Future Hype/Optimism`, `2 = Uncertainty`  

Models evaluated on TF–IDF features:
- Logistic Regression
- Linear SVM (best overall)
- Multinomial Naive Bayes
- Random Forest


---

## Results (high-level)
- The three emotional orientations (Anxiety / Hype / Uncertainty) show consistent linguistic + thematic differences.
- Linear models perform best on sparse TF–IDF, with **Linear SVM** providing the strongest overall balance of performance among tested models.

> Add your final metrics here if you want:
> - Best model: Linear SVM  
> - Accuracy: <...>  
> - Weighted F1: <...>

---

## Installation

pip install -r requirements.txt

---

python src/preprocessing.py
python src/eda.py
python src/sentiment.py
python src/topic_modeling.py
python src/supervised_learning.p

---

## Deployment idea (from project plan)
A lightweight real-world version of this system could include:
- Scheduled ingestion of new posts (API/scrape).
- Automated preprocessing + sentiment/topic inference + emotional classification.
- Storage of outputs for time-series monitoring.
- A dashboard (e.g., Streamlit/Dash/Power BI) with trend lines + alerts.
- Periodic retraining + drift monitoring + a small human audit loop. [file:13]

---

## Ethics & data usage
This project uses public online text. Use the data responsibly:
- Avoid deanonymization and do not publish sensitive raw text.
- Follow platform rules and rate limits for collection.

---

## Authors
- Dolma Rawat
- Rohini Vishwanathan
- Yashas Basavaraju Mahesh
- Aashish Sunar

Course: IST 332 — Natural Language Processing

