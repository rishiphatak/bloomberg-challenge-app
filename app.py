import streamlit as st
from joblib import load
from time import sleep
import json
import requests
import numpy as np

def get_embedding(text, api_key):
    ## API Definitions
    url = "https://datathon.bindgapi.com/channel"
    headers =  {
        "X-API-Key": api_key,
        "Content-Type":"application/json"
    }
    body = { "inputs": text }
    ## API Call
    try:
        response = requests.post(url, data=json.dumps(body), headers=headers)
    except Exception:
        print("Encountered exception")
        
    try:
        # return response 
        result = response.json()
        return json.loads(result['results'])
    except:
        print("Exception again!")

def my_embedding(text):
    sleep(1)
    return get_embedding(text, "RMEtdXzF641ECEIQpFeAU2ZVgbg8CbCe8sLYL9X5")

st. title("News article classification with Bloomberg!")

clf = load('classifier_2.joblib') 

categories = [
    'COMEDY', 'WORLD NEWS', 'CULTURE & ARTS', 'TECH', 'SPORTS', 'ENTERTAINMENT', 'POLITICS'
]

description = st.text_area('Description')

# Every form must have a submit button.
submitted = st.button("Submit")

if submitted:
    embedding = my_embedding(description)
    if embedding is None:
        st.write('API is down')
    st.write("### " + categories[clf.predict(np.array([embedding]).reshape(1, -1))[0]])
