# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 00:32:30 2024

@author: jd_se
"""
import streamlit as st

st.header("The Build Action")

st.subheader("What and Where can you Build?")
video_file = open("videos/what_where_build.mp4", "rb")
test = video_file.read()
st.video(test, format="video/mp4", start_time=0, subtitles=None, end_time=None, loop=False, autoplay=False, muted=False)

st.write("Note: if a location has multiple spaces for your industry tile of choice, you must choose the space showing only that industry")

st.subheader("Costs and Requisites")
video_file = open("videos/costs_requisites.mp4", "rb")
test = video_file.read()
st.video(test, format="video/mp4", start_time=0, subtitles=None, end_time=None, loop=False, autoplay=False, muted=False)

#st.subheader("Adding resources to Tiles")
#video_file = open("videos/costs_requisites.mp4", "rb")
#test = video_file.read()
#st.video(test, format="video/mp4", start_time=0, subtitles=None, end_time=None, loop=False, autoplay=False, muted=False)


st.subheader("Next up:")
if st.button("The Build Action"):
    st.switch_page("pages/build.py")
   
st.write("Went on a tangent? Return to:")

if st.button("Eras"):
    st.switch_page("pages/eras.py")
    
