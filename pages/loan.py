# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 00:32:30 2024

@author: jd_se
"""
import streamlit as st

st.header("The Loan Action")

video_file = open("videos/loan.mp4", "rb")
test = video_file.read()
st.video(test, format="video/mp4", start_time=0, subtitles=None, end_time=None, loop=False, autoplay=False, muted=False)

st.write("Note: You never have to repay the £30 loan")

st.subheader("Next up:")
if st.button("The Scout Action"):
    st.switch_page("pages/scout.py")
   
st.write("Went on a tangent? Return to:")

if st.button("Eras"):
    st.switch_page("pages/eras.py")
    
