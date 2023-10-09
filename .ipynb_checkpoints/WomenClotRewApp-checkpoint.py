from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle  # Hem vektörleyici hem de modeller için
import streamlit as st

# Stop words
stop_words = set(stopwords.words('english'))

st.header("Sentiment Analysis for Women Clothes Review")

# Side Bar
st.sidebar.title("Please Select a Method")
selected_model = st.sidebar.selectbox("Choose a Method", ['NaiveBayes', 'LogisticRegression', 'SVM', 'KNN', 'RandomForest', 'AdaBoost'])

# Text Area
user_input = st.text_area("Please enter a review without any punctual or number:")

# Data Cleaning
def cleaning(data):
    # Tokenize
    text_tokens = word_tokenize(data.lower())
    
    # Remove Puncs and numbers
    tokens_without_punc = [w for w in text_tokens if w.isalpha()]
    
    # Remove Stopwords
    tokens_without_sw = [t for t in tokens_without_punc if t not in stop_words]
    
    # Lemmatization
    text_cleaned = [WordNetLemmatizer().lemmatize(t) for t in tokens_without_sw]
    
    # Joining
    return " ".join(text_cleaned)

# Submit Button
if st.button("Submit"):
    if user_input:
        st.write("Your review was received, and analysis began.")
        
        # Kaydedilmiş vektörleyiciyi pickle ile yükle
        with open('tf_idf_vectorizer.pkl', 'rb') as f:
            loaded_vectorizer = pickle.load(f)
        
        # Yalnızca transform kullan
        user_input_tf_idf = loaded_vectorizer.transform([user_input])  # Note the list

        try:
            # Modeli pickle ile yükle
            with open('1.NaiveBayes.pkl', 'rb') as f:
                model = pickle.load(f)

            result = model.predict(user_input_tf_idf)
            st.write("Result: ", result[0])

        except Exception as e:
            st.write(f"An error occurred: {e}")

    else:
        st.write("Please enter a valid review.")
