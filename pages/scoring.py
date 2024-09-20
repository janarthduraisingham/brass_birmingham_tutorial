# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 00:32:30 2024

@author: jd_se
"""
import streamlit as st

st.header("Scoring")

st.subheader("Scoring Link Tiles")
video_file = open("videos/scoring_links.mp4", "rb")
test = video_file.read()
st.video(test, format="video/mp4", start_time=0, subtitles=None, end_time=48, loop=False, autoplay=False, muted=False)


st.subheader("Scoring Flipped Industry Tiles")
video_file = open("videos/scoring_flipped.mp4", "rb")
test = video_file.read()
st.video(test, format="video/mp4", start_time=0, subtitles=None, end_time=48, loop=False, autoplay=False, muted=False)


st.subheader("Next up:")
if st.button("Networks vs Connections"):
    st.switch_page("pages/network_connections.py")
    
st.write("Went on a tangent? Return to:")

if st.button("Eras"):
    st.switch_page("pages/eras.py")
    
