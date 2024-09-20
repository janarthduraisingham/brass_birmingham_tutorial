# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 11:51:36 2024

@author: jd_se
"""
import streamlit as st


st.set_page_config(page_title="Brass: Birmingham Tutorial", page_icon=":factory:",
                   initial_sidebar_state='collapsed')

st.title("Brass Birmingham: How to Play")
st.write("G. Brown, M. Tolman, M. Wallace (2018). Brass: Birmingham [Board Game]. Roxley")

eliza = st.Page("pages/eliza.py", title="1) Who was Eliza Tinsley?", icon=":material/factory:")
aim = st.Page("pages/aim.py", title="2) Aim of the Game", icon=":material/factory:")
game_board = st.Page("pages/game_board.py", title="3) The Game Board", icon=":material/factory:")
player_board = st.Page("pages/player_board.py", title="4) The Player Boards", icon=":material/factory:")
turns = st.Page("pages/turns.py", title="5) Turns", icon=":material/factory:")
rounds = st.Page("pages/rounds.py", title="6) Rounds", icon=":material/factory:")
scoring = st.Page("pages/scoring.py", title="7) Scoring", icon=":material/factory:")
changing_eras = st.Page("pages/changing_eras.py", title="8) Changing Eras", icon=":material/factory:")
flipping_tiles = st.Page("pages/flipping_tiles.py", title="9) Flipping Industry Tiles", icon=":material/factory:")
network_connections = st.Page("pages/network_connections.py", title="10) Networks and Connections", icon=":material/factory:")
coal = st.Page("pages/coal.py", title="11) Consuming Coal", icon=":material/factory:")
iron = st.Page("pages/iron.py", title="12) Consuming Iron", icon=":material/factory:")
beer = st.Page("pages/beer.py", title="13) Consuming Beer", icon=":material/factory:")
build = st.Page("pages/build.py", title="14) The Build Action", icon=":material/factory:")
sell = st.Page("pages/sell.py", title="15) The Sell Action", icon=":material/factory:")
loan = st.Page("pages/loan.py", title="16) The Loan Action", icon=":material/factory:")
scout = st.Page("pages/scout.py", title="17) The Scout Action", icon=":material/factory:")
develop = st.Page("pages/develop.py", title="18) The Develop Action", icon=":material/factory:")
network = st.Page("pages/network.py", title="19) The Network Action", icon=":material/factory:")



pg = st.navigation([eliza,
                    aim,
                    game_board,
                    player_board,
                    turns,
                    rounds,
                    scoring,
                    changing_eras,
                    flipping_tiles,
                    network_connections,
                    coal,
                    iron,
                    beer,
                    build,
                    sell,
                    loan,
                    scout,
                    develop,
                    network
                
                    ])
pg.run()



