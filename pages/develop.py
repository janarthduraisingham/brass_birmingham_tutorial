# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 00:32:30 2024

@author: jd_se
"""
import streamlit as st

st.header("The Develop Action")

st.write("To perform the Develop Action, discard one card from your card. Then discard the lowest 1 or 2 industry tiles from the same or different industries on your player board, consuming 1 iron for each tile you remove")
st.write("Note: Tiles with a crossed out light bulb cannot be Developed away")

#video_file = open("videos/develop.mp4", "rb")
#test = video_file.read()
#st.video(test, format="video/mp4", start_time=0, subtitles=None, end_time=None, loop=False, autoplay=False, muted=False)

st.subheader("Next up:")
if st.button("The Network Action"):
    st.switch_page("pages/network.py")
   
#st.write("Went on a tangent? Return to:")

#if st.button("Eras"):
#    st.switch_page("pages/eras.py")
    
