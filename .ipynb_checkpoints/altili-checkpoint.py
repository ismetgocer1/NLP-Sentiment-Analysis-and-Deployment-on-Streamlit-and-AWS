{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "02a80f7e-d5fa-4045-acaf-73db74ca2793",
   "metadata": {},
   "outputs": [],
   "source": [
    "from nltk.tokenize import word_tokenize\n",
    "from nltk.corpus import stopwords\n",
    "from nltk.stem import WordNetLemmatizer\n",
    "from sklearn.feature_extraction.text import TfidfVectorizer\n",
    "import pickle\n",
    "import streamlit as st\n",
    "\n",
    "# Initialize Stop words\n",
    "stop_words = set(stopwords.words('english'))\n",
    "\n",
    "# Streamlit App\n",
    "st.header(\"Sentiment Analysis for Women Clothes Review\")\n",
    "\n",
    "# Side Bar\n",
    "st.sidebar.title(\"Please Select a Method\")\n",
    "selected_model = st.sidebar.selectbox(\"Choose a Method\", ['NaiveBayes', 'LogisticRegression', 'SVM', 'KNN', 'RandomForest', 'AdaBoost'])\n",
    "\n",
    "# Text Area\n",
    "user_input = st.text_area(\"Please enter a review without any punctual or number:\")\n",
    "\n",
    "# Data Cleaning Function\n",
    "def cleaning(data):\n",
    "    text_tokens = word_tokenize(data.lower())\n",
    "    tokens_without_punc = [w for w in text_tokens if w.isalpha()]\n",
    "    tokens_without_sw = [t for t in tokens_without_punc if t not in stop_words]\n",
    "    text_cleaned = [WordNetLemmatizer().lemmatize(t) for t in tokens_without_sw]\n",
    "    return \" \".join(text_cleaned)\n",
    "\n",
    "# Load the selected model\n",
    "try:\n",
    "    model_filename = f\"{selected_model}.pkl\"\n",
    "    with open(model_filename, 'rb') as f:\n",
    "        model = pickle.load(f)\n",
    "except FileNotFoundError:\n",
    "    st.write(f\"Model {model_filename} could not be found.\")\n",
    "\n",
    "# Submit Button\n",
    "if st.button(\"Submit\"):\n",
    "    if user_input:\n",
    "        st.write(\"Your review was received, and analysis began.\")\n",
    "        \n",
    "        try:\n",
    "            with open('tf_idf_vectorizer.pkl', 'rb') as f:\n",
    "                loaded_vectorizer = pickle.load(f)\n",
    "                \n",
    "            user_input_tf_idf = loaded_vectorizer.transform([cleaning(user_input)])\n",
    "            \n",
    "            try:\n",
    "                result = model.predict(user_input_tf_idf)\n",
    "                st.write(\"Result: \", result[0])\n",
    "            except Exception as e:\n",
    "                st.write(f\"An error occurred during prediction: {e}\")\n",
    "        except FileNotFoundError:\n",
    "            st.write(\"tf_idf_vectorizer.pkl file could not be found.\")\n",
    "    else:\n",
    "        st.write(\"Please enter a valid review.\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
