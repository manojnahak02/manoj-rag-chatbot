import personal_code
from personal_code import llm_response
import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Manoj Nahak BOT",
    page_icon="🤖",
    layout="wide"
)

# ---------------- HEADER ----------------
col1, col2 = st.columns([1, 10])

with col1:
    st.image("manoj_image.jpg", width=60)

with col2:
    st.markdown("## Manoj Nahak BOT")

# ---------------- DARK UI ----------------
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background-color: #0f172a !important;
    color: #f1f5f9 !important;
}

div[data-testid="stChatMessage"] {
    border-radius: 16px;
    padding: 14px !important;
    margin-bottom: 12px;
    max-width: 75%;
}

div[data-testid="stChatMessage"][data-author="user"] {
    background: linear-gradient(135deg, #22c55e, #16a34a) !important;
    color: white !important;
    margin-left: auto;
}

div[data-testid="stChatMessage"][data-author="assistant"] {
    background: #1e293b !important;
    color: #f1f5f9 !important;
    margin-right: auto;
    border: 1px solid #334155;
}

section[data-testid="stSidebar"] {
    background-color: #020617 !important;
}

textarea {
    background-color: #1e293b !important;
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

# ---------------- SESSION STATE ----------------
if "conversations" not in st.session_state:
    st.session_state.conversations = []

if "selected_chat" not in st.session_state:
    st.session_state.selected_chat = None

if "asked_questions" not in st.session_state:
    st.session_state.asked_questions = set()

if "show_suggestions_heading" not in st.session_state:
    st.session_state.show_suggestions_heading = True

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.header("🕘 Chat History")

    for i, chat in enumerate(st.session_state.conversations):
        if st.button(chat["user"][:50], key=f"history_{i}"):
            st.session_state.selected_chat = i

    if st.button("🧹 Clear Chat"):
        st.session_state.conversations = []
        st.session_state.asked_questions = set()
        st.session_state.selected_chat = None
        st.session_state.show_suggestions_heading = True
        st.rerun()

# ---------------- CHAT DISPLAY ----------------
for chat in st.session_state.conversations:
    with st.chat_message("user", avatar="🧑"):
        st.markdown(chat["user"])

    with st.chat_message("assistant", avatar="🤖"):
        st.markdown(chat["assistant"])

# ---------------- SUGGESTIONS ----------------
all_suggestions = [
    "Who is Manoj Nahak?",
    "Which Company he worked?",
    "What work he did at Saregama India Limited & Colgate Palmolive?",
    "How many years of experience he has?",
    "List Github projects",
    "Explain vectorless-rag"
]

remaining_suggestions = [
    q for q in all_suggestions if q not in st.session_state.asked_questions
]

# Show heading only once
if st.session_state.show_suggestions_heading and remaining_suggestions:
    st.markdown("#### 💡 Suggested Questions")

if remaining_suggestions:
    cols = st.columns(3)

    for i, question in enumerate(remaining_suggestions):
        if cols[i % 3].button(question, key=f"suggest_{i}"):

            st.session_state.asked_questions.add(question)
            st.session_state.show_suggestions_heading = False  # hide heading forever

            response = llm_response(question)

            st.session_state.conversations.append({
                "user": question,
                "assistant": response
            })

            st.rerun()

# ---------------- INPUT ----------------
prompt = st.chat_input("Ask something...")

if prompt:
    st.session_state.asked_questions.add(prompt)
    st.session_state.show_suggestions_heading = False  # hide heading forever

    response = llm_response(prompt)

    st.session_state.conversations.append({
        "user": prompt,
        "assistant": response
    })

    st.rerun()