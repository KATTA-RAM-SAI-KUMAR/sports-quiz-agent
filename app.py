import streamlit as st
from src.generator import generate_quiz

st.set_page_config(
    page_title="🏆 AI Sports Quiz Generator",
    page_icon="🏆",
    layout="wide"
)

# -------------------- Custom CSS --------------------

st.markdown("""
<style>

.stApp{
    background: linear-gradient(135deg,#0f172a,#1e293b,#334155);
    color:white;
}

.main-title{
    text-align:center;
    font-size:48px;
    font-weight:bold;
    color:white;
}

.sub-title{
    text-align:center;
    color:#cbd5e1;
    font-size:20px;
    margin-bottom:30px;
}

.question-card{
    background:white;
    padding:25px;
    border-radius:15px;
    box-shadow:0px 10px 25px rgba(0,0,0,0.25);
    color:black;
    margin-top:20px;
    margin-bottom:20px;
}

.score-card{
    background:#16a34a;
    color:white;
    padding:30px;
    border-radius:20px;
    text-align:center;
    font-size:28px;
    font-weight:bold;
}

.review-card{
    background:white;
    color:black;
    padding:20px;
    border-radius:15px;
    margin-top:15px;
}

div.stButton > button{
    width:100%;
    background:#2563eb;
    color:white;
    border:none;
    border-radius:10px;
    height:50px;
    font-size:18px;
    font-weight:bold;
}

div.stButton > button:hover{
    background:#1d4ed8;
}

</style>
""", unsafe_allow_html=True)

# -------------------- Sidebar --------------------

with st.sidebar:

    st.title("🏆 AI Quiz")

    st.markdown("---")

    st.success("Backend")

    st.write("✅ Gemini AI")
    st.write("✅ ChromaDB")
    st.write("✅ RAG")
    st.write("✅ Web Search")

    st.markdown("---")

    st.info("Made with Streamlit")

# -------------------- Session State --------------------

if "quiz" not in st.session_state:
    st.session_state.quiz = None

if "current_question" not in st.session_state:
    st.session_state.current_question = 0

if "answers" not in st.session_state:
    st.session_state.answers = {}

if "submitted" not in st.session_state:
    st.session_state.submitted = False

# -------------------- Header --------------------

st.markdown(
    "<div class='main-title'>🏆 AI Sports Quiz Generator</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='sub-title'>Powered by Gemini + ChromaDB + RAG</div>",
    unsafe_allow_html=True
)

col1,col2=st.columns(2)

with col1:

    sport=st.selectbox(
        "🏏 Select Sport",
        [
            "Cricket",
            "Football",
            "Basketball",
            "Tennis",
            "Badminton"
        ]
    )

with col2:

    difficulty=st.selectbox(
        "🎯 Difficulty",
        [
            "Easy",
            "Medium",
            "Hard"
        ]
    )

if st.button("🚀 Generate Quiz"):

    with st.spinner("Generating AI Quiz..."):

        st.session_state.quiz=generate_quiz(sport)

        st.session_state.current_question=0

        st.session_state.answers={}

        st.session_state.submitted=False

    st.rerun()
# -------------------- Quiz Screen --------------------

if st.session_state.quiz is not None and not st.session_state.submitted:

    total_questions = len(st.session_state.quiz)
    current = st.session_state.current_question

    st.progress((current + 1) / total_questions)

    st.markdown(
        f"### Question {current + 1} of {total_questions}"
    )

    question = st.session_state.quiz[current]

    st.markdown(
        "<div class='question-card'>",
        unsafe_allow_html=True
    )

    st.markdown(f"## {question['question']}")

    saved_answer = st.session_state.answers.get(current, None)

    answer = st.radio(
        "Choose your answer",
        question["options"],
        index=question["options"].index(saved_answer)
        if saved_answer in question["options"] else None,
        key=f"radio_{current}"
    )

    if answer:
        st.session_state.answers[current] = answer

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )

    left, center, right = st.columns([1, 2, 1])

    with left:

        if current > 0:

            if st.button("⬅ Previous"):

                st.session_state.current_question -= 1
                st.rerun()

    with right:

        if current < total_questions - 1:

            if st.button("Next ➡"):

                st.session_state.current_question += 1
                st.rerun()

        else:

            if st.button("✅ Submit Quiz"):

                st.session_state.submitted = True
                st.rerun()
# -------------------- Result Screen --------------------

if st.session_state.quiz is not None and st.session_state.submitted:

    quiz = st.session_state.quiz

    score = 0

    for i, question in enumerate(quiz):

        if st.session_state.answers.get(i) == question["answer"]:
            score += 1

    percentage = int((score / len(quiz)) * 100)

    if percentage >= 80:
        st.balloons()
        message = "🏆 Excellent!"
        color = "#16a34a"

    elif percentage >= 60:
        message = "👍 Good Job!"
        color = "#2563eb"

    elif percentage >= 40:
        message = "🙂 Nice Try!"
        color = "#f59e0b"

    else:
        message = "📚 Keep Practicing!"
        color = "#dc2626"

    st.markdown(
        f"""
        <div style="
            background:{color};
            padding:30px;
            border-radius:20px;
            text-align:center;
            color:white;
            margin-top:20px;
            margin-bottom:20px;
        ">
        <h1>🏆 Final Score</h1>
        <h1>{score} / {len(quiz)}</h1>
        <h2>{percentage}%</h2>
        <h3>{message}</h3>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.header("📋 Answer Review")

    for i, question in enumerate(quiz):

        user_answer = st.session_state.answers.get(i, "Not Answered")
        correct = question["answer"]

        if user_answer == correct:
            status = "✅ Correct"
            bgcolor = "#dcfce7"

        else:
            status = "❌ Wrong"
            bgcolor = "#fee2e2"

        st.markdown(
            f"""
            <div style="
                background:{bgcolor};
                padding:20px;
                border-radius:15px;
                margin-bottom:20px;
                color:black;
            ">

            <h3>Question {i+1}</h3>

            <b>{question['question']}</b>

            <br><br>

            <b>Your Answer:</b> {user_answer}

            <br>

            <b>Correct Answer:</b> {correct}

            <br>

            <b>Difficulty:</b> {question['difficulty']}

            <br><br>

            <b>{status}</b>

            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("---")

    if st.button("🔄 Start New Quiz"):

        st.session_state.quiz = None
        st.session_state.current_question = 0
        st.session_state.answers = {}
        st.session_state.submitted = False

        st.rerun()