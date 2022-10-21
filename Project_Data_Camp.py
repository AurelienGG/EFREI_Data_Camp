import cv2
#from turtle import color
import pandas as pd
import streamlit as st
#import seaborn as sns
#from bokeh.plotting import figure
import numpy as np
#import matplotlib.pyplot as plt
#import plotly.express as px
#import altair as alt
from streamlit_option_menu import option_menu
from PIL import Image
from io import StringIO
#import tensorflow as tf
#from tensorflow import keras
#import checkpoints
#import my_model as model2
from tensorflow import keras
from tensorflow.keras.models import Model
import tensorflow as tf
from keras.models import load_model
from PIL import Image


st.set_page_config(layout="wide")

def load_image(image_file):
	img = Image.open(image_file)
	return img

#image_logo = Image.open('C:/Users/clecl/S7 datacamp/logo_project_data_camp.png')
image_logo = cv2.imread('images/logo_project_data_camp.png')

with st.sidebar:
    st.markdown(
        f"""
        <style>
        .stsidebar {{
            background-color: #fafafa;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    choose = option_menu("Menu", ["Home","Your Test","Contact"],
                         icons=['house','download','envelope-fill'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "beige"},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#02ab21"},
    }
    )
    


if choose == "Home":

    column1, column2, column3, column4, column5, column6, column7, column8  = st.columns(8)

    with column1:

        st.write("")

    with column2:

        st.write("")

    with column3:

        st.write("")

    with column4:

        st.markdown("<h1 style='text-align: center; color: black; font-size: 80px;'>PNEUMONIA DETECTOR</h1>", unsafe_allow_html=True)

    with column5:

        st.write("")

    with column6:

        st.write("")

    with column7:

        st.write("")

    with column8:

        st.image(image_logo, width = 200)

    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    

    #image_poumons_sains = Image.open('C:/Users/clecl/S7 datacamp/image_poumon_sain.png')
    image_poumons_sains = cv2.imread('images/image_poumon_sain.png')

    #image_pneumonie = Image.open('C:/Users/clecl/S7 datacamp/image_pneumonie.png')
    image_pneumonie = cv2.imread('images/image_pneumonie.png')

    col1, col2, col3, col4, col5 = st.columns(5)

    #col1.header("Healthy")
    #col1.image(image_poumons_sains, width = 400)

    #col4.header("Pneumonia")
    #col4.image(image_pneumonie, width = 500)

    #st.image(image_poumons_sains)
    #st.image(image_pneumonie)

    with col1:

        st.write(" ")

    with col2:

        st.markdown("<h1 style='text-align: center; color: black;'>Healthy</h1>", unsafe_allow_html=True)

        st.image(image_poumons_sains, width = 400)

    with col3:

        st.write(" ")


    with col4:

        st.markdown("<h1 style='text-align: center; color: red;'>Pneumonia</h1>", unsafe_allow_html=True)

        st.image(image_pneumonie, width = 500)

    with col5:

        st.write(" ")


    
if choose == "Your Test":

    column1, column2, column3, column4, column5, column6, column7, column8  = st.columns(8)

    with column1:

        st.markdown("<h1 style='text-align: center; color: black; font-size : 50px'>Your test</h1>", unsafe_allow_html=True)

    with column2:

        st.write("")

    with column3:

        st.write("")

    with column4:

        st.write("")

    with column5:

        st.write("")

    with column6:

        st.write("")

    with column7:

        st.write("")

    with column8:

        st.image(image_logo, width = 200)
        
    # Loading the model
    model = tf.keras.models.load_model("./saved_model/my_model")
    
    upload_image = st.file_uploader("Upload Images", type=["png","jpg","jpeg"], accept_multiple_files = False)
    if upload_image is not None:
        # To See details
        file_details = {"filename":upload_image.name, "filetype":upload_image.type,"filesize":upload_image.size}
        st.write(file_details)

        # To View Uploaded Image
        st.image(load_image(upload_image), width = 200)

        image_to_read = Image.open(upload_image).convert('RGB')
        image_to_predict = np.array(image_to_read)
        image_to_predict = image_to_predict[:, :, ::-1].copy()
        img_to_predict = np.expand_dims(cv2.resize(image_to_predict, (200, 200)), axis=0)

        res = model.predict(img_to_predict)
        st.write(res)
        if res[0, 0] > res[0, 1]:
            st.header("Healthy")
        else:
            st.header("Pneumonia")

    #model2.load_weight('C:/Users/clecl/S7 datacamp')

if choose == "Contact":
    
    column1, column2, column3, column4, column5, column6, column7, column8  = st.columns(8)

    with column1:

        st.markdown("<h1 style='text-align: center; color: black; font-size : 50px'>Contact us</h1>", unsafe_allow_html=True)

    with column2:

        st.write("")

    with column3:

        st.write("")

    with column4:

        st.write("")

    with column5:

        st.write("")

    with column6:

        st.write("")

    with column7:

        st.write("")

    with column8:

        st.image(image_logo, width = 200)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1 :

        st.write("Clément Dauvois")

    with col2:

        st.write("")

    with col3 :

        st.write("Aurélien Gutierrez--Gary")

    with col4:

        st.write("")

    with col5 :

        st.write("Nicolas Gamberini")


    col1, col2, col3, col4, col5 = st.columns(5)

    with col1 :

        #st.image(Image.open('C:/Users/clecl/S7 datacamp/Photo/Photo_Clement.jpg'))
        st.image(cv2.imread('images/Photo_Clement.jpg', 0))


    with col2:

        st.write("")

    with col3 :

        #st.image(Image.open('C:/Users/clecl/S7 datacamp/Photo/Photo_Aurelien.jpg'))
        st.image(cv2.imread('images/Photo_Aurelien.jpg', 0))

    with col4:

        st.write("")

    with col5 :

        #st.image(Image.open('C:/Users/clecl/S7 datacamp/Photo/Photo_Nicolas.jpg'))
        st.image(cv2.imread('images/Photo_Nicolas.jpg', 0))

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1 :

        st.write("www.linkedin.com/in/clément-dauvois-2b5079222")

    with col2:

        st.write("")

    with col3 :

        st.write("https://www.linkedin.com/in/aurelien-gutierrez--gary/")

    with col4:

        st.write("")

    with col5 :

        st.write("https://www.linkedin.com/in/nicolas-gamberini-3b47031a0/")

    