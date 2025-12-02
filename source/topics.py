from gensim.corpora import Dictionary
from gensim.models import LdaModel

def build_dictionary_and_corpus(token_lists, no_below=50, no_above=0.5):
    dictionary = Dictionary(token_lists)
    dictionary.filter_extremes(no_below=no_below, no_above=no_above)
    corpus = [dictionary.doc2bow(doc) for doc in token_lists]
    return dictionary, corpus

def train_lda(corpus, dictionary, num_topics=8, passes=10, random_state=42):
    lda_model = LdaModel(
        corpus=corpus,
        id2word=dictionary,
        num_topics=num_topics,
        random_state=random_state,
        passes=passes,
        alpha="auto",
        eta="auto"
    )
    return lda_model

def print_topics(lda_model, num_topics=8, num_words=10):
    for idx, topic in lda_model.print_topics(num_topics=num_topics, num_words=num_words):
        print(f"Topic {idx}: {topic}")