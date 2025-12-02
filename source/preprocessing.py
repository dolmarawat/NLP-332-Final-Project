import re
import pandas as pd
import numpy as np
import nltk
import spacy
from nltk.corpus import stopwords
from gensim.models import Phrases
from gensim.models.phrases import Phraser

# Make sure these are downloaded in the environment
# nltk.download('stopwords')
# python -m spacy download en_core_web_sm

nlp = spacy.load("en_core_web_sm")
stop_words = set(stopwords.words("english"))

def basic_clean(text: str) -> str:
    if pd.isna(text):
        return ""
    text = text.lower()
    text = re.sub(r"http\S+|www\.\S+", " ", text)          # URLs
    text = re.sub(r"[^a-z0-9\s]", " ", text)              # keep alphanum
    text = re.sub(r"\s+", " ", text).strip()
    return text

def spacy_lemmatize(text: str):
    doc = nlp(text)
    tokens = []
    for token in doc:
        if token.is_stop or token.is_punct or token.like_num:
            continue
        if token.pos_ not in {"NOUN", "VERB", "ADJ", "ADV"}:
            continue
        lemma = token.lemma_.strip()
        if lemma and lemma not in stop_words and len(lemma) > 2:
            tokens.append(lemma)
    return tokens

def add_clean_and_tokens(df: pd.DataFrame, text_col: str = "text") -> pd.DataFrame:
    df = df.copy()
    df["text_clean_basic"] = df[text_col].apply(basic_clean)
    df["tokens"] = df["text_clean_basic"].apply(spacy_lemmatize)
    return df

def add_bigrams(df: pd.DataFrame, min_count=20, threshold=10):
    phrases = Phrases(df["tokens"], min_count=min_count, threshold=threshold)
    bigram = Phraser(phrases)
    df["tokens_bigram"] = df["tokens"].apply(lambda x: bigram[x])
    df["clean_joined"] = df["tokens_bigram"].apply(lambda toks: " ".join(toks))
    return df

def corpus_stats(df: pd.DataFrame):
    df = df.copy()
    df["length_tokens"] = df["tokens"].apply(len)
    num_docs = len(df)
    avg_len = df["length_tokens"].mean()
    max_len = df["length_tokens"].max()

    all_tokens = [t for doc in df["tokens"] for t in doc]
    vocab_size = len(set(all_tokens))

    return {
        "num_docs": num_docs,
        "avg_length_tokens": avg_len,
        "max_length_tokens": max_len,
        "vocab_size": vocab_size
    }