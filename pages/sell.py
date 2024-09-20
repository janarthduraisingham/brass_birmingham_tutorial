# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 00:32:30 2024

@author: jd_se
"""
import streamlit as st

st.header("The Sell Action")

st.subheader("How to Sell Cotton, Pottery, and Manufactured Goods Tiles")
video_file = open("videos/sell.mp4", "rb")
test = video_file.read()
st.video(test, format="video/mp4", start_time=0, subtitles=None, end_time=None, loop=False, autoplay=False, muted=False)

st.write("Note: you can sell as many tiles as you like in one Sell action")

st.subheader("Merchant Beer")
video_file = open("videos/merchant_beer.mp4", "rb")
test = video_file.read()
st.video(test, format="video/mp4", start_time=0, subtitles=None, end_time=None, loop=False, autoplay=False, muted=False)

st.write("Note: Merchant beer is replenished between Eras")

st.subheader("Next up:")
if st.button("The Loan Action"):
    st.switch_page("pages/loan.py")
   
st.write("Went on a tangent? Return to:")

if st.button("Eras"):
    st.switch_page("pages/eras.py")
    
