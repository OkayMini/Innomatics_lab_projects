import streamlit as st
import requests
import pandas as pd
from matplotlib import image
import os

PAGE_TITLE = "Nandini Shukla|Portfolio"
PAGE_ICON = ":wave:"

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON,initial_sidebar_state="auto")

def load_lottieurl(url):
 r=requests.get(url)
 if r.status_code !=200:
  return None
 return r.json()

st.title(":blue[Nandini shukla] :wave:")

st.image('Profile.png',width=250) 
st. header('My Portfolio :sunglasses:')
#st.write('Here is a breakdown of my portfolio:')
st.write("A data science enthusiast with experience in Python language, have a strong foundation in data analysis, visualization, and machine learning. I'm also comfortable working with various types of data sources, building and evaluating machine learning models, and using data visualization techniques to communicate insights effectively.")


st.subheader("Skills & Tools ⚒️")

btn_click = st.button("TOOLS")

if btn_click == True:
    st.write(""" Jupyter Notebook ,
             VSCode, Python Web Scraping Tools,
             Requests,
             Beautiful Soup.
             """)
    st.balloons()

btn_click = st.button("SKILLS")

if btn_click == True:
    st.write("Python, Numpy,Pandas, Data Analysis")
    st.balloons()


st.subheader("Contect me :coffee:")

st.markdown("Github Account Link - https://github.com/OkayMini")

st.markdown("Linkedin Account Link - https://www.linkedin.com/in/nandini-shukla-40ab9020a/")

