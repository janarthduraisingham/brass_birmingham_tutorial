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
game_board = st.Page("pages/game_board.py", title="2) The Game Board", icon=":material/factory:")
player_board = st.Page("pages/player_board.py", title="3) The Player Boards", icon=":material/factory:")
turns = st.Page("pages/turns.py", title="4) Turns", icon=":material/factory:")
eras = st.Page("pages/eras.py", title="5) Eras", icon=":material/factory:")
actions = st.Page("pages/actions.py", title="6) The 6 Actions", icon=":material/factory:")
changing_eras = st.Page("pages/changing_eras.py", title="7) Changing Eras", icon=":material/factory:")
network_connections = st.Page("pages/network_connections.py", title="8) Networks vs Connections", icon=":material/factory:")
coal = st.Page("pages/coal.py", title="9) Coal", icon=":material/factory:")
iron = st.Page("pages/iron.py", title="10) Iron", icon=":material/factory:")
beer = st.Page("pages/beer.py", title="11) Beer", icon=":material/factory:")



pg = st.navigation([eliza,
                    game_board,
                    player_board,
                    turns,
                    eras,
                    actions,
                    changing_eras,
                    network_connections,
                    coal,
                    iron,
                    beer
                
                    ])
pg.run()



