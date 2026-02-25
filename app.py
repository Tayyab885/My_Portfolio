import streamlit as st

# Contact Information
LINKEDIN_URL = 'https://www.linkedin.com/in/muhammad-tayyab-9b965b1b1/'
GITHUB_URL = 'https://github.com/Tayyab885'
EMAIL = 'm.tayyab273@gmail.com'

# Page Configuration
st.set_page_config(
    page_title='Muhammad Tayyab | Data Scientist',
    page_icon='◈',
    layout='wide',
    initial_sidebar_state='expanded'
)

# Custom CSS - Modern Black Theme, No Gradients
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Syne:wght@400;600;700;800&display=swap');

    /* ===== KEYFRAMES ===== */
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(24px); }
        to   { opacity: 1; transform: translateY(0); }
    }

    @keyframes fadeInLeft {
        from { opacity: 0; transform: translateX(-20px); }
        to   { opacity: 1; transform: translateX(0); }
    }

    @keyframes fadeIn {
        from { opacity: 0; }
        to   { opacity: 1; }
    }

    @keyframes slideDown {
        from { opacity: 0; transform: translateY(-16px); }
        to   { opacity: 1; transform: translateY(0); }
    }

    @keyframes cursorBlink {
        0%, 100% { opacity: 1; }
        50%       { opacity: 0; }
    }

    @keyframes shimmer {
        0%   { background-position: -400px 0; }
        100% { background-position: 400px 0; }
    }

    @keyframes borderPulse {
        0%, 100% { border-color: #303030; }
        50%       { border-color: #555; }
    }

    @keyframes countUp {
        from { opacity: 0; transform: translateY(10px); }
        to   { opacity: 1; transform: translateY(0); }
    }

    /* ===== BASE ===== */
    * { box-sizing: border-box; }

    .stApp {
        background-color: #222222;
        font-family: 'Syne', sans-serif;
    }

    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }
    header { visibility: hidden; }

    /* Hide ALL sidebar toggle / collapse buttons */
    [data-testid="collapsedControl"] { display: none !important; }
    button[kind="header"] { display: none !important; }
    [data-testid="stSidebarCollapseButton"] { display: none !important; }
    [data-testid="stSidebarUserContent"] button[aria-label] { display: none !important; }
    section[data-testid="stSidebar"] > div > div:first-child button { display: none !important; }
    .st-emotion-cache-1rtdyuf { display: none !important; }
    .st-emotion-cache-eczf16 { display: none !important; }
    /* Keep sidebar always visible */
    section[data-testid="stSidebar"] { transform: none !important; min-width: 240px !important; }

    .block-container {
        padding: 2rem 2.5rem;
        max-width: 1200px;
    }

    /* ===== SIDEBAR ===== */
    [data-testid="stSidebar"] {
        background-color: #222222;
        border-right: 1px solid #242424;
        animation: fadeIn 0.6s ease both;
    }

    [data-testid="stSidebar"] * {
        font-family: 'Space Mono', monospace !important;
    }

    .sidebar-logo {
        font-family: 'Space Mono', monospace;
        font-size: 0.7rem;
        color: #444;
        letter-spacing: 0.15em;
        text-transform: uppercase;
        padding: 0 0 1.5rem 0;
        border-bottom: 1px solid #2e2e2e;
        margin-bottom: 1.5rem;
    }

    .sidebar-name {
        font-family: 'Syne', sans-serif;
        font-weight: 800;
        font-size: 1.1rem;
        color: #fff;
        margin-bottom: 0.2rem;
    }

    .sidebar-title {
        font-family: 'Space Mono', monospace;
        font-size: 0.65rem;
        color: #555;
        letter-spacing: 0.1em;
        text-transform: uppercase;
    }

    .nav-link {
        display: block;
        padding: 10px 14px;
        margin: 4px 0;
        border-radius: 4px;
        font-family: 'Space Mono', monospace;
        font-size: 0.75rem;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        color: #666;
        text-decoration: none;
        border: 1px solid transparent;
        transition: all 0.2s ease;
    }

    .nav-link:hover, .nav-link.active {
        color: #fff;
        border-color: #353535;
        background: #2a2a2a;
        transform: translateX(4px);
    }

    .social-btn {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        padding: 9px 16px;
        margin: 4px 0;
        width: 100%;
        border-radius: 4px;
        font-family: 'Space Mono', monospace;
        font-size: 0.7rem;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        text-decoration: none;
        border: 1px solid #3a3a3a;
        color: #aaa;
        background: #1e1e1e;
        transition: all 0.2s;
        box-sizing: border-box;
    }

    .social-btn:hover {
        border-color: #fff;
        color: #fff;
        background: #2a2a2a;
        text-decoration: none;
    }

    /* ===== HERO ===== */
    .hero-section {
        padding: 3rem 0 2rem 0;
        border-bottom: 1px solid #222222;
        margin-bottom: 3rem;
        animation: fadeInUp 0.7s ease both;
    }

    .hero-eyebrow {
        font-family: 'Space Mono', monospace;
        font-size: 0.7rem;
        letter-spacing: 0.25em;
        text-transform: uppercase;
        color: #fff;
        background: #222222;
        border: 1px solid #353535;
        display: inline-block;
        padding: 5px 12px;
        border-radius: 2px;
        margin-bottom: 1.5rem;
        animation: slideDown 0.5s ease both;
    }

    .hero-name {
        font-family: 'Syne', sans-serif;
        font-weight: 800;
        font-size: clamp(2.8rem, 6vw, 5rem);
        color: #ffffff;
        line-height: 1.05;
        letter-spacing: -0.02em;
        margin: 0 0 0.5rem 0;
        animation: fadeInUp 0.6s ease 0.15s both;
    }

    .hero-name::after {
        content: '_';
        animation: cursorBlink 1.1s step-end infinite;
        color: #555;
        font-weight: 400;
    }

    .hero-role {
        font-family: 'Space Mono', monospace;
        font-size: 0.9rem;
        color: #555;
        letter-spacing: 0.05em;
        margin-bottom: 1.5rem;
        animation: fadeInUp 0.6s ease 0.28s both;
    }

    .hero-desc {
        font-size: 1.05rem;
        color: #888;
        line-height: 1.75;
        max-width: 520px;
        font-weight: 400;
        animation: fadeInUp 0.6s ease 0.4s both;
    }

    .stat-item {
        display: inline-block;
        margin-right: 2.5rem;
        margin-top: 1.5rem;
        animation: countUp 0.5s ease both;
    }

    .stat-item:nth-child(1) { animation-delay: 0.5s; }
    .stat-item:nth-child(2) { animation-delay: 0.65s; }
    .stat-item:nth-child(3) { animation-delay: 0.8s; }

    .stat-num {
        font-family: 'Space Mono', monospace;
        font-size: 2rem;
        font-weight: 700;
        color: #fff;
        display: block;
        line-height: 1;
    }

    .stat-lbl {
        font-family: 'Space Mono', monospace;
        font-size: 0.65rem;
        color: #444;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        margin-top: 4px;
    }

    .profile-img-wrap {
        display: flex;
        align-items: center;
        justify-content: center;
        height: 100%;
    }

    .profile-img-wrap img {
        border-radius: 4px !important;
        filter: grayscale(20%) contrast(1.05);
        border: 1px solid #222;
    }

    /* ===== SECTION HEADERS ===== */
    .sec-label {
        font-family: 'Space Mono', monospace;
        font-size: 0.65rem;
        color: #444;
        letter-spacing: 0.25em;
        text-transform: uppercase;
        margin-bottom: 0.3rem;
        animation: fadeIn 0.5s ease both;
    }

    .sec-title {
        font-family: 'Syne', sans-serif;
        font-weight: 800;
        font-size: 2rem;
        color: #fff;
        margin: 0 0 2rem 0;
        letter-spacing: -0.01em;
        animation: fadeInUp 0.5s ease 0.1s both;
    }

    /* ===== CARDS ===== */
    .card {
        background: #222222;
        border: 1px solid #303030;
        border-radius: 6px;
        padding: 1.75rem;
        margin-bottom: 1rem;
        transition: border-color 0.25s ease, transform 0.25s ease, box-shadow 0.25s ease;
        animation: fadeInUp 0.5s ease both;
    }

    .card:hover {
        border-color: #555;
        transform: translateY(-3px);
        box-shadow: 0 8px 30px rgba(0,0,0,0.4);
    }

    .card-title {
        font-family: 'Syne', sans-serif;
        font-weight: 700;
        font-size: 1.15rem;
        color: #fff;
        margin-bottom: 0.3rem;
    }

    .card-meta {
        font-family: 'Space Mono', monospace;
        font-size: 0.7rem;
        color: #555;
        letter-spacing: 0.05em;
        margin-bottom: 1rem;
    }

    .card-body {
        color: #888;
        font-size: 0.92rem;
        line-height: 1.7;
    }

    .card-body ul {
        padding-left: 1.2rem;
        margin: 0;
    }

    .card-body li {
        color: #888;
        margin-bottom: 0.5rem;
        font-size: 0.92rem;
    }

    /* ===== WORK TIMELINE ===== */
    .timeline-item {
        position: relative;
        padding: 1.75rem;
        background: #222222;
        border: 1px solid #303030;
        border-radius: 6px;
        margin-bottom: 1rem;
        transition: border-color 0.25s ease, transform 0.25s ease, box-shadow 0.25s ease;
        animation: fadeInLeft 0.5s ease both;
    }

    .timeline-item:nth-child(1) { animation-delay: 0.05s; }
    .timeline-item:nth-child(2) { animation-delay: 0.15s; }
    .timeline-item:nth-child(3) { animation-delay: 0.25s; }

    .timeline-item:hover {
        border-color: #555;
        transform: translateX(6px);
        box-shadow: 0 4px 20px rgba(0,0,0,0.35);
    }

    .tl-company {
        font-family: 'Space Mono', monospace;
        font-size: 0.65rem;
        letter-spacing: 0.15em;
        text-transform: uppercase;
        color: #fff;
        background: #2e2e2e;
        border: 1px solid #303030;
        display: inline-block;
        padding: 3px 10px;
        border-radius: 2px;
        margin-bottom: 0.8rem;
    }

    .tl-role {
        font-family: 'Syne', sans-serif;
        font-weight: 700;
        font-size: 1.2rem;
        color: #fff;
        margin-bottom: 0.2rem;
    }

    .tl-date {
        font-family: 'Space Mono', monospace;
        font-size: 0.68rem;
        color: #444;
        letter-spacing: 0.08em;
        margin-bottom: 1rem;
    }

    .tl-current {
        font-family: 'Space Mono', monospace;
        font-size: 0.6rem;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        color: #000;
        background: #fff;
        padding: 2px 8px;
        border-radius: 2px;
        margin-left: 0.75rem;
        vertical-align: middle;
    }

    /* ===== SKILL TAGS ===== */
    .tag {
        display: inline-block;
        padding: 5px 12px;
        margin: 4px 3px;
        background: #222222;
        border: 1px solid #353535;
        border-radius: 3px;
        color: #888;
        font-family: 'Space Mono', monospace;
        font-size: 0.7rem;
        letter-spacing: 0.05em;
        transition: all 0.15s;
    }

    .tag:hover {
        border-color: #fff;
        color: #fff;
    }

    /* ===== SKILL CATEGORY ===== */
    .skill-category {
        margin-bottom: 1.25rem;
    }

    .skill-cat-label {
        font-family: 'Space Mono', monospace;
        font-size: 0.62rem;
        letter-spacing: 0.18em;
        text-transform: uppercase;
        color: #555;
        margin-bottom: 0.5rem;
        padding-bottom: 0.4rem;
        border-bottom: 1px solid #222222;
    }

    /* ===== PROJECT CARD ===== */

    .proj-num {
        font-family: 'Space Mono', monospace;
        font-size: 0.62rem;
        color: #333;
        letter-spacing: 0.1em;
        margin-bottom: 0.75rem;
    }

    .proj-title {
        font-family: 'Syne', sans-serif;
        font-weight: 700;
        font-size: 1.1rem;
        color: #fff;
        margin-bottom: 0.5rem;
    }

    .proj-desc {
        color: #666;
        font-size: 0.88rem;
        line-height: 1.65;
        margin-bottom: 1rem;
    }

    .proj-btn {
        display: inline-block;
        padding: 7px 16px;
        margin: 0 6px 4px 0;
        border: 1px solid #353535;
        border-radius: 3px;
        font-family: 'Space Mono', monospace;
        font-size: 0.65rem;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        color: #888;
        text-decoration: none;
        transition: all 0.2s;
    }

    .proj-btn:hover {
        border-color: #fff;
        color: #fff;
        text-decoration: none;
    }

    /* ===== CERT CARD ===== */
    .cert-card {
        background: #222222;
        border: 1px solid #303030;
        border-radius: 6px;
        padding: 1.25rem 1.5rem;
        margin-bottom: 0.75rem;
        display: flex;
        align-items: center;
        justify-content: space-between;
        transition: border-color 0.25s ease, transform 0.25s ease;
        animation: fadeInUp 0.4s ease both;
    }

    .cert-card:hover {
        border-color: #555;
        transform: translateX(4px);
    }

    .cert-name {
        font-family: 'Syne', sans-serif;
        font-weight: 600;
        font-size: 0.92rem;
        color: #ddd;
    }

    .cert-issuer {
        font-family: 'Space Mono', monospace;
        font-size: 0.62rem;
        color: #444;
        letter-spacing: 0.08em;
        margin-top: 3px;
    }

    .cert-link {
        font-family: 'Space Mono', monospace;
        font-size: 0.62rem;
        color: #555;
        text-decoration: none;
        border: 1px solid #222;
        padding: 5px 12px;
        border-radius: 3px;
        white-space: nowrap;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        transition: all 0.2s;
    }

    .cert-link:hover {
        color: #fff;
        border-color: #fff;
        text-decoration: none;
    }

    /* ===== CONTACT ===== */
    .contact-card {
        background: #222222;
        border: 1px solid #303030;
        border-radius: 6px;
        padding: 2rem;
        margin-bottom: 1rem;
        text-align: center;
        transition: border-color 0.25s ease, transform 0.25s ease, box-shadow 0.25s ease;
        animation: fadeInUp 0.5s ease both;
    }

    .contact-card:hover {
        border-color: #555;
        transform: translateY(-4px);
        box-shadow: 0 10px 30px rgba(0,0,0,0.4);
    }

    .contact-icon {
        font-size: 1.8rem;
        margin-bottom: 0.75rem;
        display: block;
    }

    .contact-label {
        font-family: 'Syne', sans-serif;
        font-weight: 700;
        font-size: 1rem;
        color: #fff;
        margin-bottom: 0.4rem;
    }

    .contact-sub {
        font-family: 'Space Mono', monospace;
        font-size: 0.68rem;
        color: #555;
        margin-bottom: 1.25rem;
        line-height: 1.6;
    }

    .contact-btn {
        display: inline-block;
        padding: 9px 22px;
        border: 1px solid #353535;
        border-radius: 3px;
        font-family: 'Space Mono', monospace;
        font-size: 0.65rem;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        color: #888;
        text-decoration: none;
        transition: all 0.2s;
    }

    .contact-btn:hover {
        border-color: #fff;
        color: #fff;
        text-decoration: none;
    }

    /* ===== FORM OVERRIDES ===== */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea {
        background-color: #222222 !important;
        border: 1px solid #222 !important;
        border-radius: 4px !important;
        color: #fff !important;
        font-family: 'Space Mono', monospace !important;
        font-size: 0.82rem !important;
    }

    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus {
        border-color: #555 !important;
        box-shadow: none !important;
    }

    .stTextInput label, .stTextArea label {
        font-family: 'Space Mono', monospace !important;
        font-size: 0.7rem !important;
        letter-spacing: 0.08em !important;
        color: #555 !important;
        text-transform: uppercase !important;
    }

    div[data-testid="stFormSubmitButton"] button {
        background: #fff !important;
        color: #000 !important;
        border: none !important;
        font-family: 'Space Mono', monospace !important;
        font-size: 0.72rem !important;
        letter-spacing: 0.12em !important;
        text-transform: uppercase !important;
        padding: 10px 28px !important;
        border-radius: 3px !important;
        transition: all 0.2s !important;
    }

    div[data-testid="stFormSubmitButton"] button:hover {
        background: #ddd !important;
    }

    /* Radio override */
    .stRadio label {
        font-family: 'Space Mono', monospace !important;
        font-size: 0.72rem !important;
        color: #666 !important;
    }

    /* Divider */
    hr {
        border: none !important;
        border-top: 1px solid #222222 !important;
        margin: 2rem 0 !important;
    }

    /* About competency card */
    .comp-card {
        background: #222222;
        border: 1px solid #303030;
        border-radius: 6px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        transition: border-color 0.25s ease, transform 0.25s ease, box-shadow 0.25s ease;
        animation: fadeInUp 0.5s ease both;
    }

    .comp-card:hover {
        border-color: #555;
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.35);
    }

    .comp-icon {
        font-size: 1.4rem;
        margin-bottom: 0.6rem;
    }

    .comp-title {
        font-family: 'Syne', sans-serif;
        font-weight: 700;
        font-size: 0.95rem;
        color: #fff;
        margin-bottom: 0.4rem;
    }

    .comp-desc {
        font-size: 0.85rem;
        color: #666;
        line-height: 1.6;
    }

    /* ===== PROJECT CARD ===== */
    .proj-card {
        background: #222222;
        border: 1px solid #303030;
        border-radius: 6px;
        padding: 1.75rem;
        margin-bottom: 1.25rem;
        transition: border-color 0.25s ease, transform 0.25s ease, box-shadow 0.25s ease;
        animation: fadeInUp 0.5s ease both;
    }

    .proj-card:hover {
        border-color: #666;
        transform: translateY(-4px);
        box-shadow: 0 12px 35px rgba(0,0,0,0.45);
    }

    .footer-text {
        font-family: 'Space Mono', monospace;
        font-size: 0.62rem;
        color: #333;
        letter-spacing: 0.1em;
        text-align: center;
        padding: 2rem 0;
    }
