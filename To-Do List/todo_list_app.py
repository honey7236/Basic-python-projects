"""
Project #6 - 📋 To-Do List
Lists, loops, CRUD operations -> Streamlit UI
"""

import streamlit as st
from pathlib import Path

st.set_page_config(page_title="To-Do List", page_icon="📋", layout="wide")

# ---------------------------------------------------------
# DATA FOLDER (sandboxed workspace for CRUD)
# ---------------------------------------------------------
DATA_DIR = Path("todo_lists")
DATA_DIR.mkdir(exist_ok=True)

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

section[data-testid="stSidebar"] {
    background: rgba(15, 12, 41, 0.9);
    border-right: 1px solid rgba(255,255,255,0.08);
}

.block-container {
    padding-top: 2rem;
    max-width: 900px;
}

.glass-card {
    background: rgba(255, 255, 255, 0.06);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 1px solid rgba(255, 255, 255, 0.12);
    border-radius: 22px;
    padding: 2rem;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.35);
    margin-bottom: 1.5rem;
}

.title-text {
    text-align: center;
    font-size: 2.3rem;
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
    margin-bottom: 1.5rem;
}

.sidebar-title {
    color: #e9d5ff;
    font-weight: 700;
    font-size: 1.1rem;
    margin-bottom: 0.5rem;
}

.task-row {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 12px;
    padding: 0.6rem 1rem;
    margin-bottom: 0.5rem;
    display: flex;
    align-items: center;
}

.task-done {
    text-decoration: line-through;
    color: rgba(255,255,255,0.35) !important;
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
    font-size: 0.75rem;
    color: rgba(255,255,255,0.5);
    text-transform: uppercase;
    letter-spacing: 1px;
}

div.stButton > button {
    background: linear-gradient(90deg, #7c3aed, #ec4899);
    color: white;
    border: none;
    border-radius: 12px;
    padding: 0.5rem 0;
    font-weight: 700;
    letter-spacing: 0.5px;
    transition: transform 0.15s ease, box-shadow 0.15s ease;
    box-shadow: 0 4px 16px rgba(124, 58, 237, 0.35);
}

div.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(236, 72, 153, 0.45);
}

