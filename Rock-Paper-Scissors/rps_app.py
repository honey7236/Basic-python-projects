import streamlit as st
from random import randint
import time

# ----------------------------
# Page config
# ----------------------------
st.set_page_config(
    page_title="Rock Paper Scissors",
    page_icon="✂️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ----------------------------
# Custom CSS - dark gradient theme
# ----------------------------
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
        color: #f0f0f0;
    }

    #MainMenu, footer, header {visibility: hidden;}

    .main-title {
        text-align: center;
        font-size: 3rem;
        font-weight: 800;
        background: linear-gradient(90deg, #ff6ec4, #7873f5, #4ade80);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0px;
        padding-top: 10px;
    }

    .subtitle {
        text-align: center;
        color: #a0a0c0;
        font-size: 1.05rem;
        margin-bottom: 25px;
    }

    .score-card {
        background: rgba(255, 255, 255, 0.06);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.12);
        border-radius: 18px;
        padding: 18px 10px;
        text-align: center;
        box-shadow: 0 8px 32px rgba(0,0,0,0.3);
    }

    .score-label {
        font-size: 0.85rem;
        color: #b0b0d0;
        letter-spacing: 1px;
        text-transform: uppercase;
    }

    .score-value {
        font-size: 2rem;
        font-weight: 700;
        margin-top: 4px;
    }

    .win-color { color: #4ade80; }
    .lose-color { color: #f87171; }
    .draw-color { color: #facc15; }

    .battle-card {
        background: rgba(255, 255, 255, 0.06);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.12);
        border-radius: 22px;
        padding: 30px;
        margin-top: 25px;
        text-align: center;
        box-shadow: 0 8px 32px rgba(0,0,0,0.35);
    }

    .emoji-big {
        font-size: 5rem;
        line-height: 1.1;
    }

    .vs-text {
        font-size: 1.8rem;
        font-weight: 700;
        color: #a0a0c0;
        padding: 0 10px;
    }

    .result-banner {
        font-size: 1.6rem;
        font-weight: 800;
        text-align: center;
        padding: 14px;
        border-radius: 14px;
        margin-top: 20px;
    }

    .banner-win {
        background: rgba(74, 222, 128, 0.15);
        border: 1px solid #4ade80;
        color: #4ade80;
    }

    .banner-lose {
        background: rgba(248, 113, 113, 0.15);
        border: 1px solid #f87171;
        color: #f87171;
    }

    .banner-draw {
        background: rgba(250, 204, 21, 0.15);
        border: 1px solid #facc15;
        color: #facc15;
    }

    div.stButton > button {
        width: 100%;
        height: 90px;
        font-size: 2.5rem;
        border-radius: 18px;
        border: 1px solid rgba(255,255,255,0.15);
        background: rgba(255, 255, 255, 0.05);
        color: white;
        transition: all 0.2s ease;
    }

    div.stButton > button:hover {
        background: linear-gradient(135deg, #7873f5, #ff6ec4);
        border: 1px solid transparent;
        transform: translateY(-3px);
    }

    .choice-label {
        text-align: center;
        color: #a0a0c0;
        font-size: 0.85rem;
        margin-top: -8px;
        margin-bottom: 15px;
        letter-spacing: 1px;
        text-transform: uppercase;
    }
</style>
""", unsafe_allow_html=True)

# ----------------------------
# Game constants & logic
# ----------------------------
CHOICES = {1: ("Rock", "🪨"), 2: ("Paper", "📄"), 3: ("Scissor", "✂️")}

BEATS = {1: 3, 2: 1, 3: 2}  # rock beats scissor, paper beats rock, scissor beats paper

def get_result(user, computer):
    if user == computer:
        return "draw"
    elif BEATS[user] == computer:
        return "win"
    else:
        return "lose"

# ----------------------------
# Session state
# ----------------------------
if "wins" not in st.session_state:
    st.session_state.wins = 0
if "losses" not in st.session_state:
    st.session_state.losses = 0
if "draws" not in st.session_state:
    st.session_state.draws = 0
if "last_user" not in st.session_state:
    st.session_state.last_user = None
if "last_computer" not in st.session_state:
    st.session_state.last_computer = None
if "last_result" not in st.session_state:
    st.session_state.last_result = None

# ----------------------------
# Header
# ----------------------------
st.markdown('<div class="main-title">Rock · Paper · Scissor</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Pick your weapon and challenge the computer</div>', unsafe_allow_html=True)

# ----------------------------
# Scoreboard
# ----------------------------
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown(f'''
        <div class="score-card">
            <div class="score-label">Wins</div>
            <div class="score-value win-color">{st.session_state.wins}</div>
        </div>
    ''', unsafe_allow_html=True)
with c2:
    st.markdown(f'''
        <div class="score-card">
            <div class="score-label">Draws</div>
            <div class="score-value draw-color">{st.session_state.draws}</div>
        </div>
    ''', unsafe_allow_html=True)
with c3:
    st.markdown(f'''
        <div class="score-card">
            <div class="score-label">Losses</div>
            <div class="score-value lose-color">{st.session_state.losses}</div>
        </div>
    ''', unsafe_allow_html=True)

st.write("")
st.write("")

# ----------------------------
# Choice buttons
# ----------------------------
b1, b2, b3 = st.columns(3)

def play(user_choice):
    computer_choice = randint(1, 3)
    result = get_result(user_choice, computer_choice)

    st.session_state.last_user = user_choice
    st.session_state.last_computer = computer_choice
    st.session_state.last_result = result

    if result == "win":
        st.session_state.wins += 1
    elif result == "lose":
        st.session_state.losses += 1
    else:
        st.session_state.draws += 1

with b1:
    if st.button("🪨", key="rock"):
        play(1)
    st.markdown('<div class="choice-label">Rock</div>', unsafe_allow_html=True)

with b2:
    if st.button("📄", key="paper"):
        play(2)
    st.markdown('<div class="choice-label">Paper</div>', unsafe_allow_html=True)

with b3:
    if st.button("✂️", key="scissor"):
        play(3)
    st.markdown('<div class="choice-label">Scissor</div>', unsafe_allow_html=True)

# ----------------------------
# Battle result display
# ----------------------------
if st.session_state.last_user is not None:
    user_name, user_emoji = CHOICES[st.session_state.last_user]
    comp_name, comp_emoji = CHOICES[st.session_state.last_computer]

    st.markdown(f'''
        <div class="battle-card">
            <div style="display:flex; justify-content:center; align-items:center;">
                <div>
                    <div class="emoji-big">{user_emoji}</div>
                    <div class="choice-label">You: {user_name}</div>
                </div>
                <div class="vs-text">VS</div>
                <div>
                    <div class="emoji-big">{comp_emoji}</div>
                    <div class="choice-label">Computer: {comp_name}</div>
                </div>
            </div>
        </div>
    ''', unsafe_allow_html=True)

    result = st.session_state.last_result
    if result == "win":
        st.markdown('<div class="result-banner banner-win">🎉 You Win!</div>', unsafe_allow_html=True)
    elif result == "lose":
        st.markdown('<div class="result-banner banner-lose">💀 You Lost!</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="result-banner banner-draw">🤝 It\'s a Draw!</div>', unsafe_allow_html=True)

st.write("")

# ----------------------------
# Reset button
# ----------------------------
if st.button("🔄 Reset Game", key="reset"):
    st.session_state.wins = 0
    st.session_state.losses = 0
    st.session_state.draws = 0
    st.session_state.last_user = None
    st.session_state.last_computer = None
    st.session_state.last_result = None
    st.rerun()