</style>
""", unsafe_allow_html=True)

# ===== SIDEBAR =====
with st.sidebar:
    st.markdown("""
        <div class="sidebar-logo">Portfolio · 2023</div>
        <div class="sidebar-name">Muhammad Tayyab</div>
        <div class="sidebar-title">Data Scientist & ML Engineer</div>
        <br>
    """, unsafe_allow_html=True)

    nav_choice = st.radio(
        'Navigation',
        ['Home', 'Resume', 'Projects', 'Contact'],
        label_visibility='collapsed'
    )

    st.markdown("<hr>", unsafe_allow_html=True)

    st.markdown(f"""
        <a href="{LINKEDIN_URL}" target="_blank" class="social-btn">↗ LinkedIn</a>
        <a href="{GITHUB_URL}" target="_blank" class="social-btn">↗ GitHub</a>
        <a href="mailto:{EMAIL}" class="social-btn">↗ Email</a>
    """, unsafe_allow_html=True)


# ===== HOME PAGE =====
if nav_choice == 'Home':
    col1, col2 = st.columns([3, 2])

    with col1:
        st.markdown("""
            <div class="hero-section">
                <div class="hero-eyebrow">◈ Available for opportunities</div>
                <h1 class="hero-name">Muhammad<br>Tayyab</h1>
                <div class="hero-role">DATA SCIENTIST / ML ENGINEER / DESIGN ENGINEER</div>
                <p class="hero-desc">
                    Building intelligent systems that extract meaning from data. 
                    Specialized in deep learning, computer vision, NLP, and 
                    end-to-end ERP solutions.
                </p>
                <div>
                    <div class="stat-item">
                        <span class="stat-num">25+</span>
                        <span class="stat-lbl">Projects</span>
                    </div>
                    <div class="stat-item">
                        <span class="stat-num">3+</span>
                        <span class="stat-lbl">Years Experience</span>
                    </div>
                    <div class="stat-item">
                        <span class="stat-num">20+</span>
                        <span class="stat-lbl">Certifications</span>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        try:
            st.image('Images/me.png', width='stretch')
        except:
            st.markdown("""
                <div style="background:#222222;border:1px solid #303030;border-radius:6px;
                height:320px;display:flex;align-items:center;justify-content:center;">
                    <span style="color:#333;font-family:'Space Mono',monospace;font-size:0.7rem;">
                        PHOTO
                    </span>
                </div>
            """, unsafe_allow_html=True)

    # About
    st.markdown("""
        <div class="sec-label">About</div>
        <div class="sec-title">Who I Am</div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="card">
            <div class="card-body">
                Highly motivated Data Scientist and Design Engineer with a passion for machine 
                learning and artificial intelligence. Currently at the Center for Advanced Research 
                in Engineering, I design ERP workflows, system architectures, and data-driven 
                solutions. My work spans deep learning systems, computer vision, NLP applications, 
                and enterprise software.<br><br>
                I believe in the power of clean code, reproducible workflows, and continuous learning. 
                Whether contributing to open-source or building production systems, I'm always pushing 
                what's possible.
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Core Competencies
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
        <div class="sec-label">Expertise</div>
        <div class="sec-title">Core Competencies</div>
    """, unsafe_allow_html=True)

    cols = st.columns(2)
    competencies = [
        ("🤖", "Machine Learning", "Supervised & unsupervised learning, feature engineering, model optimization. Proficient in scikit-learn, XGBoost, and ensemble methods."),
        ("👁", "Computer Vision", "Image classification, object detection, video analysis using CNNs. Skilled with OpenCV, TensorFlow, and transfer learning."),
        ("🧠", "Deep Learning", "CNNs, RNNs, BiLSTMs, and transformer architectures. Hands-on with TensorFlow and Keras for complex model development."),
        ("💬", "NLP & LLMs", "Text processing, sentiment analysis, and LLM-powered applications. Experience with transformers, BERT, and GPT-based workflows."),
        ("🗄", "ERP Systems", "End-to-end ERP design and implementation. Database management, workflow automation, dashboards, and reporting."),
        ("📊", "Data Analytics", "SQL-based analysis, ETL pipelines, Power BI dashboards, and business intelligence reporting."),
    ]

    for i, (icon, title, desc) in enumerate(competencies):
        with cols[i % 2]:
            st.markdown(f"""
                <div class="comp-card">
                    <div class="comp-icon">{icon}</div>
                    <div class="comp-title">{title}</div>
                    <div class="comp-desc">{desc}</div>
                </div>
            """, unsafe_allow_html=True)


