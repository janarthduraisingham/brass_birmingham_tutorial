# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 00:32:30 2024

@author: jd_se
"""
import streamlit as st

st.header("Networks and Connections")

st.subheader("Your Network")
video_file = open("videos/network.mp4", "rb")
test = video_file.read()
st.video(test, format="video/mp4", start_time=0, subtitles=None, end_time=None, loop=False, autoplay=False, muted=False)

st.subheader("Connected Locations")
video_file = open("videos/connected.mp4", "rb")
test = video_file.read()
st.video(test, format="video/mp4", start_time=0, subtitles=None, end_time=None, loop=False, autoplay=False, muted=False)

st.subheader("Examples:")
st.subheader("Network Example")
video_file = open("videos/network_example.mp4", "rb")
test = video_file.read()
st.video(test, format="video/mp4", start_time=0, subtitles=None, end_time=None, loop=False, autoplay=False, muted=False)

st.subheader("Connected Example")
video_file = open("videos/connected_example.mp4", "rb")
test = video_file.read()
st.video(test, format="video/mp4", start_time=0, subtitles=None, end_time=None, loop=False, autoplay=False, muted=False)

st.subheader("Next up:")
if st.button("Consuming Coal"):
    st.switch_page("pages/coal.py")
    
#st.write("Went on a tangent? Return to:")

#if st.button("Eras"):
#    st.switch_page("pages/eras.py")
    
