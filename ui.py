import streamlit as st
import random

choices = ["rock","paper","scissor"]
computer = random.choice(choices)
player = None

st.header("Rock Paper Scissor Game 🪨📄✂️🎮")

player = st.text_input('Enter your choice:', placeholder='Rock | Paper | Scissor').lower()

submit_btn = st.button('submit')

if submit_btn:
    if player == '':
        st.text('Enter your choice. 😶')
    elif player not in choices:
        st.text('Do not enter other words. 😶‍🌫️')
    else:
        st.text(f'Computer: {computer}')
        st.text(f'Player: {player}')

        if player == computer:
            st.text('Match draw 😐')
        elif player == 'rock':
            if computer == 'paper':
                st.text('Computer win 🥲')
            elif computer == 'scissor':
                st.text('You Win 🙂')
        elif player == 'paper':
            if computer == 'rock':
                st.text('You win 🙂')
            elif computer == 'scissor':
                st.text('Computer win 🥲')
        elif player == 'scissor':
            if computer == 'paper':
                st.text('You win 🙂')
            elif computer == 'rock':
                st.text('Computer win 🥲')
