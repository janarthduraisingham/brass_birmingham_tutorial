# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 00:32:30 2024

@author: jd_se
"""
import streamlit as st

st.header("Aim of the Game")

st.subheader("Victory Points")
video_file = open("videos/aim.mp4", "rb")
test = video_file.read()
st.video(test, format="video/mp4", start_time=0, subtitles=None, end_time=None, loop=False, autoplay=False, muted=False)

st.subheader("Eras")
video_file = open("videos/eras.mp4", "rb")
test = video_file.read()
st.video(test, format="video/mp4", start_time=0, subtitles=None, end_time=None, loop=False, autoplay=False, muted=False)


st.subheader("Next up:")
if st.button("The Game Board"):
    st.switch_page("pages/game_board.py")
    

    
