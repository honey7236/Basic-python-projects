import streamlit as st
from pathlib import Path
from datetime import datetime

# ----------------------------- CONFIG -----------------------------
st.set_page_config(page_title="Notes Vault", page_icon="📝", layout="centered")

NOTES_DIR = Path("notes")
NOTES_DIR.mkdir(exist_ok=True)

# ----------------------------- STYLING -----------------------------
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
        color: #e8e8f0;
    }

    #MainMenu, footer, header {visibility: hidden;}

    .block-container {
        padding-top: 2.5rem;
        max-width: 720px;
    }

    .title-box {
        text-align: center;
        margin-bottom: 1.8rem;
    }
    .title-box h1 {
        font-size: 2.3rem;
        font-weight: 700;
        background: linear-gradient(90deg, #a78bfa, #60a5fa);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.2rem;
    }
    .title-box p {
        color: #a3a3c2;
        font-size: 0.95rem;
    }

    .glass-card {
        background: rgba(255, 255, 255, 0.06);
        backdrop-filter: blur(14px);
        -webkit-backdrop-filter: blur(14px);
        border: 1px solid rgba(255, 255, 255, 0.12);
        border-radius: 18px;
        padding: 1.8rem 1.8rem 1.4rem 1.8rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.35);
        margin-bottom: 1.5rem;
    }

    .note-preview {
        background: rgba(0, 0, 0, 0.25);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 12px;
        padding: 1rem 1.2rem;
        font-family: 'Courier New', monospace;
        white-space: pre-wrap;
        color: #d6d6ee;
        max-height: 300px;
        overflow-y: auto;
    }

    .stTextInput input, .stTextArea textarea {
        background: rgba(255, 255, 255, 0.07) !important;
        color: #f0f0fa !important;
        border: 1px solid rgba(255, 255, 255, 0.15) !important;
        border-radius: 10px !important;
    }

    .stTextInput input:focus, .stTextArea textarea:focus {
        border: 1px solid #a78bfa !important;
        box-shadow: 0 0 0 1px #a78bfa !important;
    }

    .stButton button {
        background: linear-gradient(90deg, #7c3aed, #4f46e5);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.55rem 1.3rem;
        font-weight: 600;
        transition: all 0.2s ease;
        width: 100%;
    }
    .stButton button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 18px rgba(124, 58, 237, 0.4);
    }

    .stRadio > label, .stSelectbox > label, .stTextInput > label, .stTextArea > label {
        color: #c9c9e6 !important;
        font-weight: 500;
    }

    div[role="radiogroup"] {
        gap: 0.4rem;
    }

    .empty-state {
        text-align: center;
        color: #8888aa;
        padding: 2rem 0;
        font-size: 0.95rem;
    }

    .stAlert {
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

# ----------------------------- HELPERS -----------------------------
def list_notes():
    return sorted([f.name for f in NOTES_DIR.iterdir() if f.is_file()])

def note_path(name: str) -> Path:
    return NOTES_DIR / name

# ----------------------------- HEADER -----------------------------
st.markdown("""
<div class="title-box">
    <h1>📝 Notes Vault</h1>
    <p>Create, read, update and delete your notes — minimal and fast.</p>
</div>
""", unsafe_allow_html=True)

# ----------------------------- NAVIGATION -----------------------------
action = st.radio(
    "Choose an action",
    ["Create", "Read", "Update", "Delete"],
    horizontal=True,
    label_visibility="collapsed",
)

st.markdown("<br>", unsafe_allow_html=True)

# ----------------------------- CREATE -----------------------------
if action == "Create":
    with st.container():
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.subheader("Create a new note")
        name = st.text_input("File name", placeholder="e.g. ideas.txt")
        content = st.text_area("Note content", height=180, placeholder="Write your note here...")

        if st.button("Create Note"):
            if not name.strip():
                st.warning("Please enter a file name.")
            else:
                path = note_path(name.strip())
                if path.exists():
                    st.error("A file with this name already exists.")
                else:
                    try:
                        path.write_text(content)
                        st.success(f"Note '{name}' created successfully.")
                    except Exception as e:
                        st.error(f"There was an error: {e}")
        st.markdown('</div>', unsafe_allow_html=True)

# ----------------------------- READ -----------------------------
elif action == "Read":
    notes = list_notes()
    with st.container():
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.subheader("Read a note")
        if not notes:
            st.markdown('<div class="empty-state">No notes yet. Create one to get started.</div>', unsafe_allow_html=True)
        else:
            selected = st.selectbox("Select a note", notes)
            if selected:
                try:
                    data = note_path(selected).read_text()
                    st.markdown(f'<div class="note-preview">{data if data.strip() else "(empty file)"}</div>', unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"There was an error: {e}")
        st.markdown('</div>', unsafe_allow_html=True)

# ----------------------------- UPDATE -----------------------------
elif action == "Update":
    notes = list_notes()
    with st.container():
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.subheader("Update a note")
        if not notes:
            st.markdown('<div class="empty-state">No notes yet. Create one to get started.</div>', unsafe_allow_html=True)
        else:
            selected = st.selectbox("Select a note", notes)
            mode = st.radio("Update mode", ["Append", "Overwrite"], horizontal=True)
            new_text = st.text_area("Text", height=150, placeholder="What do you want to write?")

            if st.button("Save changes"):
                path = note_path(selected)
                try:
                    if mode == "Append":
                        with open(path, "a") as fs:
                            fs.write("\n" + new_text)
                        st.success("Note appended successfully.")
                    else:
                        path.write_text(new_text)
                        st.success("Note overwritten successfully.")
                except Exception as e:
                    st.error(f"There was an error: {e}")
        st.markdown('</div>', unsafe_allow_html=True)

# ----------------------------- DELETE -----------------------------
elif action == "Delete":
    notes = list_notes()
    with st.container():
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.subheader("Delete a note")
        if not notes:
            st.markdown('<div class="empty-state">No notes yet. Nothing to delete.</div>', unsafe_allow_html=True)
        else:
            selected = st.selectbox("Select a note to delete", notes)
            confirm = st.checkbox(f"I confirm I want to permanently delete '{selected}'")
            if st.button("Delete Note"):
                if not confirm:
                    st.warning("Please confirm deletion before proceeding.")
                else:
                    try:
                        note_path(selected).unlink()
                        st.success(f"'{selected}' deleted successfully.")
                        st.rerun()
                    except Exception as e:
                        st.error(f"There was an error: {e}")
        st.markdown('</div>', unsafe_allow_html=True)

# ----------------------------- FOOTER -----------------------------
st.markdown(
    f"<p style='text-align:center; color:#6b6b8a; font-size:0.8rem; margin-top:2rem;'>"
    f"{len(list_notes())} note(s) stored · Notes Vault</p>",
    unsafe_allow_html=True,
)
