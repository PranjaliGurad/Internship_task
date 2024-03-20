import streamlit as st
import spacy
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
# from cleaning import data

# df = data

# Load the pre-trained spaCy model
nlp = spacy.load("en_core_web_md")

def calculate_similarity(text1, text2):
    # Process the text with spaCy
    doc1 = nlp(text1)
    doc2 = nlp(text2)
    
    # Calculate the average word embeddings for each document
    avg_vector1 = doc1.vector
    avg_vector2 = doc2.vector
    
    # Compute the cosine similarity between the vectors
    similarity_score = cosine_similarity([avg_vector1], [avg_vector2])[0][0]
    
    return similarity_score

# Streamlit UI
st.title('Text Similarity Scorer')

text1 = st.text_area('Enter Text 1', '')
text2 = st.text_area('Enter Text 2', '')

if st.button('Calculate Similarity'):
    if text1 and text2:
        similarity_score = calculate_similarity(text1, text2)
        st.write('Similarity Score:', similarity_score)
    else:
        st.write('Please enter both text inputs.')
