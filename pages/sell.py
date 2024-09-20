# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 00:32:30 2024

@author: jd_se
"""
import streamlit as st

st.header("Consuming Beer")

st.subheader("Where to consume Beer from")
video_file = open("videos/beer.mp4", "rb")
test = video_file.read()
st.video(test, format="video/mp4", start_time=0, subtitles=None, end_time=None, loop=False, autoplay=False, muted=False)

st.subheader("Next up:")
if st.button("The Build Action"):
    st.switch_page("pages/build.py")
   
st.write("Went on a tangent? Return to:")

if st.button("Eras"):
    st.switch_page("pages/eras.py")
    
