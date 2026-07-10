"""
Project #1 - 🧮 Calculator
Input, operators, functions, if-else -> Streamlit UI
"""

import streamlit as st

st.set_page_config(page_title="Calculator", page_icon="🧮", layout="centered")

# ---------------------------------------------------------
# CORE FUNCTIONS (same logic as original)
# ---------------------------------------------------------
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def multi(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

OPERATIONS = {
    "+": ("Addition", add, "➕"),
    "-": ("Subtraction", sub, "➖"),
    "×": ("Multiplication", multi, "✖️"),
    "÷": ("Division", div, "➗"),
}

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
    max-width: 640px;
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

.result-display {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(167, 139, 250, 0.3);
    border-radius: 18px;
    padding: 1.6rem;
    text-align: center;
    margin-top: 1rem;
}

.result-expr {
    color: rgba(255,255,255,0.5);
    font-size: 1.1rem;
    margin-bottom: 0.3rem;
}

.result-value {
    font-size: 2.6rem;
    font-weight: 800;
    color: #facc15;
    word-break: break-all;
}

.error-text {
    color: #f87171;
    font-size: 1.2rem;
    font-weight: 700;
    text-align: center;
}

.history-row {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 10px;
    padding: 0.5rem 1rem;
    margin-bottom: 0.4rem;
    font-size: 0.95rem;
    color: rgba(255,255,255,0.75);
    display: flex;
    justify-content: space-between;
}

.op-label {
    color: #a78bfa;
    font-weight: 700;
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
    letter-spacing: 0.5px;
    transition: transform 0.15s ease, box-shadow 0.15s ease;
    box-shadow: 0 4px 18px rgba(124, 58, 237, 0.4);
}

div.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 24px rgba(236, 72, 153, 0.5);
}

.ghost-btn button {
    background: rgba(255,255,255,0.08) !important;
    box-shadow: none !important;
}

/* Operator toggle buttons */
div[data-testid="stHorizontalBlock"] div.stButton > button {
    font-size: 1.3rem;
    padding: 0.6rem 0;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# SESSION STATE
# ---------------------------------------------------------
if "history" not in st.session_state:
    st.session_state.history = []
if "selected_op" not in st.session_state:
    st.session_state.selected_op = "+"
if "result" not in st.session_state:
    st.session_state.result = None
if "error" not in st.session_state:
    st.session_state.error = None

# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------
st.markdown('<div class="title-text">🧮 Calculator</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle-text">Functions &nbsp;•&nbsp; Operators &nbsp;•&nbsp; Streamlit UI</div>', unsafe_allow_html=True)

# ---------------------------------------------------------
# INPUT CARD
# ---------------------------------------------------------
st.markdown('<div class="glass-card">', unsafe_allow_html=True)

col_a, col_b = st.columns(2)
with col_a:
    num_a = st.number_input("First number", value=0.0, format="%g", key="num_a")
with col_b:
    num_b = st.number_input("Second number", value=0.0, format="%g", key="num_b")

st.markdown('<div style="margin-top:0.8rem; margin-bottom:0.4rem; color:rgba(255,255,255,0.55); font-size:0.9rem;">Choose operation</div>', unsafe_allow_html=True)

op_cols = st.columns(4)
for col, symbol in zip(op_cols, OPERATIONS.keys()):
    with col:
        is_selected = st.session_state.selected_op == symbol
        label = f"🟣 {symbol}" if is_selected else symbol
        if st.button(label, key=f"op_{symbol}"):
            st.session_state.selected_op = symbol
            st.rerun()

st.markdown("<br>", unsafe_allow_html=True)

calc_clicked = st.button("🟰 Calculate", use_container_width=True)

if calc_clicked:
    symbol = st.session_state.selected_op
    name, func, emoji = OPERATIONS[symbol]
    try:
        result = func(num_a, num_b)
        st.session_state.result = result
        st.session_state.error = None
        st.session_state.history.insert(0, {
            "expr": f"{num_a:g} {symbol} {num_b:g}",
            "result": result,
        })
        st.session_state.history = st.session_state.history[:10]
    except ZeroDivisionError:
        st.session_state.result = None
        st.session_state.error = "Cannot divide by zero."

# ---- Result display ----
if st.session_state.error:
    st.markdown(f'<div class="result-display"><div class="error-text">⚠️ {st.session_state.error}</div></div>', unsafe_allow_html=True)
elif st.session_state.result is not None:
    symbol = st.session_state.selected_op
    expr = f"{num_a:g} {symbol} {num_b:g} ="
    val = st.session_state.result
    val_display = f"{val:g}" if isinstance(val, float) else str(val)
    st.markdown(
        f'<div class="result-display">'
        f'<div class="result-expr">{expr}</div>'
        f'<div class="result-value">{val_display}</div>'
        f'</div>',
        unsafe_allow_html=True,
    )
else:
    st.markdown(
        '<div class="result-display"><div class="result-expr" style="color:rgba(255,255,255,0.35);">'
        'Pick numbers and an operation, then hit Calculate</div></div>',
        unsafe_allow_html=True,
    )

st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------------------------------------
# HISTORY CARD
# ---------------------------------------------------------
if st.session_state.history:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    col_title, col_clear = st.columns([4, 1])
    with col_title:
        st.markdown('<div class="subtitle-text" style="margin-bottom:0.8rem; text-align:left;">🕘 Recent Calculations</div>', unsafe_allow_html=True)
    with col_clear:
        st.markdown('<div class="ghost-btn">', unsafe_allow_html=True)
        if st.button("Clear", key="clear_history"):
            st.session_state.history = []
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    for item in st.session_state.history:
        val = item["result"]
        val_display = f"{val:g}" if isinstance(val, float) else str(val)
        st.markdown(
            f'<div class="history-row"><span>{item["expr"]}</span>'
            f'<span class="op-label">{val_display}</span></div>',
            unsafe_allow_html=True,
        )

    st.markdown('</div>', unsafe_allow_html=True)

st.markdown(
    '<div style="text-align:center; color:rgba(255,255,255,0.3); font-size:0.8rem;">'
    'Project #1 &nbsp;|&nbsp; Built with Python + Streamlit</div>',
    unsafe_allow_html=True,
)
