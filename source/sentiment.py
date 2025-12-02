import numpy as np
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def compute_vader_scores(text: str):
    if not isinstance(text, str) or len(text.strip()) == 0:
        return None
    return analyzer.polarity_scores(text)

def add_sentiment(df: pd.DataFrame, text_col: str = "text"):
    df = df.copy()
    scores = df[text_col].apply(compute_vader_scores)
    df["sent_compound"] = scores.apply(lambda x: x["compound"] if x else np.nan)
    df["sent_label"] = df["sent_compound"].apply(
        lambda c: "pos" if c >= 0.05 else ("neg" if c <= -0.05 else "neu")
    )
    return df

def add_material_label(df: pd.DataFrame, text_col: str = "text_clean_basic"):
    df = df.copy()

    def has_lab(text):
        text = text.lower()
        return int("lab grown" in text or "lab-grown" in text or "labgrown" in text)

    def has_nat(text):
        text = text.lower()
        return int("natural diamond" in text or "natural stones" in text)

    lab = df[text_col].apply(has_lab)
    nat = df[text_col].apply(has_nat)

    df["label_material"] = "other"
    df.loc[lab == 1, "label_material"] = "lab_grown"
    df.loc[(lab == 0) & (nat == 1), "label_material"] = "natural"

    return df