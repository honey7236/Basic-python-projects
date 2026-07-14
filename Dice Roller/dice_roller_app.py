"""
Project #8 - 🎲 Dice Roller
Random module, loops -> Streamlit UI
"""

import streamlit as st
import random
import time

st.set_page_config(page_title="Dice Roller", page_icon="🎲", layout="centered")

# ---------------------------------------------------------
# STYLING - Dark gradient glass-card theme (signature look)
# ---------------------------------------------------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
    background-attachment: fixed;
}

#MainMenu, footer, header {visibility: hidden;}

.block-container {
    padding-top: 2.5rem;
    max-width: 720px;
}

.glass-card {
    background: rgba(255, 255, 255, 0.06);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 1px solid rgba(255, 255, 255, 0.12);
    border-radius: 22px;
    padding: 2.2rem 2rem;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.35);
    margin-bottom: 1.5rem;
}

.title-text {
    text-align: center;
    font-size: 2.4rem;
    font-weight: 800;
    background: linear-gradient(90deg, #a78bfa, #f472b6, #facc15);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0.2rem;
}

.subtitle-text {
    text-align: center;
    color: rgba(255,255,255,0.55);
    font-size: 0.95rem;
    margin-bottom: 1.8rem;
}

.dice-display {
    text-align: center;
    font-size: 8rem;
    line-height: 1;
    filter: drop-shadow(0 0 25px rgba(167, 139, 250, 0.5));
    margin: 0.5rem 0 1rem 0;
}

.result-number {
    text-align: center;
    font-size: 1.3rem;
    font-weight: 700;
    color: #facc15;
    letter-spacing: 2px;
}

.stat-box {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 16px;
    padding: 1rem;
    text-align: center;
}

.stat-value {
    font-size: 1.6rem;
    font-weight: 800;
    color: #a78bfa;
}

.stat-label {
    font-size: 0.78rem;
    color: rgba(255,255,255,0.5);
    text-transform: uppercase;
    letter-spacing: 1px;
}

.history-chip {
    display: inline-block;
    background: rgba(167, 139, 250, 0.15);
    border: 1px solid rgba(167, 139, 250, 0.35);
    color: #e9d5ff;
    padding: 0.35rem 0.8rem;
    border-radius: 10px;
    margin: 3px;
    font-size: 1.1rem;
    font-weight: 600;
}

div.stButton > button {
    width: 100%;
    background: linear-gradient(90deg, #7c3aed, #ec4899);
    color: white;
    border: none;
    border-radius: 14px;
    padding: 0.8rem 0;
    font-size: 1.05rem;
    font-weight: 700;
    letter-spacing: 1px;
    transition: transform 0.15s ease, box-shadow 0.15s ease;
    box-shadow: 0 4px 18px rgba(124, 58, 237, 0.4);
}

div.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 24px rgba(236, 72, 153, 0.5);
}

.secondary-btn button {
    background: rgba(255,255,255,0.08) !important;
    box-shadow: none !important;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# SESSION STATE
# ---------------------------------------------------------
if "history" not in st.session_state:
    st.session_state.history = []
if "current_rolls" not in st.session_state:
    st.session_state.current_rolls = None

DICE_FACES = {1: "⚀", 2: "⚁", 3: "⚂", 4: "⚃", 5: "⚄", 6: "⚅"}

# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------
st.markdown('<div class="title-text">🎲 Dice Roller</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle-text">Random Module &nbsp;•&nbsp; Loops &nbsp;•&nbsp; Streamlit UI</div>', unsafe_allow_html=True)

# ---------------------------------------------------------
# CONTROLS
# ---------------------------------------------------------
st.markdown('<div class="glass-card">', unsafe_allow_html=True)

num_dice = st.slider("Number of dice", min_value=1, max_value=5, value=1)

col1, col2 = st.columns([3, 1])
with col1:
    roll_clicked = st.button("🎲 ROLL THE DICE", use_container_width=True)
with col2:
    st.markdown('<div class="secondary-btn">', unsafe_allow_html=True)
    clear_clicked = st.button("🗑️ Clear", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

if clear_clicked:
    st.session_state.history = []
    st.session_state.current_rolls = None
    st.rerun()

if roll_clicked:
    placeholder = st.empty()
    # quick shuffle animation
    for _ in range(8):
        temp = [random.randint(1, 6) for _ in range(num_dice)]
        faces = " ".join(DICE_FACES[t] for t in temp)
        placeholder.markdown(f'<div class="dice-display">{faces}</div>', unsafe_allow_html=True)
        time.sleep(0.05)

    final_rolls = [random.randint(1, 6) for _ in range(num_dice)]
    st.session_state.current_rolls = final_rolls
    st.session_state.history.extend(final_rolls)
    placeholder.empty()

if st.session_state.current_rolls:
    rolls = st.session_state.current_rolls
    faces = " ".join(DICE_FACES[r] for r in rolls)
    st.markdown(f'<div class="dice-display">{faces}</div>', unsafe_allow_html=True)
    if len(rolls) == 1:
        st.markdown(f'<div class="result-number">YOU ROLLED A {rolls[0]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(
            f'<div class="result-number">{" + ".join(map(str, rolls))} &nbsp;=&nbsp; {sum(rolls)}</div>',
            unsafe_allow_html=True,
        )
else:
    st.markdown('<div class="dice-display">🎲</div>', unsafe_allow_html=True)
    st.markdown('<div class="result-number" style="color:rgba(255,255,255,0.4);">Press ROLL to begin</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------------------------------------
# STATS
# ---------------------------------------------------------
if st.session_state.history:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<div class="subtitle-text" style="margin-bottom:1rem;">📊 Session Stats</div>', unsafe_allow_html=True)

    total_rolls = len(st.session_state.history)
    avg_roll = sum(st.session_state.history) / total_rolls
    highest = max(st.session_state.history)
    lowest = min(st.session_state.history)

    c1, c2, c3, c4 = st.columns(4)
    for col, label, value in zip(
        [c1, c2, c3, c4],
        ["Total Rolls", "Average", "Highest", "Lowest"],
        [total_rolls, f"{avg_roll:.2f}", highest, lowest],
    ):
        with col:
            st.markdown(
                f'<div class="stat-box"><div class="stat-value">{value}</div>'
                f'<div class="stat-label">{label}</div></div>',
                unsafe_allow_html=True,
            )

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="subtitle-text">Roll Distribution</div>', unsafe_allow_html=True)
    distribution = {i: st.session_state.history.count(i) for i in range(1, 7)}
    st.bar_chart(distribution)

    st.markdown('<div class="subtitle-text" style="margin-top:1rem;">Recent History</div>', unsafe_allow_html=True)
    recent = st.session_state.history[-20:][::-1]
    chips = "".join(f'<span class="history-chip">{r}</span>' for r in recent)
    st.markdown(chips, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

st.markdown(
    '<div style="text-align:center; color:rgba(255,255,255,0.3); font-size:0.8rem;">'
    'Project #8 &nbsp;|&nbsp; Built with Python + Streamlit</div>',
    unsafe_allow_html=True,
)
