# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 00:32:30 2024

@author: jd_se
"""
import streamlit as st

st.header("Who Was Eliza Tinsley?")

video_file = open("videos/eliza_tinsley.mp4", "rb")
test = video_file.read()
st.video(test, format="video/mp4", start_time=0, subtitles=None, end_time=None, loop=False, autoplay=False, muted=False)

st.header("Be Eliza, and Take the Industrial Revolution")

video_file = open("videos/intro.mp4", "rb")
test = video_file.read()
st.video(test, format="video/mp4", start_time=0, subtitles=None, end_time=None, loop=False, autoplay=False, muted=False)

st.subheader("Next up:")
if st.button("Aim of the Game"):
    st.switch_page("pages/aim.py")
    

    
