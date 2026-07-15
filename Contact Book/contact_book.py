import json
from pathlib import Path

import streamlit as st

DATABASE = Path(__file__).with_name("contact.json")


def load_contacts():
    if DATABASE.exists():
        with open(DATABASE, "r", encoding="utf-8") as file:
            content = file.read().strip()
            if content:
                return json.loads(content)
    return []


def save_contacts(contacts):
    with open(DATABASE, "w", encoding="utf-8") as file:
        json.dump(contacts, file, indent=4)


def load_data():
    return load_contacts()


def save_data(contacts):
    save_contacts(contacts)


def add_contact(name, contact):
    if not str(name).strip():
        return False

    try:
        number = int(contact)
    except (TypeError, ValueError):
        return False

    contacts = load_contacts()
    contacts.append({"name": str(name).strip(), "contact": number})
    save_contacts(contacts)
    return True


def search_contact(query):
    term = str(query).strip().lower()
    if not term:
        return []

    return [contact for contact in load_contacts() if term in contact["name"].lower()]


def delete_contact(name):
    contacts = load_contacts()
    target = str(name).strip().lower()

    for index, contact in enumerate(contacts):
        if contact["name"].lower() == target:
            removed = contacts.pop(index)
            save_contacts(contacts)
            return removed

    return None


