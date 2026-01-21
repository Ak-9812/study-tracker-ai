import streamlit as st
from database import add_session, get_all_sessions
from agent import analyze_study

st.title("📘 Daily Study Tracker AI")

date = st.date_input("Date")
subject = st.text_input("Subject")
topics = st.text_area("Topics Studied")
time_spent = st.number_input("Time (minutes)", min_value=1)
done = st.checkbox("Completed?")

if st.button("Save Study Session"):
    add_session(date, subject, topics, time_spent, done)
    st.success("Study session saved!")

st.divider()
st.subheader("🤖 AI Study Analysis")

if st.button("Analyze My Study"):
    sessions = get_all_sessions()
    if sessions:
        analysis = analyze_study(sessions)
        st.write(analysis)
    else:
        st.warning("No study data yet.")
