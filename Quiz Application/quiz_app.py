import streamlit as st
import random
from data import python_questions, gk_questions, cs_questions

# ----------------------------- PAGE CONFIG -----------------------------
st.set_page_config(
    page_title="QuizVerse | The Ultimate Quiz Arena",
    page_icon="❓",
    layout="centered",
    initial_sidebar_state="collapsed",
)

QUESTIONS_PER_QUIZ = 10

CATEGORIES = {
    "🐍 Python": python_questions,
    "🌍 General Knowledge": gk_questions,
    "💻 Computer Science": cs_questions,
}

# ----------------------------- STYLES -----------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700;900&family=Poppins:wght@300;400;500;600&display=swap');

html, body, [class*="css"] { font-family: 'Poppins', sans-serif; }

.stApp {
    background: radial-gradient(circle at 20% 20%, #1b1035 0%, #0a0518 45%, #05030d 100%);
    color: #eae6ff;
}
#MainMenu, footer, header {visibility: hidden;}

.hero { text-align: center; padding: 1.4rem 1rem 1rem 1rem; }
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
.hero p { color: #a6a1c9; font-size: 0.95rem; margin-top: 0; }

.glass-card {
    background: rgba(255, 255, 255, 0.06);
    border: 1px solid rgba(255, 255, 255, 0.12);
    border-radius: 20px;
    padding: 1.8rem 1.6rem;
    backdrop-filter: blur(14px);
    box-shadow: 0 8px 32px rgba(0,0,0,0.45);
    margin-bottom: 1.2rem;
}

.stat-box {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 16px;
    padding: 0.9rem 0.6rem;
    text-align: center;
}
.stat-box .label { font-size: 0.72rem; color: #a6a1c9; text-transform: uppercase; letter-spacing: 1px; }
.stat-box .value { font-family: 'Orbitron', sans-serif; font-size: 1.5rem; font-weight: 700; color: #fff; margin-top: 0.15rem; }

.progress-track {
    height: 10px;
    border-radius: 999px;
    background: rgba(255,255,255,0.08);
    overflow: hidden;
    margin-bottom: 0.4rem;
}
.progress-fill {
    height: 100%;
    border-radius: 999px;
    background: linear-gradient(90deg, #7f5af0, #2cb67d);
    transition: width 0.4s ease;
}

.category-badge {
    display: inline-block;
    padding: 0.4rem 1.1rem;
    border-radius: 999px;
    background: linear-gradient(90deg, rgba(127,90,240,0.25), rgba(44,182,125,0.25));
    border: 1px solid rgba(255,255,255,0.15);
    font-size: 0.8rem;
    font-weight: 600;
    letter-spacing: 0.5px;
    color: #fff;
    margin-bottom: 0.8rem;
}

.question-text {
    font-size: 1.25rem;
    font-weight: 600;
    color: #fff;
    margin: 0.6rem 0 1.2rem 0;
    line-height: 1.5;
}

.feedback {
    text-align: center;
    font-size: 1.1rem;
    font-weight: 600;
    padding: 0.8rem;
    border-radius: 14px;
    margin: 0.8rem 0;
    animation: pop 0.25s ease-out;
}
@keyframes pop {
    0% { transform: scale(0.9); opacity: 0; }
    100% { transform: scale(1); opacity: 1; }
}
.fb-correct { background: rgba(44, 182, 125, 0.18); border: 1px solid rgba(44,182,125,0.45); color: #7bf0bd; }
.fb-wrong   { background: rgba(255, 88, 88, 0.15); border: 1px solid rgba(255,88,88,0.4); color: #ff9d9d; }

.result-score {
    text-align: center;
    font-family: 'Orbitron', sans-serif;
    font-size: 3rem;
    font-weight: 900;
    background: linear-gradient(90deg, #7f5af0, #2cb67d, #ff8906);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin: 0.6rem 0;
}

.result-grade {
    text-align: center;
    font-size: 1.1rem;
    color: #a6a1c9;
    margin-bottom: 1rem;
}

.stButton>button {
    width: 100%;
    border-radius: 12px;
    background: linear-gradient(90deg, #7f5af0, #5c3fd6);
    color: white;
    border: none;
    padding: 0.65rem 0;
    font-weight: 600;
    font-size: 1rem;
    transition: transform 0.15s ease, box-shadow 0.15s ease;
    margin-bottom: 0.5rem;
}
.stButton>button:hover { transform: translateY(-2px); box-shadow: 0 6px 18px rgba(127,90,240,0.4); }

.stTextInput input {
    border-radius: 12px !important;
    background: rgba(255,255,255,0.07) !important;
    color: #fff !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
}

.stRadio > label { display: none; }
.stRadio [role="radiogroup"] > label {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.14);
    border-radius: 12px;
    padding: 0.7rem 1rem;
    margin-bottom: 0.5rem;
    width: 100%;
    transition: background 0.15s ease, border 0.15s ease;
}
.stRadio [role="radiogroup"] > label:hover {
    background: rgba(127,90,240,0.15);
    border: 1px solid rgba(127,90,240,0.4);
}
</style>
""", unsafe_allow_html=True)

# ----------------------------- SESSION STATE -----------------------------
if "screen" not in st.session_state:
    st.session_state.screen = "welcome"
    st.session_state.name = ""
    st.session_state.category_name = ""
    st.session_state.quiz_questions = []
    st.session_state.q_index = 0
    st.session_state.correct_score = 0
    st.session_state.wrong_score = 0
    st.session_state.feedback = None
    st.session_state.answered = False

def start_quiz(name, category_name):
    pool = CATEGORIES[category_name]
    st.session_state.name = name
    st.session_state.category_name = category_name
    st.session_state.quiz_questions = random.sample(pool, QUESTIONS_PER_QUIZ)
    st.session_state.q_index = 0
    st.session_state.correct_score = 0
    st.session_state.wrong_score = 0
    st.session_state.feedback = None
    st.session_state.answered = False
    st.session_state.screen = "quiz"

def restart():
    for key in ["screen", "name", "category_name", "quiz_questions", "q_index",
                "correct_score", "wrong_score", "feedback", "answered"]:
        if key in st.session_state:
            del st.session_state[key]

# ----------------------------- HERO -----------------------------
st.markdown("""
<div class="hero">
    <h1>❓ QUIZVERSE</h1>
    <p>Test your knowledge across the arena. Speed and accuracy win the crown.</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="glass-card">', unsafe_allow_html=True)

# ----------------------------- WELCOME SCREEN -----------------------------
if st.session_state.screen == "welcome":
    st.subheader("Enter the Arena")
    name_input = st.text_input("What should we call you?", placeholder="Your name")

    st.markdown("#### Choose your battlefield")
    category_choice = st.radio(
        "Category",
        list(CATEGORIES.keys()),
        label_visibility="collapsed",
    )

    if st.button("⚔️ Start Quiz"):
        if not name_input.strip():
            st.warning("Please enter your name to begin.")
        else:
            start_quiz(name_input.strip(), category_choice)
            st.rerun()

# ----------------------------- QUIZ SCREEN -----------------------------
elif st.session_state.screen == "quiz":
    idx = st.session_state.q_index
    total = len(st.session_state.quiz_questions)

    progress_pct = int((idx / total) * 100)
    st.markdown(f"""
    <div class="progress-track"><div class="progress-fill" style="width:{progress_pct}%;"></div></div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"<div class='stat-box'><div class='label'>Question</div>"
                    f"<div class='value'>{idx+1}/{total}</div></div>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<div class='stat-box'><div class='label'>Correct</div>"
                    f"<div class='value'>{st.session_state.correct_score}</div></div>", unsafe_allow_html=True)
    with col3:
        st.markdown(f"<div class='stat-box'><div class='label'>Wrong</div>"
                    f"<div class='value'>{st.session_state.wrong_score}</div></div>", unsafe_allow_html=True)

    st.write("")
    st.markdown(f"<span class='category-badge'>{st.session_state.category_name}</span>", unsafe_allow_html=True)

    q = st.session_state.quiz_questions[idx]
    st.markdown(f"<div class='question-text'>Q{idx+1}. {q['question']}</div>", unsafe_allow_html=True)

    if not st.session_state.answered:
        selected = st.radio("Options", q["options"], label_visibility="collapsed", key=f"opt_{idx}")

        if st.button("✅ Submit Answer"):
            st.session_state.answered = True
            if selected == q["answer"]:
                st.session_state.feedback = "correct"
                st.session_state.correct_score += 1
            else:
                st.session_state.feedback = "wrong"
                st.session_state.wrong_score += 1
            st.rerun()
    else:
        if st.session_state.feedback == "correct":
            st.markdown("<div class='feedback fb-correct'>✅ Correct answer!</div>", unsafe_allow_html=True)
        else:
            st.markdown(
                f"<div class='feedback fb-wrong'>❌ Wrong! The correct answer is <b>{q['answer']}</b></div>",
                unsafe_allow_html=True,
            )

        next_label = "➡️ Next Question" if idx + 1 < total else "🏁 Finish Quiz"
        if st.button(next_label):
            st.session_state.q_index += 1
            st.session_state.answered = False
            st.session_state.feedback = None
            if st.session_state.q_index >= total:
                st.session_state.screen = "result"
            st.rerun()

# ----------------------------- RESULT SCREEN -----------------------------
elif st.session_state.screen == "result":
    total = len(st.session_state.quiz_questions)
    correct = st.session_state.correct_score
    percentage = round((correct / total) * 100, 1)

    if percentage >= 80:
        grade = "🏆 Quiz Master!"
    elif percentage >= 60:
        grade = "🥈 Great Effort!"
    elif percentage >= 40:
        grade = "🥉 Not Bad, Keep Practicing!"
    else:
        grade = "📘 Time to Review the Basics!"

    st.balloons()
    st.markdown(f"<h3 style='text-align:center;'>Well played, {st.session_state.name}!</h3>", unsafe_allow_html=True)
    st.markdown(f"<div class='result-score'>{percentage}%</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='result-grade'>{grade}</div>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"<div class='stat-box'><div class='label'>Total</div>"
                    f"<div class='value'>{total}</div></div>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<div class='stat-box'><div class='label'>Correct</div>"
                    f"<div class='value'>{correct}</div></div>", unsafe_allow_html=True)
    with col3:
        st.markdown(f"<div class='stat-box'><div class='label'>Wrong</div>"
                    f"<div class='value'>{st.session_state.wrong_score}</div></div>", unsafe_allow_html=True)

    st.write("")
    if st.button("🔁 Play Again"):
        restart()
        st.rerun()

st.markdown('</div>', unsafe_allow_html=True)

st.markdown(
    "<p style='text-align:center; color:#605b82; font-size:0.78rem;'>"
    "Built with Streamlit • QuizVerse v1.0</p>",
    unsafe_allow_html=True,
)
