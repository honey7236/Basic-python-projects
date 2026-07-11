import streamlit as st
import random

# ----------------------------- PAGE CONFIG -----------------------------
st.set_page_config(
    page_title="Number Hunt | Guessing Game",
    page_icon="🎯",
    layout="centered",
    initial_sidebar_state="expanded",
)

# ----------------------------- STYLES -----------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700;900&family=Poppins:wght@300;400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

.stApp {
    background: radial-gradient(circle at 20% 20%, #1b1035 0%, #0a0518 45%, #05030d 100%);
    color: #eae6ff;
}

/* Hide default streamlit chrome */
#MainMenu, footer, header {visibility: hidden;}

.hero {
    text-align: center;
    padding: 1.4rem 1rem 1rem 1rem;
}

.hero h1 {
    font-family: 'Orbitron', sans-serif;
    font-weight: 900;
    font-size: 2.6rem;
    background: linear-gradient(90deg, #7f5af0, #2cb67d, #ff8906);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0.2rem;
    letter-spacing: 1px;
}

.hero p {
    color: #a6a1c9;
    font-size: 0.95rem;
    margin-top: 0;
}

.glass-card {
    background: rgba(255, 255, 255, 0.06);
    border: 1px solid rgba(255, 255, 255, 0.12);
    border-radius: 20px;
    padding: 1.8rem 1.6rem;
    backdrop-filter: blur(14px);
    box-shadow: 0 8px 32px rgba(0,0,0,0.45);
    margin-bottom: 1.2rem;
}

.range-badge {
    display: inline-block;
    padding: 0.55rem 1.4rem;
    border-radius: 999px;
    background: linear-gradient(90deg, rgba(127,90,240,0.25), rgba(44,182,125,0.25));
    border: 1px solid rgba(255,255,255,0.15);
    font-family: 'Orbitron', sans-serif;
    font-size: 1.05rem;
    letter-spacing: 1px;
    color: #fff;
    text-align: center;
    width: 100%;
    box-sizing: border-box;
}

.stat-box {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 16px;
    padding: 0.9rem 0.6rem;
    text-align: center;
}
.stat-box .label {
    font-size: 0.72rem;
    color: #a6a1c9;
    text-transform: uppercase;
    letter-spacing: 1px;
}
.stat-box .value {
    font-family: 'Orbitron', sans-serif;
    font-size: 1.5rem;
    font-weight: 700;
    color: #fff;
    margin-top: 0.15rem;
}

.feedback {
    text-align: center;
    font-size: 1.25rem;
    font-weight: 600;
    padding: 0.9rem;
    border-radius: 14px;
    margin: 0.6rem 0 1rem 0;
    animation: pop 0.25s ease-out;
}
@keyframes pop {
    0% { transform: scale(0.9); opacity: 0; }
    100% { transform: scale(1); opacity: 1; }
}
.fb-high { background: rgba(255, 88, 88, 0.15); border: 1px solid rgba(255,88,88,0.4); color: #ff9d9d; }
.fb-low  { background: rgba(88, 149, 255, 0.15); border: 1px solid rgba(88,149,255,0.4); color: #9dc1ff; }
.fb-win  { background: rgba(44, 182, 125, 0.2); border: 1px solid rgba(44,182,125,0.5); color: #7bf0bd; }

.temp-meter {
    height: 14px;
    border-radius: 999px;
    background: linear-gradient(90deg, #2cb67d, #ffd166, #ff8906, #ff4b4b);
    position: relative;
    margin: 0.6rem 0 0.2rem 0;
    overflow: visible;
}
.temp-pointer {
    position: absolute;
    top: -8px;
    width: 4px;
    height: 30px;
    background: #fff;
    border-radius: 2px;
    box-shadow: 0 0 8px rgba(255,255,255,0.8);
    transition: left 0.35s ease;
}

.history-chip {
    display: inline-block;
    padding: 0.3rem 0.75rem;
    margin: 3px;
    border-radius: 999px;
    font-size: 0.85rem;
    font-weight: 600;
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.15);
}

.stButton>button {
    width: 100%;
    border-radius: 12px;
    background: linear-gradient(90deg, #7f5af0, #5c3fd6);
    color: white;
    border: none;
    padding: 0.6rem 0;
    font-weight: 600;
    font-size: 1rem;
    transition: transform 0.15s ease, box-shadow 0.15s ease;
}
.stButton>button:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 18px rgba(127,90,240,0.4);
}

.stNumberInput input {
    border-radius: 12px !important;
    background: rgba(255,255,255,0.07) !important;
    color: #fff !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
}
</style>
""", unsafe_allow_html=True)

# ----------------------------- SESSION STATE -----------------------------
def new_game(low=1, high=100):
    st.session_state.low = low
    st.session_state.high = high
    st.session_state.computer = random.randint(low, high)
    st.session_state.score = 0
    st.session_state.game_over = False
    st.session_state.history = []
    st.session_state.feedback = None
    st.session_state.bound_low = low
    st.session_state.bound_high = high

if "computer" not in st.session_state:
    new_game()

# ----------------------------- SIDEBAR -----------------------------
with st.sidebar:
    st.markdown("### ⚙️ Game Settings")
    difficulty = st.selectbox(
        "Choose difficulty",
        ["Easy (1-50)", "Normal (1-100)", "Hard (1-500)", "Insane (1-1000)"],
        index=1,
    )
    ranges = {
        "Easy (1-50)": (1, 50),
        "Normal (1-100)": (1, 100),
        "Hard (1-500)": (1, 500),
        "Insane (1-1000)": (1, 1000),
    }
    if st.button("🔄 New Game"):
        low, high = ranges[difficulty]
        new_game(low, high)
        st.rerun()

    st.markdown("---")
    st.markdown("### 📜 Guess History")
    if st.session_state.history:
        chips = "".join(f"<span class='history-chip'>{g}</span>" for g in st.session_state.history)
        st.markdown(chips, unsafe_allow_html=True)
    else:
        st.caption("No guesses yet. Take a shot!")

# ----------------------------- HERO -----------------------------
st.markdown("""
<div class="hero">
    <h1>🎯 NUMBER HUNT</h1>
    <p>A hidden number is waiting to be found. Trust your instincts, Hunter.</p>
</div>
""", unsafe_allow_html=True)

# ----------------------------- MAIN CARD -----------------------------
st.markdown('<div class="glass-card">', unsafe_allow_html=True)

st.markdown(
    f"<div class='range-badge'>SEARCH RANGE &nbsp;➜&nbsp; "
    f"{st.session_state.bound_low} — {st.session_state.bound_high}</div>",
    unsafe_allow_html=True,
)

st.write("")

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(f"<div class='stat-box'><div class='label'>Attempts</div>"
                f"<div class='value'>{st.session_state.score}</div></div>", unsafe_allow_html=True)
with col2:
    st.markdown(f"<div class='stat-box'><div class='label'>Low Bound</div>"
                f"<div class='value'>{st.session_state.bound_low}</div></div>", unsafe_allow_html=True)
with col3:
    st.markdown(f"<div class='stat-box'><div class='label'>High Bound</div>"
                f"<div class='value'>{st.session_state.bound_high}</div></div>", unsafe_allow_html=True)

st.write("")

if not st.session_state.game_over:
    with st.form(key="guess_form", clear_on_submit=True):
        guess = st.number_input(
            "Enter your guess",
            min_value=st.session_state.low,
            max_value=st.session_state.high,
            step=1,
            key="guess_input",
        )
        submitted = st.form_submit_button("🚀 Lock In Guess")

    if submitted:
        st.session_state.score += 1
        st.session_state.history.append(guess)
        computer = st.session_state.computer

        if guess == computer:
            st.session_state.game_over = True
            st.session_state.feedback = "win"
        elif guess < computer:
            st.session_state.feedback = "low"
            st.session_state.bound_low = max(st.session_state.bound_low, guess + 1)
        else:
            st.session_state.feedback = "high"
            st.session_state.bound_high = min(st.session_state.bound_high, guess - 1)
        st.rerun()

    # Feedback + temperature meter
    if st.session_state.feedback == "low":
        st.markdown("<div class='feedback fb-low'>📈 Too low — aim higher!</div>", unsafe_allow_html=True)
    elif st.session_state.feedback == "high":
        st.markdown("<div class='feedback fb-high'>📉 Too high — aim lower!</div>", unsafe_allow_html=True)

    if st.session_state.history:
        last = st.session_state.history[-1]
        span = st.session_state.high - st.session_state.low
        distance = abs(last - st.session_state.computer)
        closeness = max(0, 1 - (distance / (span / 2 if span else 1)))
        pointer_pos = min(96, max(2, closeness * 96))
        st.markdown(f"""
        <div class="temp-meter">
            <div class="temp-pointer" style="left:{pointer_pos}%;"></div>
        </div>
        <p style="text-align:center; font-size:0.8rem; color:#a6a1c9; margin-top:0.3rem;">
            ❄️ Cold &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 🔥 Hot
        </p>
        """, unsafe_allow_html=True)
else:
    st.balloons()
    st.markdown(
        f"<div class='feedback fb-win'>🏆 CRACKED IT! The number was "
        f"<b>{st.session_state.computer}</b> — solved in "
        f"<b>{st.session_state.score}</b> attempt(s)!</div>",
        unsafe_allow_html=True,
    )
    if st.button("🎮 Play Again"):
        low, high = st.session_state.low, st.session_state.high
        new_game(low, high)
        st.rerun()

st.markdown('</div>', unsafe_allow_html=True)

st.markdown(
    "<p style='text-align:center; color:#605b82; font-size:0.78rem;'>"
    "Built with Streamlit • Number Hunt v1.0</p>",
    unsafe_allow_html=True,
)
