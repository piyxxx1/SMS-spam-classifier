import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()


def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))

st.markdown("""
    <style>
    .title {
        font-size: 50px;
        font-weight: bold;
        color: white;
        background: linear-gradient(90deg, #ff6a00, #ee0979);
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    </style>
    <div class="title">Email & SMS Spam Classifier </div>
""", unsafe_allow_html=True)

input_sms = st.text_area("Enter the message")
nltk.download('punkt_tab')
if st.button('Predict'):

    # 1. preprocess
    transformed_sms = transform_text(input_sms)
    # 2. vectorize
    vector_input = tfidf.transform([transformed_sms])
    # 3. predict
    result = model.predict(vector_input)[0]
    # 4. Display
    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")

# credit at the bottom right
st.markdown(
    """
    <style>
    .credit {
        position: fixed;
        right: 10px;
        bottom: 10px;
        background-color: rgba(0, 0, 0, 0.7);
        color: white;
        padding: 5px 10px;
        border-radius: 5px;
        font-family: Arial, sans-serif;
        font-size: 12px;
    }
    </style>
    <div class="credit">
        © 2024 Project by Piyush Jha
    </div>
    """,
    unsafe_allow_html=True
)