.danger-btn button {
    background: linear-gradient(90deg, #ef4444, #b91c1c) !important;
    box-shadow: 0 4px 16px rgba(239, 68, 68, 0.35) !important;
}

.ghost-btn button {
    background: rgba(255,255,255,0.08) !important;
    box-shadow: none !important;
}

.empty-state {
    text-align: center;
    color: rgba(255,255,255,0.35);
    padding: 2rem 0;
    font-size: 0.95rem;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# HELPERS (mirrors original CRUD functions)
# ---------------------------------------------------------
def list_all_lists():
    return sorted([p.stem for p in DATA_DIR.glob("*.txt")])

def get_path(name: str) -> Path:
    return DATA_DIR / f"{name}.txt"

def read_tasks(name: str):
    path = get_path(name)
    if not path.exists():
        return []
    lines = path.read_text().splitlines()
    return [line for line in lines if line.strip() != ""]

def write_tasks(name: str, tasks: list):
    path = get_path(name)
    with open(path, "w") as fs:
        for t in tasks:
            fs.write(t + "\n")

def create_list(name: str):
    path = get_path(name)
    if path.exists():
        return False, "A list with this name already exists."
    path.touch()
    return True, "List created successfully."

def delete_list(name: str):
    path = get_path(name)
    if path.exists():
        path.unlink()
        return True
    return False

# Tasks are stored as "DONE|task text" or "TODO|task text"
def parse_task(raw: str):
    if "|" in raw:
        status, text = raw.split("|", 1)
        return status == "DONE", text
    return False, raw

def format_task(done: bool, text: str):
    return f"{'DONE' if done else 'TODO'}|{text}"

# ---------------------------------------------------------
# SESSION STATE
# ---------------------------------------------------------
if "selected_list" not in st.session_state:
    st.session_state.selected_list = None

# ---------------------------------------------------------
# SIDEBAR - list navigation + create/delete
# ---------------------------------------------------------
with st.sidebar:
    st.markdown('<div class="sidebar-title">📋 Your Lists</div>', unsafe_allow_html=True)

    all_lists = list_all_lists()

    if all_lists:
        for lst in all_lists:
            is_selected = st.session_state.selected_list == lst
            label = f"📂 {lst}" if is_selected else f"📄 {lst}"
            if st.button(label, key=f"select_{lst}", use_container_width=True):
                st.session_state.selected_list = lst
                st.rerun()
    else:
        st.markdown('<div class="empty-state">No lists yet.<br>Create one below 👇</div>', unsafe_allow_html=True)

    st.markdown("---")
    st.markdown('<div class="sidebar-title">➕ New List</div>', unsafe_allow_html=True)
    new_list_name = st.text_input("List name", key="new_list_input", label_visibility="collapsed", placeholder="e.g. Groceries")
    if st.button("Create List", use_container_width=True):
        if new_list_name.strip() == "":
            st.warning("Enter a name first.")
        else:
            success, msg = create_list(new_list_name.strip())
            if success:
                st.session_state.selected_list = new_list_name.strip()
                st.success(msg)
                st.rerun()
            else:
                st.error(msg)

# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------
st.markdown('<div class="title-text">📋 To-Do List Manager</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle-text">Lists &nbsp;•&nbsp; Loops &nbsp;•&nbsp; CRUD Operations &nbsp;•&nbsp; Streamlit UI</div>', unsafe_allow_html=True)

# ---------------------------------------------------------
# MAIN PANEL
# ---------------------------------------------------------
selected = st.session_state.selected_list

if selected is None or not get_path(selected).exists():
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<div class="empty-state">👈 Select a list from the sidebar, or create a new one to get started.</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
else:
    raw_tasks = read_tasks(selected)
    parsed_tasks = [parse_task(t) for t in raw_tasks]

    # ---- Header row: name + delete list button ----
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    col_title, col_del = st.columns([5, 1])
    with col_title:
        st.markdown(f"### 📂 {selected}")
    with col_del:
        st.markdown('<div class="danger-btn">', unsafe_allow_html=True)
        if st.button("🗑️ Delete", key="delete_list_btn", use_container_width=True):
            delete_list(selected)
            st.session_state.selected_list = None
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    # ---- Add task ----
    with st.form(key="add_task_form", clear_on_submit=True):
        col_input, col_add = st.columns([5, 1])
        with col_input:
            new_task = st.text_input("Add task", label_visibility="collapsed", placeholder="Add a new task...")
        with col_add:
            submitted = st.form_submit_button("➕ Add", use_container_width=True)
        if submitted and new_task.strip() != "":
            parsed_tasks.append((False, new_task.strip()))
            write_tasks(selected, [format_task(d, t) for d, t in parsed_tasks])
            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

    # ---- Stats ----
    total = len(parsed_tasks)
    done_count = sum(1 for d, _ in parsed_tasks if d)
    pending = total - done_count

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    for col, label, value in zip([c1, c2, c3], ["Total Tasks", "Completed", "Pending"], [total, done_count, pending]):
        with col:
            st.markdown(
                f'<div class="stat-box"><div class="stat-value">{value}</div>'
                f'<div class="stat-label">{label}</div></div>',
                unsafe_allow_html=True,
            )
    if total > 0:
        st.progress(done_count / total)
    st.markdown('</div>', unsafe_allow_html=True)

    # ---- Task list ----
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    if total == 0:
        st.markdown('<div class="empty-state">No tasks yet. Add your first one above ☝️</div>', unsafe_allow_html=True)
    else:
        for i, (done, text) in enumerate(parsed_tasks):
            col_check, col_text, col_del_task = st.columns([0.5, 6, 1])
            with col_check:
                new_done = st.checkbox("", value=done, key=f"check_{selected}_{i}")
            with col_text:
                css_class = "task-done" if done else ""
                st.markdown(f'<div class="{css_class}" style="padding-top:6px;">{text}</div>', unsafe_allow_html=True)
            with col_del_task:
                if st.button("✖", key=f"del_{selected}_{i}"):
                    parsed_tasks.pop(i)
                    write_tasks(selected, [format_task(d, t) for d, t in parsed_tasks])
                    st.rerun()

            if new_done != done:
                parsed_tasks[i] = (new_done, text)
                write_tasks(selected, [format_task(d, t) for d, t in parsed_tasks])
                st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

st.markdown(
    '<div style="text-align:center; color:rgba(255,255,255,0.3); font-size:0.8rem;">'
    'Project #6 &nbsp;|&nbsp; Built with Python + Streamlit</div>',
    unsafe_allow_html=True,
)