st.set_page_config(
    page_title="ContactVault | Smart Contact Book",
    page_icon="📖",
    layout="centered",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700;900&family=Poppins:wght@300;400;500;600&display=swap');
    html, body, [class*="css"] { font-family: 'Poppins', sans-serif; }
    .stApp { background: radial-gradient(circle at 20% 20%, #1b1035 0%, #0a0518 45%, #05030d 100%); color: #eae6ff; }
    #MainMenu, footer, header { visibility: hidden; }
    .hero { text-align: center; padding: 1.4rem 1rem 1rem 1rem; }
    .hero h1 { font-family: 'Orbitron', sans-serif; font-weight: 900; font-size: 2.5rem; background: linear-gradient(90deg, #7f5af0, #2cb67d, #ff8906); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 0.2rem; letter-spacing: 1px; }
    .hero p { color: #a6a1c9; font-size: 0.95rem; margin-top: 0; }
    .glass-card { background: rgba(255,255,255,0.06); border: 1px solid rgba(255,255,255,0.12); border-radius: 20px; padding: 1.6rem; backdrop-filter: blur(14px); box-shadow: 0 8px 32px rgba(0,0,0,0.45); margin-bottom: 1.2rem; }
    .stat-box { background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); border-radius: 16px; padding: 0.9rem 0.6rem; text-align: center; }
    .stat-box .label { font-size: 0.72rem; color: #a6a1c9; text-transform: uppercase; letter-spacing: 1px; }
    .stat-box .value { font-family: 'Orbitron', sans-serif; font-size: 1.5rem; font-weight: 700; color: #fff; margin-top: 0.15rem; }
    .contact-card { background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.12); border-radius: 16px; padding: 0.9rem 1.1rem; margin-bottom: 0.7rem; display: flex; align-items: center; justify-content: space-between; transition: transform 0.15s ease, box-shadow 0.15s ease; }
    .contact-card:hover { transform: translateY(-2px); box-shadow: 0 6px 18px rgba(127,90,240,0.25); }
    .contact-avatar { width: 42px; height: 42px; border-radius: 50%; background: linear-gradient(135deg, #7f5af0, #2cb67d); display: flex; align-items: center; justify-content: center; font-weight: 700; font-family: 'Orbitron', sans-serif; color: #fff; margin-right: 0.9rem; flex-shrink: 0; }
    .contact-name { font-weight: 600; font-size: 1rem; color: #fff; }
    .contact-number { color: #a6a1c9; font-size: 0.85rem; }
    .msg-success { background: rgba(44, 182, 125, 0.15); border: 1px solid rgba(44,182,125,0.4); color: #7bf0bd; padding: 0.7rem 1rem; border-radius: 12px; text-align: center; font-weight: 600; margin-bottom: 0.8rem; }
    .msg-error { background: rgba(255, 88, 88, 0.15); border: 1px solid rgba(255,88,88,0.4); color: #ff9d9d; padding: 0.7rem 1rem; border-radius: 12px; text-align: center; font-weight: 600; margin-bottom: 0.8rem; }
    .stButton>button { width: 100%; border-radius: 12px; background: linear-gradient(90deg, #7f5af0, #5c3fd6); color: white; border: none; padding: 0.6rem 0; font-weight: 600; font-size: 1rem; transition: transform 0.15s ease, box-shadow 0.15s ease; }
    .stButton>button:hover { transform: translateY(-2px); box-shadow: 0 6px 18px rgba(127,90,240,0.4); }
    .stTextInput input, .stTextInput>div>div>input { border-radius: 12px !important; background: rgba(255,255,255,0.07) !important; color: #fff !important; border: 1px solid rgba(255,255,255,0.15) !important; }
    </style>
    """,
    unsafe_allow_html=True,
)


if "contacts" not in st.session_state:
    st.session_state.contacts = load_contacts()
if "message" not in st.session_state:
    st.session_state.message = None

with st.sidebar:
    st.markdown("### ⚙️ Actions")
    menu = st.radio("Choose an action", ["📇 View All", "➕ Add Contact", "🔍 Search", "🗑️ Delete"])
    st.markdown("---")
    st.markdown("### 📊 Stats")
    st.markdown(
        f"<div class='stat-box'><div class='label'>Total Contacts</div><div class='value'>{len(st.session_state.contacts)}</div></div>",
        unsafe_allow_html=True,
    )

st.markdown(
    """
    <div class="hero">
        <h1>📖 CONTACTVAULT</h1>
        <p>Your people, organized and always one search away.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="glass-card">', unsafe_allow_html=True)

if st.session_state.message:
    css_class = "msg-success" if st.session_state.message[0] == "ok" else "msg-error"
    st.markdown(f"<div class='{css_class}'>{st.session_state.message[1]}</div>", unsafe_allow_html=True)
    st.session_state.message = None

if menu == "➕ Add Contact":
    st.subheader("Add a New Contact")
    with st.form("add_form", clear_on_submit=True):
        name = st.text_input("Name")
        contact = st.text_input("Contact Number")
        submitted = st.form_submit_button("💾 Save Contact")

    if submitted:
        if not name.strip():
            st.session_state.message = ("err", "⚠️ Name cannot be empty.")
        elif not contact.strip().isdigit():
            st.session_state.message = ("err", "⚠️ Contact number must be numeric.")
        else:
            st.session_state.contacts.append({"name": name.strip(), "contact": int(contact.strip())})
            save_contacts(st.session_state.contacts)
            st.session_state.message = ("ok", f"✅ Contact '{name.strip()}' saved successfully!")
        st.rerun()

elif menu == "🔍 Search":
    st.subheader("Search a Contact")
    query = st.text_input("Enter name to search")
    if query:
        results = search_contact(query)
        if results:
            for contact in results:
                initials = contact["name"][:2].upper()
                st.markdown(
                    f"""
                    <div class="contact-card">
                        <div style="display:flex; align-items:center;">
                            <div class="contact-avatar">{initials}</div>
                            <div>
                                <div class="contact-name">{contact['name']}</div>
                                <div class="contact-number">📞 {contact['contact']}</div>
                            </div>
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
        else:
            st.info("No matching contact found.")

elif menu == "🗑️ Delete":
    st.subheader("Delete a Contact")
    if st.session_state.contacts:
        names = [f"{contact['name']} ({contact['contact']})" for contact in st.session_state.contacts]
        idx = st.selectbox("Select a contact to delete", range(len(names)), format_func=lambda i: names[i])
        if st.button("🗑️ Delete Selected Contact"):
            removed = st.session_state.contacts.pop(idx)
            save_contacts(st.session_state.contacts)
            st.session_state.message = ("ok", f"🗑️ Deleted '{removed['name']}'.")
            st.rerun()
    else:
        st.info("No contacts to delete yet.")

else:
    st.subheader("All Contacts")
    if st.session_state.contacts:
        for contact in st.session_state.contacts:
            initials = contact["name"][:2].upper()
            st.markdown(
                f"""
                <div class="contact-card">
                    <div style="display:flex; align-items:center;">
                        <div class="contact-avatar">{initials}</div>
                        <div>
                            <div class="contact-name">{contact['name']}</div>
                            <div class="contact-number">📞 {contact['contact']}</div>
                        </div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
    else:
        st.info("Your contact book is empty. Add your first contact from the sidebar!")

st.markdown('</div>', unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#605b82; font-size:0.78rem;'>Built with Streamlit • ContactVault v1.0</p>", unsafe_allow_html=True)

