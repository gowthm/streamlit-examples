import streamlit as st
from textblob import TextBlob
import pandas as pd
import nltk
from textblob.download_corpora import download_all



try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt")

try:
    nltk.data.find("corpora/wordnet")
except LookupError:
    nltk.download("wordnet")

try:
    nltk.data.find("taggers/averaged_perceptron_tagger")
except LookupError:
    nltk.download("averaged_perceptron_tagger")

# Optional but recommended
try:
    nltk.data.find("corpora/brown")
except LookupError:
    nltk.download("brown")

# If TextBlob still complains
try:
    download_all()
except:
    pass

nltk.download("punkt")

st.title("📝 Text Analysis Notebook")

# ---------------------------
# Input Section
# ---------------------------
st.subheader("Enter Text")
text = st.text_area("Paste your text here", height=200)

uploaded_file = st.file_uploader("…or upload a .txt file", type=["txt"])

if uploaded_file:
    text = uploaded_file.read().decode("utf-8")

# Run analysis only when text exists
if text.strip():
    st.divider()

    # ---------------------------
    # Sentiment Analysis
    # ---------------------------
    st.subheader("📌 Sentiment Analysis")

    blob = TextBlob(text)
    sentiment = blob.sentiment

    st.write("Polarity:", sentiment.polarity)
    st.write("Subjectivity:", sentiment.subjectivity)

    # ---------------------------
    # Word Statistics
    # ---------------------------
    st.subheader("📊 Word Statistics")

    words = blob.words
    df_stats = pd.DataFrame({
        "Metric": ["Total Words", "Unique Words"],
        "Value": [len(words), len(set(words))]
    })

    st.table(df_stats)

    # ---------------------------
    # Keyword Extraction (simple frequency)
    # ---------------------------
    st.subheader("🔑 Keyword Extraction")

    freq = pd.Series(words).value_counts().head(10)
    st.bar_chart(freq)

    # ---------------------------
    # Sentence Breakdown
    # ---------------------------
    st.subheader("📘 Sentences")
    for i, sentence in enumerate(blob.sentences):
        st.write(f"**Sentence {i+1}:** {sentence}")
else:
    st.info("Enter text above to start analysis")
