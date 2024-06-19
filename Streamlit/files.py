import streamlit as st
import pandas as pd


st.subheader("Uploading the CSV File")
df=st.file_uploader("Upload the CSV file :",type=['csv','pdf','xlsx'])

df=pd.read_csv("Details.csv")
if df is not None:
    st.table(df.head())

st.subheader("Dealing with Images")
st.text("Rohit Sharma")    
st.image('Hitman.jpg')

st.subheader("Dealing with images while uploading")
img=st.file_uploader("Uploading the image file :",type=['png','jpg','jpeg'])
if img is not None:
    st.image(img)


st.subheader("Working with Videos")
video_file=st.file_uploader("Uploading the video file :", type=['mkv','mp4'])
if video_file is not None:
    st.video(video_file,start_time=5)


st.subheader("Working with Audio file ")
audio_file=st.file_uploader("Uploading the audio file :",type=['mp3','wav'])
if audio_file is not None:
    st.audio(audio_file)
