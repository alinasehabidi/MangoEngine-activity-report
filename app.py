"""MangoEngine activity report | 1 July–3 September 2026."""

from __future__ import annotations

import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="MangoEngine | Activity Report", page_icon="🥭", layout="wide")

PERIOD = "1 July – 3 September 2026"
SECTIONS = ["Meetings & outcomes", "Presentation & webinar feedback", "Events & networking", "Learning & development", "New SOPs that helped", "My support"]
MEETINGS = pd.DataFrame({"Meeting type": ["MangoEngine daily meetings", "Event meetings", "Office / visitor meetings"], "Number": [42, 12, 18]})
SOCIAL = pd.DataFrame({"Platform": ["Instagram", "Facebook", "YouTube", "X", "Threads"], "Followers": [101000, 198, 149, 22, 0]})
AI_LEARNING = pd.DataFrame([
    ["AI Fundamentals & the Future of AI", "Done", "What AI, ML, GenAI and LLMs can do"],
    ["Prompt Engineering Masterclass", "Done", "Better prompts for research and business work"],
    ["AI Productivity for Founders", "Done", "AI for emails, slides, summaries and tasks"],
    ["First Principles Thinking", "Done", "Question assumptions and find a better way"],
    ["iOS 27: Top 5 New Features", "Done", "Video learning"],
    ["Hailuo AI", "In progress", "AI update"],
    ["Dr. Fei-Fei Li interview", "In progress", "Interview and quiz"],
], columns=["Session", "Status", "Main learning"])


def header(title: str, subtitle: str) -> None:
    st.title(title)
    st.caption(subtitle)


def presenter_box(talk: str, ask: str, end: str) -> None:
    if not st.session_state.presentation_mode:
        return
    st.divider()
    st.subheader("Presenter notes")
    a, b, c = st.columns(3)
    a.info(f"**Say:** {talk}")
    b.warning(f"**Ask:** {ask}")
    c.success(f"**End with:** {end}")


if "report_section" not in st.session_state:
    st.session_state.report_section = SECTIONS[0]

