# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 11:51:36 2024

@author: jd_se
"""
import streamlit as st


st.set_page_config(page_title="Brass: Birmingham Tutorial", page_icon=":european_castle:",
                   initial_sidebar_state='collapsed')

st.title("Brass Biringham: How to Play")


eliza = st.Page("eliza.py", title="1) Who was Eliza Tinsley", icon=":material/castle:")
game_board = st.Page("board.py", title="2) The Game Board", icon=":material/castle:")
player_board = st.Page("setup.py", title="3) The PLayer Boards", icon=":material/castle:")
turns = st.Page("turns.py", title="4) Turns", icon=":material/castle:")
eras = st.Page("eras.py", title="5) Eras", icon=":material/castle:")
actions = st.Page("actions.py", title="6) The 6 Actions", icon=":material/castle:")
changing_eras = st.Page("changing_eras.py", title="7) Changing Eras", icon=":material/castle:")
network_connections = st.Page("network_connections.py", title="8) Networks vs Connections", icon=":material/castle:")
coal = st.Page("coal.py", title="9) Coal", icon=":material/castle:")
iron = st.Page("iron.py", title="10) Iron", icon=":material/castle:")
beer = st.Page("beer.py", title="11) Beer", icon=":material/castle:")



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



