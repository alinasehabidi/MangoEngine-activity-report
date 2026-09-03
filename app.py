import streamlit as st
import pandas as pd
import altair as alt

# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------
st.set_page_config(
    page_title="Jainam — Quarterly Impact Report",
    page_icon="🥭",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------------------------------------------------
# CUSTOM STYLING (Executive Minimalist Dark Theme)
# ---------------------------------------------------------
def apply_custom_styles(is_presentation: bool):
    max_w = "1180px" if not is_presentation else "1360px"
    font_boost = "1.05rem" if is_presentation else "0.95rem"
    
    st.markdown(
        f"""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
            
            html, body, [class*="css"] {{
                font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            }}
            
            .main .block-container {{
                max-width: {max_w};
                padding-top: 2rem;
                padding-bottom: 3.5rem;
                padding-left: 2rem;
                padding-right: 2rem;
            }}
            
            /* Sidebar Category Headers */
            .sidebar-category {{
                font-size: 0.72rem;
                font-weight: 700;
                letter-spacing: 0.08em;
                text-transform: uppercase;
                color: #8c9ba5;
                margin-top: 1.25rem;
                margin-bottom: 0.35rem;
                padding-left: 0.2rem;
            }}
            
            /* Executive KPI Card */
            .kpi-card {{
                background-color: #1a1e24;
                border: 1px solid #283039;
                border-radius: 8px;
                padding: 1.15rem 1.25rem;
                margin-bottom: 0.75rem;
                box-shadow: 0 2px 4px rgba(0,0,0,0.15);
            }}
            .kpi-title {{
                font-size: 0.78rem;
                font-weight: 600;
                text-transform: uppercase;
                letter-spacing: 0.05em;
                color: #94a3b8;
                margin-bottom: 0.3rem;
            }}
            .kpi-value {{
                font-size: 2rem;
                font-weight: 700;
                color: #ffffff;
                line-height: 1.1;
            }}
            .kpi-subtext {{
                font-size: 0.78rem;
                color: #64748b;
                margin-top: 0.3rem;
            }}
            
            /* Structured Logic / Before-After Containers */
            .logic-card {{
                background-color: #161b22;
                border-left: 4px solid #30885f;
                border-top: 1px solid #262c36;
                border-right: 1px solid #262c36;
                border-bottom: 1px solid #262c36;
                border-radius: 4px 8px 8px 4px;
                padding: 1.1rem 1.3rem;
                margin-bottom: 1rem;
            }}
            
            .logic-header {{
                font-size: 0.95rem;
                font-weight: 600;
                color: #f1f5f9;
                margin-bottom: 0.4rem;
            }}
            
            .status-badge {{
                display: inline-block;
                padding: 0.2rem 0.55rem;
                font-size: 0.72rem;
                font-weight: 600;
                border-radius: 4px;
                text-transform: uppercase;
                letter-spacing: 0.04em;
            }}
            .badge-done {{ background-color: rgba(48, 136, 95, 0.2); color: #4ade80; border: 1px solid #30885f; }}
            .badge-progress {{ background-color: rgba(234, 138, 50, 0.2); color: #fbbf24; border: 1px solid #ea8a32; }}
            .badge-planned {{ background-color: rgba(56, 114, 224, 0.2); color: #60a5fa; border: 1px solid #2563eb; }}
            .badge-invited {{ background-color: rgba(168, 85, 247, 0.2); color: #c084fc; border: 1px solid #9333ea; }}
            
            /* Banner Callouts */
            .outcome-banner {{
                background-color: #14221b;
                border: 1px solid #234e38;
                border-radius: 6px;
                padding: 0.9rem 1.2rem;
                font-size: {font_boost};
                color: #e2e8f0;
                margin: 1.25rem 0;
            }}
            .priority-banner {{
                background-color: #261b1b;
                border: 1px solid #542c2c;
                border-radius: 6px;
                padding: 0.9rem 1.2rem;
                font-size: {font_boost};
                color: #fed7d7;
                margin: 1.25rem 0;
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )

# ---------------------------------------------------------
# SIDEBAR NAVIGATION
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("### 🥭 MangoEngine")
    st.caption("Quarterly Impact Report • Q3 2026")
    
    st.markdown('<div class="sidebar-category">Overview</div>', unsafe_allow_html=True)
    p_overview = ["1. Executive Summary"]
    
    st.markdown('<div class="sidebar-category">Performance</div>', unsafe_allow_html=True)
    p_perf = [
        "2. Activity & Outcomes",
        "3. MangoEngine",
        "4. Visibility & Networking"
    ]
    
    st.markdown('<div class="sidebar-category">Development</div>', unsafe_allow_html=True)
    p_dev = [
        "5. Learning & Development",
        "6. Systems & SOPs"
    ]
    
    st.markdown('<div class="sidebar-category">Contribution</div>', unsafe_allow_html=True)
    p_contrib = ["7. Contribution & Impact"]
    
    st.markdown('<div class="sidebar-category">Next</div>', unsafe_allow_html=True)
    p_next = ["8. Next Quarter"]
    
    all_pages = p_overview + p_perf + p_dev + p_contrib + p_next
    selected_page = st.radio("Navigation", all_pages, label_visibility="collapsed")
    
    st.markdown("---")
    presentation_mode = st.toggle("Presentation mode", value=False)
    st.caption("Report period: 1 July – 3 September 2026")

apply_custom_styles(presentation_mode)

# ---------------------------------------------------------
# 1. EXECUTIVE SUMMARY
# ---------------------------------------------------------
if selected_page == "1. Executive Summary":
    st.title("Jainam — Quarterly Impact Report")
    st.subheader("1 July – 3 September 2026")
    
    st.markdown(
        """
        This report reviews execution, operational systems, and product development completed 
        during the quarter. Jainam engaged in 72 professional meetings, established 4 foundational operating 
        procedures, advanced core AI capabilities, and expanded visibility across external events and digital media.
        """
    )
    
    # 6 KPI Cards
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(
            """<div class="kpi-card">
                <div class="kpi-title">Total Meetings</div>
                <div class="kpi-value">72</div>
                <div class="kpi-subtext">Across product, visitors & events</div>
            </div>""",
            unsafe_allow_html=True
        )
        st.markdown(
            """<div class="kpi-card">
                <div class="kpi-title">External Events</div>
                <div class="kpi-value">12</div>
                <div class="kpi-subtext">In-person networking sessions</div>
            </div>""",
            unsafe_allow_html=True
        )
    with col2:
        st.markdown(
            """<div class="kpi-card">
                <div class="kpi-title">MangoEngine Focus</div>
                <div class="kpi-value">42</div>
                <div class="kpi-subtext">58.3% of all recorded meetings</div>
            </div>""",
            unsafe_allow_html=True
        )
        st.markdown(
            """<div class="kpi-card">
                <div class="kpi-title">Speaking Pipeline</div>
                <div class="kpi-value">4</div>
                <div class="kpi-subtext">Confirmed / invited engagements</div>
            </div>""",
            unsafe_allow_html=True
        )
    with col3:
        st.markdown(
            """<div class="kpi-card">
                <div class="kpi-title">AI Learning Completed</div>
                <div class="kpi-value">5</div>
                <div class="kpi-subtext">Modules (2 additional in progress)</div>
            </div>""",
            unsafe_allow_html=True
        )
        st.markdown(
            """<div class="kpi-card">
                <div class="kpi-title">Systems & SOPs</div>
                <div class="kpi-value">4</div>
                <div class="kpi-subtext">Operating procedures introduced</div>
            </div>""",
            unsafe_allow_html=True
        )
        
    st.markdown("---")
    
    # Timeline
    st.markdown("**Quarter Progression**")
    t_col1, t_col2, t_col3 = st.columns(3)
    with t_col1:
        st.markdown(
            """<div class="logic-card">
                <div class="logic-header">July 2026</div>
                • Initiated routine meeting cadence<br>
                • Conducted AI fundamental learning modules<br>
                • Introduced initial Google Form intake
            </div>""",
            unsafe_allow_html=True
        )
    with t_col2:
        st.markdown(
            """<div class="logic-card">
                <div class="logic-header">August 2026</div>
                • Gathered critical MangoEngine presentation feedback<br>
                • Established Burj Khalifa office visit workflow<br>
                • Structured lead routing & marketing connections
            </div>""",
            unsafe_allow_html=True
        )
    with t_col3:
        st.markdown(
            """<div class="logic-card">
                <div class="logic-header">September 2026</div>
                • Concluded 72 recorded stakeholder meetings<br>
                • Outlined backup server and compliance requirements<br>
                • Established Q4 dashboard demonstration priorities
            </div>""",
            unsafe_allow_html=True
        )

    st.markdown("---")
    st.markdown("**What Changed This Quarter**")
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("**Product**")
        st.write("Presentation feedback was converted into improvements, and an interactive dashboard was identified as the next major MangoEngine development step.")
        
        st.markdown("**Operations**")
        st.write("Standardized inquiry forms, structured lead routing, visitor intake, and marketing collaboration procedures were deployed.")
    with c2:
        st.markdown("**Development**")
        st.write("Professional learning was structured through business books, applied AI sessions, weekly assessments, and progress tracking.")
        
        st.markdown("**Visibility**")
        st.write("Maintained event participation, strengthened press relationships, and established a forward pipeline of 4 speaking engagements.")

    st.markdown(
        """<div class="priority-banner">
            <strong>Key priorities for next quarter:</strong> Complete MangoEngine dashboard demo • Formulate Time-management SOP • Standardize webinar preparation • Define productivity measurement.
        </div>""",
        unsafe_allow_html=True
    )

# ---------------------------------------------------------
# 2. ACTIVITY & OUTCOMES
# ---------------------------------------------------------
elif selected_page == "2. Activity & Outcomes":
    st.title("Activity & Outcomes")
    st.caption("Meeting breakdown, operational distribution, and resulting progress")
    
    # KPI row
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Total Meetings", "72")
    m2.metric("MangoEngine", "42", "58.3%")
    m3.metric("Office / Visitors", "18", "25.0%")
    m4.metric("Events", "12", "16.7%")
    
    st.markdown("---")
    
    col_chart, col_detail = st.columns([1.1, 1.3])
    
    with col_chart:
        st.markdown("**Meeting Allocation**")
        source_df = pd.DataFrame({
            "Category": ["MangoEngine daily meetings", "Office / visitor meetings", "Event meetings"],
            "Count": [42, 18, 12]
        })
        chart = (
            alt.Chart(source_df)
            .mark_arc(innerRadius=65)
            .encode(
                theta=alt.Theta(field="Count", type="quantitative"),
                color=alt.Color(
                    field="Category", 
                    type="nominal",
                    scale=alt.Scale(
                        domain=["MangoEngine daily meetings", "Office / visitor meetings", "Event meetings"],
                        range=["#30885f", "#ea8a32", "#4a7bb0"]
                    ),
                    legend=alt.Legend(orient="bottom", columns=1)
                ),
                tooltip=["Category", "Count"]
            )
            .properties(height=310)
        )
        st.altair_chart(chart, use_container_width=True)
        
        st.markdown(
            """<div class="logic-card">
                <div class="logic-header">Data Insight</div>
                More than half of recorded meetings (58.3%) were directly focused on MangoEngine product strategy and development.
            </div>""",
            unsafe_allow_html=True
        )
        
    with col_detail:
        st.markdown("**Key Outcomes**")
        st.markdown(
            """
            * **Deck Iteration:** MangoEngine presentation was restructured based on direct audience feedback.
            * **Product Simplification:** Identified the specific need for a clearer, non-technical product explanation.
            * **Visual Demonstration:** Defined an interactive dashboard as the primary proof-of-concept requirement.
            * **Launch Architecture:** Critical compliance and backup-server redundancies were identified prior to launch.
            """
        )
        
        st.markdown(
            """<div class="outcome-banner">
                <strong>Result:</strong> The meetings resulted in clearer product communication, presentation improvements, and a defined launch-readiness plan.
            </div>""",
            unsafe_allow_html=True
        )

# ---------------------------------------------------------
# 3. MANGOENGINE
# ---------------------------------------------------------
elif selected_page == "3. MangoEngine":
    st.title("MangoEngine")
    st.subheader("Product feedback, presentation development, and launch readiness")
    
    col_fb, col_ch = st.columns(2)
    
    with col_fb:
        st.markdown(
            """<div class="logic-card">
                <div class="logic-header">A. Audience Feedback (Recurring Questions)</div>
                • <strong>What is MangoEngine?</strong> Need for concise value proposition.<br>
                • <strong>Is Jainam building it himself?</strong> Clarification needed on Jainam's technical role.<br>
                • <strong>How will it work?</strong> Clarification required on day-to-day workflow.<br>
                • <strong>How will it be personal for each employee?</strong> Questions regarding customization.
            </div>""",
            unsafe_allow_html=True
        )
        
    with col_ch:
        st.markdown(
            """<div class="logic-card">
                <div class="logic-header">B. Changes Implemented</div>
                • <strong>Simple Explanation:</strong> Defined product in clear language at the start of deck.<br>
                • <strong>Role Clarity:</strong> Explicitly delineated Jainam's responsibilities in the slides.<br>
                • <strong>Personalization Detail:</strong> Added slides showing personalized employee utility.<br>
                • <strong>Demo Preparedness:</strong> Committed to building live dashboard demonstration.
            </div>""",
            unsafe_allow_html=True
        )
        
    st.markdown("---")
    st.markdown("**C. Current Product Status**")
    
    s1, s2, s3 = st.columns(3)
    with s1:
        st.markdown(
            """<div class="kpi-card">
                <span class="status-badge badge-done">Completed</span>
                <div style="margin-top:0.6rem; font-weight:600; color:#fff;">Slide Deck Revision</div>
                <div class="kpi-subtext">Incorporated simpler messaging, clarified founder role, and refined narrative flow.</div>
            </div>""",
            unsafe_allow_html=True
        )
    with s2:
        st.markdown(
            """<div class="kpi-card">
                <span class="status-badge badge-progress">In Progress</span>
                <div style="margin-top:0.6rem; font-weight:600; color:#fff;">Launch Preparation</div>
                <div class="kpi-subtext">Structuring backup-server infrastructure and pre-launch compliance checks.</div>
            </div>""",
            unsafe_allow_html=True
        )
    with s3:
        st.markdown(
            """<div class="kpi-card">
                <span class="status-badge badge-planned">Next</span>
                <div style="margin-top:0.6rem; font-weight:600; color:#fff;">Dashboard Demonstration</div>
                <div class="kpi-subtext">Building interactive dashboard to show functional mechanics in live presentations.</div>
            </div>""",
            unsafe_allow_html=True
        )

    st.markdown(
        """<div class="outcome-banner">
            <strong>Next major product priority:</strong> MangoEngine dashboard demonstration.
        </div>""",
        unsafe_allow_html=True
    )

# ---------------------------------------------------------
# 4. VISIBILITY & NETWORKING
# ---------------------------------------------------------
elif selected_page == "4. Visibility & Networking":
    st.title("Visibility & Networking")
    st.caption("Professional relations, audience footprint, and speaking pipeline")
    
    v1, v2, v3 = st.columns(3)
    v1.metric("Events Attended", "12")
    v2.metric("Instagram Audience", "101K", "Current followers")
    v3.metric("Speaking Pipeline", "4 Engagements")
    
    st.markdown("---")
    
    col_aud, col_net = st.columns([1.2, 1])
    
    with col_aud:
        st.markdown("**Audience & Visibility**")
        st.caption("Current platform follower distribution (Audience footprint, not growth rate)")
        
        aud_df = pd.DataFrame({
            "Platform": ["Instagram", "Facebook", "YouTube", "X", "Threads"],
            "Followers": [101000, 198, 149, 22, 0]
        })
        
        aud_chart = (
            alt.Chart(aud_df)
            .mark_bar(color="#30885f")
            .encode(
                x=alt.X("Followers:Q", title="Followers", scale=alt.Scale(type="sqrt")),
                y=alt.Y("Platform:N", sort="-x", title=""),
                tooltip=["Platform", "Followers"]
            )
            .properties(height=220)
        )
        st.altair_chart(aud_chart, use_container_width=True)
        
    with col_net:
        st.markdown("**Media Contacts & Engagement**")
        st.markdown(
            """
            * **Network Connections:** Amit Bherwani, Sunil Kumar, RJ Sarah, Hayat / Dubai Media, Dubai Radio, and collegiate networks.
            * **Top Content:** Reels featuring Sanjadat and the Sunil Kumar podcast recorded approximately 3K+ likes each.
            * **Channel Recovery:** Dedicated marketing efforts continue for Facebook, YouTube, X, Threads, and LinkedIn account recovery.
            """
        )

    st.markdown("---")
    st.markdown("**Speaking & Visibility Pipeline**")
    
    pipe_data = [
        {"When": "November 2026", "Opportunity": "TEDx", "Place": "University of Ras Al Khaimah", "Status": "Planned"},
        {"When": "To be confirmed", "Opportunity": "Product / speaking event", "Place": "University of Ras Al Khaimah", "Status": "Invited"},
        {"When": "To be confirmed", "Opportunity": "Invitation-only event", "Place": "Sri Lanka — 200 guests", "Status": "Invited"},
        {"When": "March 2027", "Opportunity": "Dubai Police event", "Place": "Dubai", "Status": "Planned"}
    ]
    st.dataframe(pd.DataFrame(pipe_data), use_container_width=True, hide_index=True)

# ---------------------------------------------------------
# 5. LEARNING & DEVELOPMENT
# ---------------------------------------------------------
elif selected_page == "5. Learning & Development":
    st.title("Learning & Development")
    st.caption("Professional development tracking, knowledge application, and assessments")
    
    l1, l2, l3 = st.columns(3)
    l1.metric("Books Completed", "2")
    l2.metric("Average Test Score", "80%")
    l3.metric("Performance Evaluation", "85%")
    
    st.markdown("---")
    st.markdown("**Curriculum Progress & Practical Application**")
    
    dev_data = [
        {
            "Session / Topic": "AI Fundamentals & the Future of AI",
            "Status": "Done",
            "Practical Application": "Understanding core capabilities of AI, ML, GenAI, and LLMs"
        },
        {
            "Session / Topic": "Prompt Engineering Masterclass",
            "Status": "Done",
            "Practical Application": "Formulating optimized prompts for business and market research"
        },
        {
            "Session / Topic": "AI Productivity for Founders",
            "Status": "Done",
            "Practical Application": "Streamlining emails, presentations, routine summaries, and task automation"
        },
        {
            "Session / Topic": "First Principles Thinking",
            "Status": "Done",
            "Practical Application": "Questioning foundational assumptions and designing direct solutions"
        },
        {
            "Session / Topic": "iOS 27: Top 5 New Features",
            "Status": "Done",
            "Practical Application": "Video learning module completion"
        },
        {
            "Session / Topic": "Hailuo AI",
            "Status": "In progress",
            "Practical Application": "Evaluating AI video platform updates and generation capabilities"
        },
        {
            "Session / Topic": "Dr. Fei-Fei Li interview",
            "Status": "In progress",
            "Practical Application": "Reviewing advanced AI industry insights and structured evaluation quiz"
        }
    ]
    
    st.dataframe(pd.DataFrame(dev_data), use_container_width=True, hide_index=True)
    
    st.markdown(
        """<div class="outcome-banner">
            <strong>Impact:</strong> AI knowledge is directly applied to daily research, prompt iteration, deck drafting, meeting synthesis, and workflow design.
        </div>""",
        unsafe_allow_html=True
    )

# ---------------------------------------------------------
# 6. SYSTEMS & SOPS
# ---------------------------------------------------------
elif selected_page == "6. Systems & SOPs":
    st.title("Systems & Process Improvements")
    st.caption("Operational frameworks deployed to eliminate bottlenecks and standardize workflows")
    
    st.markdown(
        """<div class="logic-card">
            <div class="logic-header">1. Inquiry Intake Form</div>
            • <strong>Problem / Need:</strong> Inquiries lacked standard intake, leading to unorganized requests.<br>
            • <strong>What Was Implemented:</strong> A standard Google Form intake process.<br>
            • <strong>Impact:</strong> Rapidly categorizes requests (podcast, speaking engagement, or partnership).
        </div>""",
        unsafe_allow_html=True
    )
    
    st.markdown(
        """<div class="logic-card">
            <div class="logic-header">2. Lead Sorting and Follow-Up</div>
            • <strong>Problem / Need:</strong> Risk of dropped leads and delayed responses.<br>
            • <strong>What Was Implemented:</strong> Standardized lead categorization and follow-up routing.<br>
            • <strong>Impact:</strong> Connects prospective partners faster with reduced drop-off.
        </div>""",
        unsafe_allow_html=True
    )
    
    st.markdown(
        """<div class="logic-card">
            <div class="logic-header">3. Office Visit Workflow</div>
            • <strong>Problem / Need:</strong> Ad-hoc coordination for visitors at the Burj Khalifa office.<br>
            • <strong>What Was Implemented:</strong> Structured visitor invitation and clearance protocol.<br>
            • <strong>Impact:</strong> Organized visitor reception with clear scheduling.
        </div>""",
        unsafe_allow_html=True
    )
    
    st.markdown(
        """<div class="logic-card">
            <div class="logic-header">4. Marketing-Team Coordination</div>
            • <strong>Problem / Need:</strong> Unstructured communication between leadership and the IMF / marketing unit.<br>
            • <strong>What Was Implemented:</strong> Formal communication pipeline with the marketing team.<br>
            • <strong>Impact:</strong> Marketing initiatives advance with reduced friction and ambiguity.
        </div>""",
        unsafe_allow_html=True
    )
    
    st.markdown(
        """<div class="priority-banner">
            <strong>Outstanding Priority:</strong> Time-Management SOP. To be created following baseline measurement of daily work allocation.
        </div>""",
        unsafe_allow_html=True
    )
    
    st.markdown("**Tools Supporting Operations**")
    st.write("ChatGPT, Claude, specialized AI agents, and Canva AI are utilized to accelerate content drafts, outbound communication, and administrative tasks.")

# ---------------------------------------------------------
# 7. CONTRIBUTION & IMPACT
# ---------------------------------------------------------
elif selected_page == "7. Contribution & Impact":
    st.title("Contribution & Impact")
    st.caption("Delineating executive leadership activity and operational support provided")
    
    st.markdown(
        """
        To maintain executive governance, this section distinguishes between 
        **Jainam's strategic execution** and the **operational support provided** to scale capacity.
        """
    )
    
    contrib_items = [
        {
            "Domain": "Operations",
            "Support Provided": "Configured Google Forms intake and systematized follow-up routing.",
            "Result / Change": "Inquiries categorized rapidly; pipeline leakage prevented."
        },
        {
            "Domain": "Opportunities",
            "Support Provided": "Handled initial inbound contact sorting and prompt follow-up management.",
            "Result / Change": "High-value external connections preserved without missed opportunities."
        },
        {
            "Domain": "Learning",
            "Support Provided": "Curated technical video readings, designed quizzes, and logged evaluation scores.",
            "Result / Change": "Maintained 80% test average and continuous AI skill advancement."
        },
        {
            "Domain": "Product",
            "Support Provided": "Critiqued MangoEngine presentation slides and scoped demo requirements.",
            "Result / Change": "Streamlined deck narrative; established dashboard demo as next milestone."
        },
        {
            "Domain": "Webinar Coaching",
            "Support Provided": "Assisted in rehearsal prep, speech clarity, filler reduction, and closing syntheses.",
            "Result / Change": "Established 4-step delivery standard for live presentations."
        },
        {
            "Domain": "Memory & Retention",
            "Support Provided": "Introduced 'explain-it-to-someone' synthesis method with 30/60-day reviews.",
            "Result / Change": "Ensured retention and practical application of insights from completed books."
        }
    ]
    
    st.dataframe(pd.DataFrame(contrib_items), use_container_width=True, hide_index=True)
    
    st.markdown(
        """<div class="outcome-banner">
            <strong>Support Focus:</strong> Translating feedback into an interactive dashboard demo, standardizing webinar delivery frameworks, and establishing productivity metrics.
        </div>""",
        unsafe_allow_html=True
    )

# ---------------------------------------------------------
# 8. NEXT QUARTER
# ---------------------------------------------------------
elif selected_page == "8. Next Quarter":
    st.title("Next Quarter")
    st.subheader("Priorities, outstanding work, and measurable next steps")
    
    col_p1, col_p2 = st.columns(2)
    
    with col_p1:
        st.markdown(
            """<div class="kpi-card">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <span style="font-weight:700; color:#fff;">1. MangoEngine Dashboard</span>
                    <span class="status-badge badge-planned">Planned</span>
                </div>
                <div style="margin-top:0.8rem; font-size:0.85rem;">
                    <strong>Objective:</strong> Provide an interactive visual proof-of-concept for presentations.<br>
                    <strong>Next Action:</strong> Scope UI requirements and build live demonstration module.
                </div>
            </div>""",
            unsafe_allow_html=True
        )
        
        st.markdown(
            """<div class="kpi-card">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <span style="font-weight:700; color:#fff;">2. Time-Management SOP</span>
                    <span class="status-badge badge-progress">Not Yet Created</span>
                </div>
                <div style="margin-top:0.8rem; font-size:0.85rem;">
                    <strong>Objective:</strong> Standardize daily routine allocation and calendar discipline.<br>
                    <strong>Next Action:</strong> Measure baseline daily activity prior to drafting SOP documentation.
                </div>
            </div>""",
            unsafe_allow_html=True
        )
        
    with col_p2:
        st.markdown(
            """<div class="kpi-card">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <span style="font-weight:700; color:#fff;">3. Webinar Format</span>
                    <span class="status-badge badge-progress">Being Developed</span>
                </div>
                <div style="margin-top:0.8rem; font-size:0.85rem;">
                    <strong>Objective:</strong> Ensure disciplined delivery and minimize live pauses.<br>
                    <strong>Next Action:</strong> Implement 4-step preparation protocol across upcoming webinars.
                </div>
            </div>""",
            unsafe_allow_html=True
        )
        
        st.markdown(
            """<div class="kpi-card">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <span style="font-weight:700; color:#fff;">4. Productivity Measurement</span>
                    <span class="status-badge badge-planned">To Be Defined</span>
                </div>
                <div style="margin-top:0.8rem; font-size:0.85rem;">
                    <strong>Objective:</strong> Quantify output improvements across operations and AI adoption.<br>
                    <strong>Next Action:</strong> Determine simple, recurring metrics to monitor ongoing efficiency.
                </div>
            </div>""",
            unsafe_allow_html=True
        )
        
    st.markdown("---")
    st.markdown("**Success by the Next Report**")
    st.markdown(
        """
        * **Dashboard demonstration:** Operational visual demo integrated into partner presentations.
        * **Time-management process:** Standard procedure established and executed daily.
        * **Standardized webinar format:** Rehearsal-backed execution with structured closing summaries.
        * **Productivity measurement:** Established baseline metrics tracking operational gains.
        """
    )