st.markdown("""
<style>
.block-container {padding-top: 2rem; padding-bottom: 3rem;}
[data-testid="stMetric"], [data-testid="stDataFrame"], [data-testid="stPlotlyChart"], [data-testid="stExpander"] {transition: transform .22s ease, filter .22s ease, box-shadow .22s ease;}
[data-testid="stMetric"] {background: rgba(243,169,83,.14); border-radius: 12px; padding: 16px;}
[data-testid="stMetric"]:hover, [data-testid="stDataFrame"]:hover, [data-testid="stPlotlyChart"]:hover, [data-testid="stExpander"]:hover {transform: translateY(-3px); filter: brightness(1.12); box-shadow: 0 14px 30px rgba(243,169,83,.16);}
div[data-testid="stHorizontalBlock"]:has([data-testid="stMetric"]:hover) [data-testid="stMetric"]:not(:hover) {filter: blur(1.5px) opacity(.58);}
.note {background: rgba(46,125,91,.18); border-left: 5px solid #2e7d5b; padding: 1rem 1.2rem; border-radius: 8px; margin: .6rem 0;}
.warn {background: rgba(199,91,57,.18); border-left: 5px solid #c75b39; padding: 1rem 1.2rem; border-radius: 8px; margin: .6rem 0;}
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.header("🥭 MangoEngine")
    st.caption("Simple activity report")
    st.divider()
    st.radio("Choose a section", SECTIONS, key="report_section")
    st.divider()
    st.toggle("Presentation mode", key="presentation_mode", help="Shows short talk tracks, questions, and closing points.")
    st.caption(f"Report period: {PERIOD}")

section = st.session_state.report_section

if section == "Meetings & outcomes":
    header("Meetings & outcomes", PERIOD)
    st.write("Jainam attended **72 meetings**. Most were about MangoEngine, events, and office visitors.")
    a, b, c, d = st.columns(4)
    a.metric("Total meetings", "72")
    b.metric("MangoEngine meetings", "42")
    c.metric("Event meetings", "12")
    d.metric("Office / visitor meetings", "18")
    left, right = st.columns([1, 1.05])
    with left:
        fig = px.pie(MEETINGS, values="Number", names="Meeting type", hole=.58, color_discrete_sequence=["#2e7d5b", "#f3a953", "#6e9dd1"])
        fig.update_layout(title="Where the meeting time went", height=345, margin=dict(t=55, b=10, l=10, r=10), legend_title_text="")
        st.plotly_chart(fig, width="stretch")
    with right:
        st.subheader("What came from the meetings")
        st.markdown("- The MangoEngine presentation was improved after feedback.\n- People still need a clearer product explanation.\n- A dashboard is planned so people can see how the product works.\n- Compliance and backup-server planning were raised before launch.")
        st.markdown("<div class='note'><b>Main result:</b> the meetings gave a clear product, presentation, and launch-readiness plan.</div>", unsafe_allow_html=True)
    presenter_box("We had a strong meeting rhythm: 72 meetings, with 42 focused on MangoEngine.", "What should we improve first: the story, dashboard, or launch readiness?", "The feedback gave us a clear next-step plan.")

elif section == "Presentation & webinar feedback":
    header("Presentation & webinar feedback", "What people asked, what changed, and what happens next")
    st.subheader("Feedback on the MangoEngine presentation")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("**Questions heard many times**\n\n- What is MangoEngine?\n- Is Jainam building it himself?\n- How will it work?\n- How will it be personal for each employee?")
    with c2:
        st.markdown("**Changes needed**\n\n- Explain the product in simple words at the start.\n- Make Jainam's role clear in the slides.\n- Show how it will be personal for employees.\n- Add a dashboard demo when it is ready.")
    st.markdown("<div class='note'><b>Already done:</b> the presentation has been changed a little. The next big improvement is to add the dashboard.</div>", unsafe_allow_html=True)
    st.subheader("Webinar feedback")
    st.write("Jainam led **4 webinars**. Building from audience input is a good idea, but the delivery will work better with more preparation.")
    feedback, plan = st.columns(2)
    with feedback:
        st.markdown("**What to improve**\n\n- Practice before the webinar to reduce fillers and long pauses.\n- Speak clearly while building.\n- Use a prepared example when a live idea needs too much thinking time.\n- End with a clear summary.")
    with plan:
        st.markdown("**New webinar standard**\n\n1. Prepare the product flow first.\n2. Explain each step out loud.\n3. Use audience ideas when they fit the flow.\n4. End by showing what was made and the steps used.")
    st.caption("Jainam watched his webinar, spoke with Hashitar, and the next webinar is being planned.")
    presenter_box("Make the product easier to understand and the webinar flow more confident.", "Would a dashboard demo answer the main questions faster than more slides?", "We know exactly what to test in the next webinar.")

elif section == "Events & networking":
    header("Events & networking", "New relationships, visibility, and future speaking chances")
    a, b, c = st.columns(3)
    a.metric("Events attended", "12")
    b.metric("Instagram followers", "101K")
    c.metric("Future speaking opportunities", "4")
    left, right = st.columns([1.05, 1])
    with left:
        fig = px.bar(SOCIAL, x="Followers", y="Platform", orientation="h", text="Followers", color="Platform", color_discrete_sequence=["#2e7d5b", "#f3a953", "#6e9dd1", "#a071ba", "#d06c74"])
        fig.update_layout(title="Current social audience", height=335, showlegend=False, yaxis_title=None, margin=dict(t=55, b=15, l=5, r=10))
        st.plotly_chart(fig, width="stretch")
    with right:
        st.subheader("People and media contacts")
        st.write("Connections include Amit Bherwani, Sunil Kumar, RJ Sarah, Hayat / Dubai Media, Dubai Radio, and college contacts.")
        st.markdown("<div class='note'><b>Content that did well:</b> reels with Sanjadat and the Sunil Kumar podcast reportedly received 3K+ likes each.</div>", unsafe_allow_html=True)
        st.caption("Instagram is the strongest channel. The marketing team is working on Facebook, YouTube, X, Threads and LinkedIn recovery.")
    st.subheader("Speaking and visibility pipeline")
    opportunities = pd.DataFrame([["November 2026", "TEDx", "University of Ras Al Khaimah", "Planned"], ["To be confirmed", "Product / speaking event", "University of Ras Al Khaimah", "Invited"], ["To be confirmed", "Invitation-only event", "Sri Lanka — 200 guests", "Invited"], ["March 2027", "Dubai Police event", "Dubai", "Planned"]], columns=["When", "Opportunity", "Place", "Status"])
    st.dataframe(opportunities, width="stretch", hide_index=True)
    presenter_box("Events are growing the network and creating a strong speaking pipeline.", "Which opportunity gives the best chance to show MangoEngine clearly?", "Now we must turn visibility into product understanding.")

elif section == "Learning & development":
    header("Learning & development", "Book reading and AI learning sessions")
    a, b, c = st.columns(3)
    a.metric("Books completed", "2")
    b.metric("Average test score", "80%")
    c.metric("Performance evaluation", "85%")
    book_tab, ai_tab = st.tabs(["A. Book reading", "B. AI learning sessions"])
    with book_tab:
        st.subheader("Books read and outcomes")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**1. Million Dollar Weekend**\n\nMain lesson: start before you feel fully ready. It helped with fear of asking, fear of failure, and fear of starting.\n\n**Use it:** take action faster, ask for feedback, and test ideas early.")
        with col2:
            st.markdown("**2. Personal Success**\n\nCompleted. Detailed notes were not supplied, so the next review should record the main lessons and one action to take.\n\n**Remembering method:** explain the book to someone else, then repeat after about 30 and 60 days.")
    with ai_tab:
        st.subheader("AI learning sessions")
        st.write("Four core AI sessions are complete. Two extra AI learning items are in progress.")
        st.dataframe(AI_LEARNING, width="stretch", hide_index=True)
        st.markdown("<div class='note'><b>Result:</b> AI learning is being used for research, prompts, presentations, meeting summaries, tasks and better workflow thinking.</div>", unsafe_allow_html=True)
    presenter_box("Learning is not only a list of completed sessions. It is being used in daily work and product thinking.", "Which learning should become a weekly habit?", "Next, we will track one practical action from each learning item.")

elif section == "New SOPs that helped":
    header("New SOPs that helped streamline work", "Simple systems that make opportunities easier to manage")
    st.write("These processes made it easier to understand requests, connect the right people, and keep follow-up moving.")
    sops = pd.DataFrame([["Inquiry form", "A Google Form is shared when an inquiry arrives.", "The team quickly sees if it is for a podcast, speaking chance, or another request."], ["Lead sorting and follow-up", "Opportunities are sorted and followed up in a clearer way.", "The right people can be connected faster and fewer leads are missed."], ["Office visit process", "A process was created for inviting people to the Burj Khalifa office.", "Visitor meetings are easier to organise."], ["Marketing-team connection", "A standard way to connect with the IMF / marketing team was set.", "Marketing requests can move with less confusion."]], columns=["SOP", "What changed", "How it helped"])
    st.dataframe(sops, width="stretch", hide_index=True)
    st.subheader("Tools that support the work")
    st.write("ChatGPT, Claude, other AI agents, and Canva AI are used to work faster on content, communication and routine tasks.")
    presenter_box("The main win is not only new tools. It is a clearer way to receive, sort and follow up on opportunities.", "Which process should we document next so anyone can follow it?", "The next SOP should protect time for product work.")

else:
    header("My support", "How I helped Jainam execute, learn and improve")
    st.subheader("My role")
    support = pd.DataFrame([["Better process", "Helped set up the Google Form and a clearer way to manage leads and follow-ups."], ["More opportunities", "Connected with people who reached out and followed up so opportunities did not get lost."], ["Learning support", "Shared videos and reading, gave quizzes and tests, and kept a record of progress."], ["Product feedback", "Gave feedback on the MangoEngine presentation. The deck has already been improved and dashboard feedback is ready for when the product is available."], ["Webinar coaching", "Gave feedback on preparation, clear speaking, fewer fillers, and ending with a summary."], ["Memory support", "Introduced the explain-it-to-someone method, with 30-day and 60-day book summaries."]], columns=["Support area", "What I did"])
    st.dataframe(support, width="stretch", hide_index=True)
    st.subheader("How this helped")
    one, two, three = st.columns(5)
    one.metric("Better focus", "More time for product work")
    two.metric("Learning record", "Quizzes and tests tracked")
    three.metric("Product feedback", "Deck improved")
    st.markdown("<div class='note'><b>Next support focus:</b> turn feedback into a dashboard demo, a clear webinar format, and a simple way to measure productivity gains.</div>", unsafe_allow_html=True)
    presenter_box("My support makes execution easier: clearer processes, steady learning and practical feedback.", "What support would give Jainam the biggest benefit in the next 90 days?", "We will keep the systems simple and link every activity to a clear result.")
