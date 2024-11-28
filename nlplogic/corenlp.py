from textblob import TextBlob
import wikipedia
import nltk

nltk.download("punkt_tab")


def search_wikipedia(name):
    """Search wikipedia for a page"""
    print(f"searching for {name}")
    return wikipedia.search(name)


def summarize_wikipedia(name, length=2):
    """Summarize wikipedia"""
    print(f"summary for name {name}")
    return wikipedia.summary(name, sentences=length)


def get_text_blob(text):
    blob = TextBlob(text)
    return blob


def get_phrases(name, length):
    """Find wikipedia name and return back phrases"""
    text = summarize_wikipedia(name, length)
    blob = get_text_blob(text)
    phrases = blob.noun_phrases

    return phrases


if __name__ == "__main__":
    print(get_phrases("Facebook", 3))
