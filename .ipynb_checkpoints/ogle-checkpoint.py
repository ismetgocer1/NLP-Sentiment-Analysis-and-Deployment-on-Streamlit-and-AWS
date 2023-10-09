{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e9fc2a17-4856-4aae-87c5-0950e01099fc",
   "metadata": {},
   "outputs": [],
   "source": [
    "from joblib import load\n",
    "from sklearn.pipeline import Pipeline\n",
    "from sklearn.feature_extraction.text import TfidfVectorizer\n",
    "import streamlit as st\n",
    "import pandas as pd\n",
    "\n",
    "# Assuming that X, y are already defined somewhere if you need them\n",
    "\n",
    "# Load the pre-trained model\n",
    "log_model = load('2.LogisticRegression.joblib')\n",
    "\n",
    "# Create pipeline\n",
    "pipe = Pipeline([\n",
    "    ('tfidf', TfidfVectorizer(min_df=3)),\n",
    "    ('log', log_model)\n",
    "])\n",
    "\n",
    "# Streamlit app\n",
    "user_input = st.text_area(\"Please enter a review without any punctuation or number:\")\n",
    "\n",
    "if st.button(\"Submit\"):\n",
    "    if user_input:\n",
    "        st.write(\"Your review was received, and analysis begins.\")\n",
    "        \n",
    "        # You typically don't fit the pipeline here if you are using a pre-trained model\n",
    "        # pipe.fit(X, y)\n",
    "        \n",
    "        review = pd.Series(user_input)\n",
    "        prediction = pipe.predict(review)\n",
    "        \n",
    "        st.write(f\"Prediction: {prediction}\")\n"
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
