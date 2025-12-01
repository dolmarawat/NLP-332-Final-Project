# NLP-332-Final-Project

This repository contains the code and artifacts for our IST 322: Introduction to NLP final project.

We analyze public posts and comments from Reddit communities such as r/Diamonds subreddit to understand how consumers talk about:

- Lab-grown vs. natural diamonds  
- Different jewelry product types (rings, earrings, necklaces, bracelets)  
- Occasion-based sentiment (proposals, weddings, anniversaries, birthdays)  
- Diamonds vs. gold in the context of price, ethics, and emotional value  

We use an end-to-end NLP pipeline:

1. **Corpus Creation** – Scraping posts & top-level comments from Reddit  
2. **Preprocessing** – Cleaning, tokenization, lemmatization, bigrams  
3. **Exploratory Data Analysis** – Corpus stats, token distributions  
4. **Sentiment Analysis** – Using VADER on Reddit text  
5. **Topic Modeling** – LDA on bigram-enriched tokens  
6. **Supervised Learning** – Classifier to distinguish lab-grown vs natural diamond discussions  

---

## Repository Structure

```text
.
├── README.md
├── requirements.txt
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   ├── 01_data_collection.ipynb
│   ├── 02_preprocessing_eda.ipynb
│   └── 03_modeling.ipynb
└── src/
    ├── __init__.py
    ├── config.py
    ├── reddit_scraper.py
    ├── preprocessing.py
    ├── sentiment.py
    ├── topics.py
    └── supervised.py

```

## Notes for working on this project:

1. Pull all the recent changes to the github to your repo in the VSCODE: 

2. Make changes/updates to the code and make sure two people are not pushing the updates at the same time. 

3. Once done with your part, push the code to main branch > feel free to notify others.