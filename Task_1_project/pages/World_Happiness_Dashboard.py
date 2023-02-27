import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os


# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "Happiness.jpg")

DATA_PATH = os.path.join(dir_of_interest, "data", "New.csv")

st.write('''
# :red[INNOMATICS] Intership Assignment:writing_hand: 
''')
st.write('''
##### Hello everyone, I've created a simple VIsualization Dashboard on World Happiness Report.
##### 
''')

st.subheader("Dashboard - World Happiness Report 2021")
img = image.imread(IMAGE_PATH)
st.image(img,width=800)

st.write('''
## _Dataset_ 
#### *World Happines Report*
''')

df = pd.read_csv(DATA_PATH)
st.dataframe(df)


st.write('''
## _Dataset_ 
#### *World Happines Report*
''')

st.write('''
###### This dasboard shows the many depedencies in World happines.
###### Below is the histogarm and a box plot which repesent the Freedom to make life choices by the number of people in a country
''')

Country = st.selectbox("Select the Country:", df['Country name'].unique())

col1, col2 = st.columns(2)

fig_1 = px.histogram(df[df['Country name'] == Country], x="Freedom to make life choices")
col1.plotly_chart(fig_1, use_container_width=True)

fig_2 = px.box(df[df['Country name'] == Country], x="Freedom to make life choices")
col2.plotly_chart(fig_2, use_container_width=True)


st.write('''

###### Above is the histogarm and a box plot which repesent the rate ofHealthy life expectancy at birth by the number of people in a country
''')

fig_1 = px.histogram(df[df['Country name'] == Country], x="Healthy life expectancy at birth")
col1.plotly_chart(fig_1, use_container_width=True)

fig_2 = px.box(df[df['Country name'] == Country], x="Healthy life expectancy at birth")
col2.plotly_chart(fig_2, use_container_width=True)


st.line_chart(data=df,x = 'Country name',y=['Positive affect','Negative affect'])