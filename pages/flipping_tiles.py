# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 00:32:30 2024

@author: jd_se
"""
import streamlit as st

st.header("Flipping Industry Tiles")

st.subheader("Flipping Cotton, Manufactured Goods, and Pottery Industry Tiles")
video_file = open("videos/flipping_cotton_goods_pottery.mp4", "rb")
test = video_file.read()
st.video(test, format="video/mp4", start_time=0, subtitles=None, end_time=None, loop=False, autoplay=False, muted=False)

st.subheader("Flipping Coal, Iron, and Beer Idustry Tiles")
video_file = open("videos/flipping_coal_iron_beer.mp4", "rb")
test = video_file.read()
st.video(test, format="video/mp4", start_time=0, subtitles=None, end_time=None, loop=False, autoplay=False, muted=False)


st.subheader("Next up:")
if st.button("Networks and Connections"):
    st.switch_page("pages/network_connections.py")
    
#st.write("Went on a tangent? Return to:")

#if st.button("Eras"):
#    st.switch_page("pages/eras.py")
    