# ===== RESUME PAGE =====
elif nav_choice == 'Resume':
    st.markdown("""
        <div class="sec-label">Resume</div>
        <div class="sec-title">Experience & Skills</div>
    """, unsafe_allow_html=True)

    # Work Experience
    st.markdown("""
        <div class="sec-label">Work Experience</div>
        <h3 style="font-family:'Syne',sans-serif;color:#888;font-weight:600;font-size:1.1rem;margin:0 0 1.25rem 0;">
            Career Timeline
        </h3>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="timeline-item">
            <div class="tl-company">Center for Advanced Research in Engineering · Islamabad</div>
            <div class="tl-role">Design Engineer <span class="tl-current">Current</span></div>
            <div class="tl-date">DEC 2025 – PRESENT</div>
            <div class="card-body">
                <ul>
                    <li>Collaborate with clients to gather business requirements and design ERP workflows and system architectures.</li>
                    <li>Guide implementation teams to deliver scalable, business-aligned enterprise solutions.</li>
                </ul>
            </div>
        </div>

        <div class="timeline-item">
            <div class="tl-company">Center for Advanced Research in Engineering · Islamabad</div>
            <div class="tl-role">Implementation Engineer</div>
            <div class="tl-date">DEC 2023 – DEC 2025</div>
            <div class="card-body">
                <ul>
                    <li>Developed and implemented end-to-end ERP systems by building workflows, databases, and automated reports.</li>
                    <li>Created interactive dashboards to support operational and analytical needs.</li>
                    <li>Customized forms in Joget using JavaScript, HTML, and CSS; built dynamic reports with Jasper.</li>
                    <li>Applied strong analytical skills to ensure data accuracy and optimize system functionality.</li>
                </ul>
            </div>
        </div>

        <div class="timeline-item">
            <div class="tl-company">Kashmir Wood Industries PVT. LTD. · Faisalabad</div>
            <div class="tl-role">Data Science Intern</div>
            <div class="tl-date">NOV 2022 – APR 2023</div>
            <div class="card-body">
                <ul>
                    <li>Performed end-to-end data science workflows including data cleaning, preprocessing, exploratory analysis, feature engineering, visualization, and ML model development.</li>
                    <li>Delivered machine learning solutions aligned with client requirements.</li>
                    <li>Documented project workflows and methodologies to ensure clarity, reproducibility, and effective knowledge transfer.</li>
                </ul>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    # Education
    st.markdown("""
        <div class="sec-label">Education</div>
        <h3 style="font-family:'Syne',sans-serif;color:#888;font-weight:600;font-size:1.1rem;margin:0 0 1.25rem 0;">
            Academic Background
        </h3>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="card">
            <div class="card-title">Bachelor of Science in Computer Science</div>
            <div class="card-meta">RIPHAH INTERNATIONAL UNIVERSITY, FAISALABAD · 2018 – 2022 · GPA: 3.59/4.0</div>
            <div class="card-body">
                Strong foundation in computer science fundamentals, data structures, algorithms, 
                and specialized coursework in machine learning and artificial intelligence.
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    # Skills
    st.markdown("""
        <div class="sec-label">Skills</div>
        <h3 style="font-family:'Syne',sans-serif;color:#888;font-weight:600;font-size:1.1rem;margin:0 0 1.25rem 0;">
            Technical Stack
        </h3>
    """, unsafe_allow_html=True)

    skills_dict = {
        "Languages": ["Python", "Java", "JavaScript", "SQL"],
        "Data": ["Pandas", "NumPy", "Statistical Analysis", "Feature Engineering"],
        "Machine Learning": ["Scikit-Learn", "XGBoost", "Collaborative Filtering"],
        "Deep Learning": ["TensorFlow", "Keras", "PyTorch", "Conv3D", "BiLSTM", "CTC Loss"],
        "Computer Vision": ["OpenCV", "CNN", "Image Classification", "Transfer Learning"],
        "NLP": ["BERT", "Transformers", "LangChain", "GPT APIs", "Text Processing"],
        "Visualization": ["Matplotlib", "Seaborn", "Plotly", "PowerBI"],
        "Databases": ["MySQL", "SQL Server", "PostgreSQL"],
        "Tools": ["Git/GitHub", "Jupyter", "Google Colab", "Streamlit", "Jasper", "Joget"],
        "Web": ["HTML/CSS", "RESTful APIs", "Beautiful Soup"],
    }

    cols = st.columns(2)
    items = list(skills_dict.items())
    half = (len(items) + 1) // 2

    for col_idx, col in enumerate(cols):
        with col:
            for cat, skills in items[col_idx * half:(col_idx + 1) * half]:
                tags_html = ''.join([f'<span class="tag">{s}</span>' for s in skills])
                st.markdown(f"""
                    <div class="skill-category">
                        <div class="skill-cat-label">{cat}</div>
                        <div>{tags_html}</div>
                    </div>
                """, unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    # Certifications
    st.markdown("""
        <div class="sec-label">Certifications</div>
        <h3 style="font-family:'Syne',sans-serif;color:#888;font-weight:600;font-size:1.1rem;margin:0 0 1.25rem 0;">
            Credentials
        </h3>
    """, unsafe_allow_html=True)

    certifications = [
        {"name": "Google Advanced Data Analytics", "issuer": "Coursera · Sep 2023", "url": "https://coursera.org/verify/professional-cert/3VGYLML6U8ZC/"},
        {"name": "SQL for Data Science", "issuer": "Coursera · Jun 2022", "url": "https://coursera.org/verify/KB4FA685KYNJ/"},
        {"name": "Statistics", "issuer": "365 Data Science · Oct 2022", "url": "https://learn.365datascience.com/certificates/CC-EC4896E8AD/"},
        {"name": "Machine Learning in Python", "issuer": "365 Data Science", "url": "https://learn.365datascience.com/certificates/CC-F2AC711D5E/"},
        {"name": "Scientific Computing with Python", "issuer": "freeCodeCamp", "url": "https://www.freecodecamp.org/certification/Tayyab885/scientific-computing-with-python-v7"},
        {"name": "Applied Data Science with Python", "issuer": "Simplilearn", "url": "https://www.simplilearn.com/skillup-certificate-landing?token=eyJjb3Vyc2VfaWQiOiI2ODQiLCJjZXJ0aWZpY2F0ZV91cmwiOiJodHRwczpcL1wvY2VydGlmaWNhdGVzLnNpbXBsaWNkbi5uZXRcL3NoYXJlXC90aHVtYl8zODQ4NjI4XzE2NjU1ODk4NTMucG5nIiwidXNlcm5hbWUiOiJNdWhhbW1hZCBUYXl5YWIifQ%3D%3D&utm_source=shared-certificate&utm_medium=lms&utm_campaign=shared-certificate-promotion"},
        {"name": "Python (Basic)", "issuer": "HackerRank · Jun 2022", "url": "https://www.hackerrank.com/certificates/9ce1e3043a5a"},
        {"name": "SQL (Basic)", "issuer": "HackerRank", "url": "https://www.hackerrank.com/certificates/a2a976e2c4bc"},
    ]

    for cert in certifications:
        st.markdown(f"""
            <div class="cert-card">
                <div>
                    <div class="cert-name">{cert['name']}</div>
                    <div class="cert-issuer">{cert['issuer']}</div>
                </div>
                <a href="{cert['url']}" target="_blank" class="cert-link">View ↗</a>
            </div>
        """, unsafe_allow_html=True)


# ===== PROJECTS PAGE =====
elif nav_choice == 'Projects':
    st.markdown("""
        <div class="sec-label">Portfolio</div>
        <div class="sec-title">Selected Projects</div>
    """, unsafe_allow_html=True)

    projects = [
        {
            "title": "Lip Reading Using Deep Learning",
            "desc": "End-to-end deep learning lip-reading system for speech recognition in low-audio environments. Built with Conv3D and Bidirectional LSTM layers with CTC loss for sequence alignment, trained on aligned video datasets, and deployed via an interactive Streamlit application.",
            "tech": ["TensorFlow", "Conv3D", "BiLSTM", "CTC Loss", "Streamlit", "Computer Vision"],
            "github": "https://github.com/Tayyab885/Lip-Reading-Project-Using-Deep-Learning",
            "demo": None
        },
        {
            "title": "AutoGPT YouTube Title and Script Generator",
            "desc": "AI-powered content creation tool using OpenAI GPT to automatically generate YouTube titles and full video scripts. Integrates Wikipedia for real-time research, tracks conversation history for context, and features an intuitive Streamlit interface for creators.",
            "tech": ["OpenAI GPT", "LangChain", "Python", "Streamlit", "NLP"],
            "github": "https://github.com/Tayyab885/AutoGPT-YouTube-Title-and-Script-Generator",
            "demo": None
        },
        {
            "title": "Stock Market Prediction Using LSTM",
            "desc": "Time series forecasting system for stock prices using LSTM neural networks. Features MinMax scaling, a sliding window approach, and comprehensive preprocessing. Generates 30-day future forecasts with confidence intervals and interactive visualizations for financial analysis.",
            "tech": ["LSTM", "TensorFlow", "Keras", "Time Series", "Finance", "Pandas"],
            "github": "https://github.com/Tayyab885/Stock-Price-Prediction-And-Forecasting-Using-LSTM",
            "demo": None
        },
        {
            "title": "Cotton Plant Disease Prediction",
            "desc": "Deep learning plant disease classification system achieving 87% accuracy on cotton leaf images. Led the full pipeline from dataset collection and image augmentation to CNN architecture design, model training, evaluation, and production deployment using TensorFlow and Keras.",
            "tech": ["CNN", "TensorFlow", "Keras", "Image Classification", "Agriculture AI", "OpenCV"],
            "github": "https://github.com/Tayyab885/Cotton-Disease-Prediction",
            "demo": None
        },
        {
            "title": "Chronic Kidney Disease Prediction",
            "desc": "AutoML web application for predicting chronic kidney disease with 98% accuracy using Random Forest, SVM, and Logistic Regression. Includes automated data cleaning, EDA pipeline, and interactive visualizations. Deployed publicly on Streamlit Cloud for open access.",
            "tech": ["AutoML", "Scikit-learn", "Pandas", "Streamlit", "Healthcare AI", "EDA"],
            "github": "https://github.com/Tayyab885/Chronic_Kidney_DIsease_Prediction",
            "demo": "https://tayyab885-chronic-kidney-disease-prediction-app-s4cofm.streamlit.app/"
        },
        {
            "title": "Book Recommendation System",
            "desc": "Collaborative filtering recommendation engine delivering personalized book suggestions using instance-based cosine similarity scoring. Features a searchable database with book metadata and ratings, generating top-N recommendations based on reading history via a clean Streamlit interface.",
            "tech": ["Collaborative Filtering", "Machine Learning", "Streamlit", "Python", "Cosine Similarity"],
            "github": "https://github.com/Tayyab885/BookRecommendationSystem",
            "demo": None
        },
        {
            "title": "Superstore Sales Analysis",
            "desc": "Comprehensive sales analytics project combining Python preprocessing with SQL-based business intelligence. Identified customer behavior patterns, revenue drivers, and shipping bottlenecks. Data-driven recommendations contributed to an approximate 5% sales increase with an interactive Streamlit dashboard.",
            "tech": ["SQL", "Python", "Pandas", "Power BI", "Business Intelligence", "Streamlit"],
            "github": "https://github.com/Tayyab885/Superstore-Sales-Analysis",
            "demo": None
        },
        {
            "title": "COVID-19 Data Analysis Using SQL",
            "desc": "In-depth SQL analysis of global COVID-19 data covering infection rates, death percentages, vaccination rollout statistics, and regional pandemic trends. Used CTEs and window functions to calculate country-wise metrics and produce insights for data-driven public health decision-making.",
            "tech": ["SQL", "Data Analysis", "Statistics", "Public Health", "CTEs", "Window Functions"],
            "github": "https://github.com/Tayyab885/Covid-19-Data-Analysis-Using-SQL",
            "demo": None
        },
        {
            "title": "Nashville Housing Data Cleaning Using SQL",
            "desc": "Comprehensive data cleaning project on Nashville housing dataset using advanced SQL. Standardized date formats, parsed and split address fields, handled NULL values, removed duplicate records using ROW_NUMBER(), and dropped redundant columns to produce a clean, analysis-ready dataset.",
            "tech": ["SQL", "Data Cleaning", "ETL", "Data Transformation", "Window Functions"],
            "github": "https://github.com/Tayyab885/Nashville-Housing-Data-Cleaning-Using-SQL",
            "demo": None
        },
    ]

    col1, col2 = st.columns(2)
    for i, proj in enumerate(projects):
        col = col1 if i % 2 == 0 else col2
        with col:
            tags_html = ''.join([f'<span class="tag">{t}</span>' for t in proj['tech']])
            demo_btn = f'<a href="{proj["demo"]}" target="_blank" class="proj-btn">Live Demo</a>' if proj.get('demo') else ''
            st.markdown(f"""<div class="proj-card">
<div class="proj-num">PROJECT {str(i+1).zfill(2)}</div>
<div class="proj-title">{proj['title']}</div>
<div class="proj-desc">{proj['desc']}</div>
<div style="margin:0.75rem 0 1rem 0">{tags_html}</div>
<a href="{proj['github']}" target="_blank" class="proj-btn">GitHub</a> {demo_btn}
</div>""", unsafe_allow_html=True)

    st.markdown(f"""
        <div style="text-align:center;padding:2.5rem;background:#222222;border:1px solid #2e2e2e;
             border-radius:6px;margin-top:1rem;">
            <div style="font-family:'Space Mono',monospace;font-size:0.65rem;color:#444;
                 letter-spacing:0.2em;text-transform:uppercase;margin-bottom:0.75rem;">
                More Projects
            </div>
            <div style="font-family:'Syne',sans-serif;font-size:1.5rem;font-weight:800;
                 color:#fff;margin-bottom:0.75rem;">
                See Everything on GitHub
            </div>
            <a href="{GITHUB_URL}" target="_blank" class="proj-btn" style="font-size:0.72rem;padding:10px 24px;">
                Visit Profile ↗
            </a>
        </div>
    """, unsafe_allow_html=True)


# ===== CONTACT PAGE =====
elif nav_choice == 'Contact':
    st.markdown("""
        <div class="sec-label">Contact</div>
        <div class="sec-title">Get In Touch</div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(f"""
            <div class="contact-card">
                <span class="contact-icon">↗</span>
                <div class="contact-label">LinkedIn</div>
                <div class="contact-sub">Professional networking and career opportunities</div>
                <a href="{LINKEDIN_URL}" target="_blank" class="contact-btn">Connect</a>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
            <div class="contact-card">
                <span class="contact-icon">⌨</span>
                <div class="contact-label">GitHub</div>
                <div class="contact-sub">Code, projects, and open source contributions</div>
                <a href="{GITHUB_URL}" target="_blank" class="contact-btn">View Profile</a>
            </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
            <div class="contact-card">
                <span class="contact-icon">@</span>
                <div class="contact-label">Email</div>
                <div class="contact-sub">Project inquiries, collaborations, or just hello</div>
                <a href="mailto:{EMAIL}" class="contact-btn">Send Email</a>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    st.markdown("""
        <div style="font-family:'Space Mono',monospace;font-size:0.65rem;color:#444;
             letter-spacing:0.2em;text-transform:uppercase;margin-bottom:0.4rem;">
            Direct Message
        </div>
        <div style="font-family:'Syne',sans-serif;font-weight:800;font-size:1.5rem;
             color:#fff;margin-bottom:1.5rem;">
            Send a Message
        </div>
    """, unsafe_allow_html=True)

    with st.form("contact_form"):
        c1, c2 = st.columns(2)
        with c1:
            name = st.text_input("Name", placeholder="Your name")
            email_in = st.text_input("Email", placeholder="your@email.com")
        with c2:
            subject = st.text_input("Subject", placeholder="Project inquiry")
            phone = st.text_input("Phone (optional)", placeholder="+92 300 0000000")

        message = st.text_area("Message", placeholder="Tell me about your project...", height=160)
        submitted = st.form_submit_button("Send Message")

        if submitted:
            if name and email_in and subject and message:
                st.success("Message sent — I'll get back to you shortly.")
            else:
                st.error("Please fill in all required fields.")

    st.markdown("<hr>", unsafe_allow_html=True)

    st.markdown("""
        <div style="font-family:'Space Mono',monospace;font-size:0.65rem;color:#444;
             letter-spacing:0.2em;text-transform:uppercase;margin-bottom:0.4rem;">
            Looking For
        </div>
        <div style="font-family:'Syne',sans-serif;font-weight:800;font-size:1.5rem;
             color:#fff;margin-bottom:1.5rem;">
            Open To
        </div>
    """, unsafe_allow_html=True)

    oc1, oc2, oc3 = st.columns(3)
    open_to = [
        ("◈", "Exciting Projects", "ML/AI challenges that push boundaries and solve real-world problems."),
        ("◉", "Career Opportunities", "Full-time roles, freelance work, or consulting in data science and ML."),
        ("◌", "Learning & Growth", "Open source, mentorship, research collaboration, and knowledge sharing."),
    ]

    for col, (icon, title, desc) in zip([oc1, oc2, oc3], open_to):
        with col:
            st.markdown(f"""
                <div class="contact-card">
                    <span class="contact-icon" style="font-size:1.4rem;">{icon}</span>
                    <div class="contact-label">{title}</div>
                    <div class="contact-sub">{desc}</div>
                </div>
            """, unsafe_allow_html=True)

    st.markdown("""
        <div class="footer-text">
            Muhammad Tayyab · m.tayyab273@gmail.com · Faisalabad, Pakistan · © 2023
        </div>
    """, unsafe_allow_html=True)
