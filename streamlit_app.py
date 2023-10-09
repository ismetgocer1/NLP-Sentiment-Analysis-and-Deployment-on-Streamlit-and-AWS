import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import streamlit as st
import os

nltk.data.path.append(os.path.join(os.path.dirname(__file__), "nltk_data"))

# Download necessary NLTK data if not present
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    stop_words = set(stopwords.words('english'))
except LookupError:
    nltk.download('stopwords')
    stop_words = set(stopwords.words('english'))

# Streamlit UI
st.image('https://media.tenor.com/B5qsCUFIXIwAAAAC/3ds-nintendo.gif', caption='Your Dream Clothes in Here!', use_column_width=True)
st.markdown('<h2 style="font-size:1.5em;">Sentiment Analysis for Women Clothes Review</h2>', unsafe_allow_html=True)

# Sidebar
st.sidebar.title("Please Select a Method")
selected_model = st.sidebar.selectbox("Choose a Method", ['1.NaiveBayes', '2.LogisticRegression', '3.SVM', '4.KNN', '5.RandomForest', '6.AdaBoost'])
user_input = st.text_area("Please enter a review without any punctual or number:")

# Data Cleaning
def cleaning(data):
    text_tokens = word_tokenize(data.lower())
    tokens_without_punc = [w for w in text_tokens if w.isalpha()]
    tokens_without_sw = [t for t in tokens_without_punc if t not in stop_words]
    text_cleaned = [WordNetLemmatizer().lemmatize(t) for t in tokens_without_sw]
    return " ".join(text_cleaned)

# Load model
try:
    with open(f"{selected_model}.pkl", 'rb') as f:
        model = pickle.load(f)
except FileNotFoundError:
    st.write(f"Model {selected_model}.pkl could not be found.")

# Submit Button
if st.button("Submit"):
    if user_input:
        st.write("Your review was received, and analysis began.")
        st.write("0: Positive review.")
        st.write("1: Negative review.")
        
        try:
            with open('tf_idf_vectorizer.pkl', 'rb') as f:
                loaded_vectorizer = pickle.load(f)
            user_input_tf_idf = loaded_vectorizer.transform([cleaning(user_input)])
            
            result = model.predict(user_input_tf_idf)
            st.write("Result: ", result[0])
            # ... (the rest of your code)
        except FileNotFoundError:
            st.write("TF-IDF vectorizer file could not be found.")
        except Exception as e:
            st.write(f"An error occurred: {e}")
    else:
        st.write("Please enter a valid review.")
