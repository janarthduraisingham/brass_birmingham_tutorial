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
st.write("Note: Locations with no name cannot be built on with Location Wildcards")
st.write("Note: in the Canal Era, you may only build one industry tile in one location. In the Railway Era, you may build multiple industry tiles in the same location (though not in the same slot)")

st.subheader("Costs and Requisites")
video_file = open("videos/costs_requisites.mp4", "rb")
test = video_file.read()
st.video(test, format="video/mp4", start_time=0, subtitles=None, end_time=None, loop=False, autoplay=False, muted=False)

st.subheader("Adding resources to Tiles")
video_file = open("videos/loading_resources.mp4", "rb")
test = video_file.read()
st.video(test, format="video/mp4", start_time=0, subtitles=None, end_time=None, loop=False, autoplay=False, muted=False)

st.subheader("Exceptions for your First Build")
video_file = open("videos/first_build.mp4", "rb")
test = video_file.read()
st.video(test, format="video/mp4", start_time=0, subtitles=None, end_time=None, loop=False, autoplay=False, muted=False)


st.subheader("Overbuilding your Tiles")
video_file = open("videos/overbuilding_self.mp4", "rb")
test = video_file.read()
st.video(test, format="video/mp4", start_time=0, subtitles=None, end_time=None, loop=False, autoplay=False, muted=False)

st.subheader("Overbuilding Other Players' Tiles")
video_file = open("videos/overbuilding_others.mp4", "rb")
test = video_file.read()
st.video(test, format="video/mp4", start_time=0, subtitles=None, end_time=None, loop=False, autoplay=False, muted=False)

st.subheader("Next up:")
if st.button("The Sell Action"):
    st.switch_page("pages/sell.py")
   
st.write("Went on a tangent? Return to:")

if st.button("Eras"):
    st.switch_page("pages/eras.py")
    
