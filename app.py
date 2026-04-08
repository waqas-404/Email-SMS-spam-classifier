import streamlit as st
import pandas as pd
import numpy as np
import pickle
import cloudpickle
from utils import transform_text

transform_text = pickle.load(open('transform_text.pkl','rb'))
# with open('transform_text.pkl', 'rb') as f:
#     transform_text = cloudpickle.load(f)
tfidf = pickle.load(open('vectorizer.pkl','rb'))
model= pickle.load(open('model.pkl','rb'))

st.title("Email/SMS Spam Classifier")

input_text = st.text_area("Enter your message:")

if st.button('Predict'):
    transformed_text = transform_text(input_text)

    transformed_text_v = tfidf.transform([transformed_text])

    probs = model.predict_proba(transformed_text_v)[:,1]
    result = (probs > 0.3).astype(int)
    if result == 1:
        st.header('Spam')
    else:
        st.header("Not Spam")
