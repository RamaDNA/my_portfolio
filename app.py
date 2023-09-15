import requests
import joblib
import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Welcome",page_icon=":tada:",layout="wide")

# ALL FUNCTION ------------------------------------------------------------

#create function reg_lottie
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#create predict function Netflix stock
def predict(x1,x2,x3):
    model = joblib.load('linear_regression_model.pkl')
    prediction = model.predict([[x1, x2, x3]])
    return prediction[0]

#create predict function Sentiment App Gojek
def predict_sentiment(text):
    model = joblib.load('RandomForest.pkl')
    tfidf = joblib.load('tfidf_vectorizer.pkl')
    content = [text]
    content_transformed = tfidf.transform(content)
    prediction = model.predict(content_transformed.toarray())
    return prediction[0]

#create function validate Machine Learning input
def validate_sentiment(text):
    text_sentiment = text
    if text_sentiment.strip():
        prediction = predict_sentiment(text_sentiment)
        st.write("The Prediction is",prediction)
    else:
        st.write("Please provide feedback to get a prediction.")

# END FUNCTION ------------------------------------------------------------

# --READ ASSETS--
lottie_coding = load_lottie_url("https://assets4.lottiefiles.com/packages/lf20_4kx2q32n.json")
chart = load_lottie_url("https://assets6.lottiefiles.com/packages/lf20_yrelFtPfpX.json")
machine_learning = load_lottie_url("https://assets9.lottiefiles.com/packages/lf20_KS2VTJka6L.json")

#--image ASSETS--


#create sidebar
menu = ['Home','My project']
choice = st.sidebar.selectbox("Select a Page", menu)

#home page
if choice == 'Home':
    #welcome
    with st.container():
        st.header("welcome")
        st.write("This is my Portfolio")
        st.title("Hello my name is Rama Dona Ariyatma")
        st.write("I'm Data Science, web progammer from Indonesia")
    #what i do
    with st.container():
        st.write("---")
        what_i_do,lottie_animation = st.columns(2)
        with what_i_do:
            st_lottie(lottie_coding, height = 400, key="coding")
        with lottie_animation:
            st.header("what I do")
            st.write("""
            - Create A model for machine learning or Deep Learning using Python and mining data
                - Cleaning data
                - Scrapping data
                - Create Model
                - NLTK
                - TensorFlow
                - Keras
                - Visualization
            - In Web progammer
                - Using php and framework like laravel i know about OOP and MVC
                - Bootstrap
                - CSS
                - Javascript
            - Mobile dev
                - I try flutter
                - Kotlin""")
    #example 
    with st.container():
        st.write("---")
        st.write("<div style='text-align:center'><h3> Like Example </h3></div>",unsafe_allow_html=True)
        one,two = st.columns(2)
        with one:
            st.write("<div style='text-align:center'><h4> Prediction </h4></div>",unsafe_allow_html=True)
            st_lottie(chart,height=300,key="chart")
        with two:
            st.write("<div style='text-align:center'><h4> Machine learning </h4></div>",unsafe_allow_html=True)
            st_lottie(machine_learning,height=300,key="machine_learning")
    #contact container
    with st.container():
        st.write("---")
        st.header("Contact Me")
        email,whatsapp,instragram,facebook = st.columns(4)
        with email:
            st.write("my email")
            st.write("rama99ever@gmail.com")
        with whatsapp:
            st.write("my whatsapp")
            st.write("+62-813-817-37058")
        with instragram:
            st.write("my Instagram")
            st.markdown("[My instagram](https:www.instagram.com)")
        with facebook:
            st.write('my facebook')
            st.markdown("[my facebook](https:www.facebook.com)")

elif choice == 'My project':
    st.header("This is my project")
    with st.container():
        image_project,explanation = st.columns(2)
        with image_project:
            st.header("Predict Netflix Price")
            open = st.number_input('Enter your Open price')
            high = st.number_input('Enter your High price')
            low = st.number_input('Enter your Low price')
            prediction = predict(open, high, low)
            st.write("The prediction Is", prediction)
        with explanation:
            st.header("Explain")
            st.write("You can predict the end price just input open price,high price, low price and get predicted")
    with st.container():
        st.write("---")
        input_form,explanation = st.columns(2)
        with input_form:
            st.header("Prediction Sentiment App Gojek")
            text_sentiment = st.text_area('Enter your Feedback App Gojek')
            validate_sentiment(text_sentiment)
        with explanation:
            st.header("Explain Machine Learning")
            st.write("We can prediction what's meaning feedback is Positif or Negatif just insert ur comment if ur in smartphone just click button ctrl + enter")
    with st.container():
        st.write("---")
        st.header("I Will update Soon to upload my next project")
