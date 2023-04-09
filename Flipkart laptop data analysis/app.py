import streamlit as st
import pickle
import numpy as np

#import model
pipe = pickle.load(open('pipe.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))

st.title('Laptop Price Predictor')

#brand 
company = st.selectbox('Brand',df['Company'].unique())

#Operating system
Opsy = st.selectbox('Operating system',df['OS'].unique())

# RAM_type
Ram_Type = st.selectbox('Ram Type',df['RAM_type'].unique())

# RAM
Ram= st.selectbox('RAM(in GB)',[4,8,16,32])

#Display
Display = st.select_slider('Display(cm)',options=df['Display(cm)'].unique())

#HDD
Hdd = st.selectbox('HDD(IN gb)',[0,128,256,512,1000])

#SSD
Ssd= st.selectbox('SSD(in GB)',[0,128,256,512,1000,2000])

#GPY BRNAD
GPU_Brand = st.selectbox('GPU_Brand',df['GPU_brand'].unique())


if st.button('Predict Price'):
    #query 
    query = np.array([company,Opsy,Ram_Type,Ram,Display,Hdd,Ssd,GPU_Brand])
    
    query = query.reshape(1,8)
    st.title("The predicted price of this configuration is " + str(int(np.exp(pipe.predict(query)[0]))))