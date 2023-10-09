import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle  # Hem vektörleyici hem de modeller için
import streamlit as st
from PIL import Image
import requests
from io import BytesIO



# Stop words
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
nltk.download('wordnet')
nltk.download('punkt')

# En ustteki GIF icin;
st.image('https://media.tenor.com/B5qsCUFIXIwAAAAC/3ds-nintendo.gif', caption='Your Dream Clothes in Here!', width=500)


#Baslik ekliyoruz
st.markdown('<h2 style="font-size:1.5em;">Sentiment Analysis for Women Clothes Review</h2>', unsafe_allow_html=True)


# Side Bar
st.sidebar.title("Please Select a Method")
selected_model = st.sidebar.selectbox("Choose a Method", ['1.NaiveBayes', '2.LogisticRegression', '3.SVM', '4.KNN', '5.RandomForest', '6.AdaBoost'])

# Text Area
#user_input = st.text_area("Please enter a review without any punctual or number:")
#user_input = st.text_area("Please enter a review without any punctual or number:", height=10)
col1, col2 = st.columns(2)
with col1:
    user_input = st.text_area("Please enter a review without any punctual or number:", height=20)




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

# Load the selected model
try:
    model_filename = f"{selected_model}.pkl"
    with open(model_filename, 'rb') as f:
        model = pickle.load(f)
except FileNotFoundError:
    st.write(f"Model {model_filename} could not be found.")


# Submit Button
if st.button("Submit"):
    if user_input:
        st.write("Your review was received, and analysis began.")
        st.write("0: Positive review;  1: Negative review")
                
        # Kaydedilmiş vektörleyiciyi pickle ile yükle
        with open('tf_idf_vectorizer.pkl', 'rb') as f:
            loaded_vectorizer = pickle.load(f)
        
        # Yalnızca transform kullan
        user_input_tf_idf = loaded_vectorizer.transform([user_input])  # Note the list

        try:
                       
            result = model.predict(user_input_tf_idf)
            st.write("Result: ", result[0])
            
            if result==0:
                st.image('https://www.funimada.com/assets/images/cards/big/congrats-14.gif', caption='You are happy, then we are happy, too!', use_column_width=True) # Alkis eklemek icin
                st.balloons()
            else:
                # Uzgun GIF'i kullanmak icin;
                st.markdown("""
    <style>
    .container {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .gif {
        width: 200px;
        height: 200px;
    }
    </style>
    <div class="container">
        <img src="https://media1.giphy.com/media/9JLOGsEfPjpR1179HE/giphy.gif?cid=ecf05e47r98iy0koitbvmx08df4rt0e3ue2k6t3btrljvvrl&ep=v1_gifs_search&rid=giphy.gif&ct=g" class="gif"/>
    </div>
    """, unsafe_allow_html=True)                
                                              
                # Resmin altindaki yaziyi ortalamak icin
                st.markdown("""<style>.center-text {display: flex; justify-content: center; align-items: center; } </style> """, unsafe_allow_html=True)

                # Resmin altina gelen yazi
                st.markdown('<div class="center-text">We are very sad for hearing it.</div>', unsafe_allow_html=True)
                st.markdown('<div class="center-text">Please calm down!</div>', unsafe_allow_html=True)
                st.markdown('<div class="center-text">We will solve this problem ASAP.</div>', unsafe_allow_html=True)
                
                           

        except Exception as e:
            st.write(f"An error occurred: {e}")

    else:
        st.write("Please enter a valid review.")
