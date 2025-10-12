import streamlit as st

# Contact Information
LINKEDIN_URL = 'https://www.linkedin.com/in/muhammad-tayyab-9b965b1b1/'
GITHUB_URL = 'https://github.com/Tayyab885'
EMAIL = 'your.email@example.com'  # Add your email

# Page Configuration
st.set_page_config(
    page_title='Muhammad Tayyab | Data Scientist',
    page_icon='🚀',
    layout='wide',
    initial_sidebar_state='expanded'
)

# Custom CSS with Modern Design
st.markdown("""
<style>
    /* Global Styles */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #0f172a 100%);
    }
    
    /* Hide Streamlit Default Elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Gradient Text */
    .gradient-text {
        background: linear-gradient(90deg, #60a5fa, #a78bfa, #f472b6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 3.5rem;
        font-weight: 900;
        display: inline-block;
        animation: float 3s ease-in-out infinite;
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }
    
    /* Section Headers */
    .section-header {
        color: #60a5fa;
        font-size: 2.5rem;
        font-weight: bold;
        margin: 40px 0 20px 0;
        padding-bottom: 10px;
        border-bottom: 3px solid #60a5fa;
    }
    
    /* Glass Card Effect */
    .glass-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 25px;
        margin: 20px 0;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .glass-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 40px 0 rgba(96, 165, 250, 0.3);
    }
    
    /* Project Card */
    .project-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 20px;
        margin: 15px 0;
        transition: all 0.3s ease;
    }
    
    .project-card:hover {
        transform: translateY(-5px);
        border: 1px solid rgba(96, 165, 250, 0.5);
        box-shadow: 0 10px 30px rgba(96, 165, 250, 0.2);
    }
    
    .project-title {
        color: #a78bfa;
        font-size: 1.8rem;
        font-weight: bold;
        margin-bottom: 15px;
    }
    
    .project-desc {
        color: #e5e7eb;
        font-size: 1rem;
        line-height: 1.6;
        margin-bottom: 10px;
    }
    
    /* Custom Buttons */
    .custom-button {
        display: inline-block;
        padding: 12px 30px;
        margin: 5px;
        background: linear-gradient(90deg, #2563eb, #7c3aed);
        color: white;
        text-decoration: none;
        border-radius: 25px;
        font-weight: bold;
        transition: all 0.3s ease;
        border: none;
        box-shadow: 0 4px 15px rgba(37, 99, 235, 0.3);
    }
    
    .custom-button:hover {
        transform: scale(1.05);
        box-shadow: 0 6px 20px rgba(37, 99, 235, 0.5);
        text-decoration: none;
        color: white;
    }
    
    .github-button {
        background: linear-gradient(90deg, #334155, #475569);
    }
    
    .github-button:hover {
        box-shadow: 0 6px 20px rgba(71, 85, 105, 0.5);
    }
    
    .linkedin-button {
        background: linear-gradient(90deg, #0e4c92, #0077b5);
    }
    
    .linkedin-button:hover {
        box-shadow: 0 6px 20px rgba(14, 76, 146, 0.5);
    }
    
    /* Skill Tags */
    .skill-tag {
        display: inline-block;
        padding: 8px 15px;
        margin: 5px;
        background: rgba(96, 165, 250, 0.2);
        border: 1px solid rgba(96, 165, 250, 0.5);
        border-radius: 20px;
        color: #60a5fa;
        font-size: 0.9rem;
        font-weight: 500;
    }
    
    /* Text Styles */
    .intro-text {
        color: #e5e7eb;
        font-size: 1.2rem;
        line-height: 1.8;
        margin: 20px 0;
    }
    
    .subheading {
        color: #a78bfa;
        font-size: 1.5rem;
        font-weight: bold;
        margin-top: 20px;
    }
    
    /* Stats Box */
    .stats-box {
        background: linear-gradient(135deg, rgba(96, 165, 250, 0.1), rgba(167, 139, 250, 0.1));
        border: 1px solid rgba(96, 165, 250, 0.3);
        border-radius: 10px;
        padding: 20px;
        text-align: center;
    }
    
    .stats-number {
        color: #60a5fa;
        font-size: 2.5rem;
        font-weight: bold;
    }
    
    .stats-label {
        color: #9ca3af;
        font-size: 1rem;
    }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0f172a 0%, #1e293b 100%);
    }
    
    [data-testid="stSidebar"] .css-1d391kg {
        padding-top: 3rem;
    }
    
    /* Remove default margins */
    .block-container {
        padding-top: 2rem;
    }
    
    /* Links */
    a {
        color: #60a5fa;
        text-decoration: none;
    }
    
    a:hover {
        color: #a78bfa;
    }
    
    /* Lists */
    ul {
        color: #e5e7eb;
        line-height: 1.8;
    }
    
    li {
        margin-bottom: 10px;
    }
    
    /* Image Styling */
    img {
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
    }
</style>
""", unsafe_allow_html=True)

# Sidebar Navigation
with st.sidebar:
    st.markdown("<h1 style='color: #60a5fa; text-align: center;'>🚀 Navigation</h1>", unsafe_allow_html=True)
    st.markdown("---")
    
    nav_options = {
        '🏠 Home': 'Home',
        '📄 Resume': 'Resume',
        '💼 Projects': 'Projects',
        '📞 Contact': 'Contact'
    }
    
    nav_choice = st.radio(
        'Select Page',
        list(nav_options.keys()),
        label_visibility='collapsed'
    )
    
    selected_page = nav_options[nav_choice]
    
    st.markdown("---")
    st.markdown("<h3 style='color: #a78bfa;'>🔗 Connect With Me</h3>", unsafe_allow_html=True)
    st.markdown(f"""
        <a href="{LINKEDIN_URL}" target="_blank" class="custom-button linkedin-button">
            LinkedIn
        </a>
        <br>
        <a href="{GITHUB_URL}" target="_blank" class="custom-button github-button">
            GitHub
        </a>
    """, unsafe_allow_html=True)

# HOME PAGE
if selected_page == 'Home':
    # Hero Section
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.image('Images/me.png', width='stretch')
    
    with col2:
        st.markdown('<h1 class="gradient-text">Muhammad Tayyab</h1>', unsafe_allow_html=True)
        st.markdown('<h2 style="color: #a78bfa; font-size: 2rem;">Data Scientist & Machine Learning Engineer</h2>', unsafe_allow_html=True)
        st.markdown("""
            <p class="intro-text">
                Passionate about transforming data into actionable insights and building intelligent systems 
                that solve real-world problems. Specialized in deep learning, computer vision, and NLP.
            </p>
        """, unsafe_allow_html=True)
        
        # Quick Stats
        stat_col1, stat_col2, stat_col3 = st.columns(3)
        with stat_col1:
            st.markdown("""
                <div class="stats-box">
                    <div class="stats-number">20+</div>
                    <div class="stats-label">Projects</div>
                </div>
            """, unsafe_allow_html=True)
        
        with stat_col2:
            st.markdown("""
                <div class="stats-box">
                    <div class="stats-number">15+</div>
                    <div class="stats-label">Certifications</div>
                </div>
            """, unsafe_allow_html=True)
        
        with stat_col3:
            st.markdown("""
                <div class="stats-box">
                    <div class="stats-number">2+</div>
                    <div class="stats-label">Years Experience</div>
                </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # About Me Section
    st.markdown('<h2 class="section-header">👨‍💻 About Me</h2>', unsafe_allow_html=True)
    
    st.markdown("""
        <div class="glass-card">
            <p class="intro-text">
                I am a highly motivated Data Scientist with a passion for machine learning and artificial intelligence. 
                With a strong foundation in statistical methods and deep learning techniques, I bring a unique blend of 
                technical expertise and problem-solving skills to every project.
            </p>
            <p class="intro-text">
                My journey in data science began during my Bachelor's in Computer Science at Riphah International University, 
                where I discovered my love for extracting meaningful patterns from data. Since then, I've worked on diverse 
                projects ranging from lip-reading systems to stock market prediction, always pushing the boundaries of what's 
                possible with AI.
            </p>
            <p class="intro-text">
                I believe in the power of collaboration and continuous learning. Whether it's staying updated with the latest 
                research papers or contributing to open-source projects, I'm always eager to grow and share knowledge with 
                the community.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Core Competencies
    st.markdown('<h2 class="section-header">🎯 Core Competencies</h2>', unsafe_allow_html=True)
    
    comp_col1, comp_col2 = st.columns(2)
    
    with comp_col1:
        st.markdown("""
            <div class="glass-card">
                <h3 class="subheading">🤖 Machine Learning</h3>
                <p class="intro-text">
                    Expert in supervised and unsupervised learning, feature engineering, and model optimization. 
                    Proficient in scikit-learn, XGBoost, and ensemble methods.
                </p>
            </div>
            
            <div class="glass-card">
                <h3 class="subheading">👁️ Computer Vision</h3>
                <p class="intro-text">
                    Experienced in image classification, object detection, and video analysis using CNNs. 
                    Skilled with OpenCV, TensorFlow, and transfer learning techniques.
                </p>
            </div>
        """, unsafe_allow_html=True)
    
    with comp_col2:
        st.markdown("""
            <div class="glass-card">
                <h3 class="subheading">🧠 Deep Learning</h3>
                <p class="intro-text">
                    Specialized in neural network architectures including CNNs, RNNs, and LSTMs. 
                    Hands-on experience with TensorFlow and Keras for complex model development.
                </p>
            </div>
            
            <div class="glass-card">
                <h3 class="subheading">💬 NLP & LLMs</h3>
                <p class="intro-text">
                    Proficient in text processing, sentiment analysis, and working with large language models. 
                    Experience with transformers, BERT, and GPT-based applications.
                </p>
            </div>
        """, unsafe_allow_html=True)

# RESUME PAGE
elif selected_page == 'Resume':
    st.markdown('<h1 class="gradient-text">📄 Resume</h1>', unsafe_allow_html=True)
    
    # Education
    st.markdown('<h2 class="section-header">🎓 Education</h2>', unsafe_allow_html=True)
    st.markdown("""
        <div class="glass-card">
            <h3 style="color: #a78bfa; font-size: 1.5rem;">Bachelor of Science in Computer Science</h3>
            <p style="color: #9ca3af; font-size: 1.1rem;">Riphah International University | 2018 - 2022</p>
            <p class="intro-text">
                Graduated with a strong foundation in computer science fundamentals, data structures, 
                algorithms, and specialized coursework in machine learning and artificial intelligence.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Work Experience
    st.markdown('<h2 class="section-header">💼 Work Experience</h2>', unsafe_allow_html=True)
    
    st.markdown("""
        <div class="glass-card">
            <h3 style="color: #a78bfa; font-size: 1.5rem;">Implementation Engineer</h3>
            <p style="color: #9ca3af; font-size: 1.1rem;">Center for Advanced Research in Engineering | Dec 2023 - Present </p>
            <ul class="intro-text">
                <li>Expertise in ERP systems, managing databases with SQL, and customizing forms in Joget using JavaScript, HTML, and CSS</li>
                <li>Developed accurate reports with Jasper and crafted dynamic dashboards to highlight key metrics</li>
                <li>Applied strong analytical skills to ensure data accuracy, optimize system functionality, and address challenges in ERP environments</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    
    
    st.markdown("""
        <div class="glass-card">
            <h3 style="color: #a78bfa; font-size: 1.5rem;">Data Science Intern</h3>
            <p style="color: #9ca3af; font-size: 1.1rem;">4media | Sep 2022 - Feb 2023</p>
            <ul class="intro-text">
                <li>Developed machine learning models for business analytics and prediction tasks</li>
                <li>Performed data analysis and visualization to derive actionable insights</li>
                <li>Collaborated with cross-functional teams to implement data-driven solutions</li>
                <li>Automated data pipelines and improved data processing efficiency</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

    
    # Skills
    st.markdown('<h2 class="section-header">🛠️ Technical Skills</h2>', unsafe_allow_html=True)
    
    skills_dict = {
        "Programming Languages": ["Python", "Java", "JavaScript", "SQL"],
        "Data Analysis": ["Pandas", "NumPy", "Statistical Analysis"],
        "Machine Learning": ["Scikit-Learn", "XGBoost", "Feature Engineering"],
        "Deep Learning": ["TensorFlow", "Keras", "PyTorch", "Neural Networks"],
        "Computer Vision": ["OpenCV", "Image Processing", "CNN"],
        "NLP": ["Text Processing", "LSTM", "Transformers", "BERT"],
        "Data Visualization": ["Matplotlib", "Seaborn", "PowerBI"],
        "Databases": ["MySQL", "SQL Server", "PostgreSQL"],
        "Tools & Platforms": ["Git/GitHub", "Jupyter Notebook", "Microsoft Office", "Google Colab"],
        "Web Development": ["Streamlit", "HTML/CSS", "RESTful APIs"]
    }
    
    for skill_category, skills in skills_dict.items():
        st.markdown(f'<h3 class="subheading">{skill_category}</h3>', unsafe_allow_html=True)
        skill_tags = ''.join([f'<span class="skill-tag">{skill}</span>' for skill in skills])
        st.markdown(f'<div class="glass-card">{skill_tags}</div>', unsafe_allow_html=True)
    
    # Certifications
    st.markdown('<h2 class="section-header">🏆 Certifications</h2>', unsafe_allow_html=True)
    
    certifications = [
        {
            "name": "Google Advanced Data Analytics",
            "issuer": "Coursera",
            "url": "https://coursera.org/verify/professional-cert/3VGYLML6U8ZC/"
        },
        {
            "name": "SQL for Data Science",
            "issuer": "Coursera",
            "url": "https://coursera.org/verify/KB4FA685KYNJ/"
        },
        {
            "name": "Machine Learning in Python",
            "issuer": "365 Data Science",
            "url": "https://learn.365datascience.com/certificates/CC-F2AC711D5E/"
        },
        {
            "name": "Applied Data Science with Python",
            "issuer": "Simplilearn",
            "url": "https://www.simplilearn.com/skillup-certificate-landing?token=eyJjb3Vyc2VfaWQiOiI2ODQiLCJjZXJ0aWZpY2F0ZV91cmwiOiJodHRwczpcL1wvY2VydGlmaWNhdGVzLnNpbXBsaWNkbi5uZXRcL3NoYXJlXC90aHVtYl8zODQ4NjI4XzE2NjU1ODk4NTMucG5nIiwidXNlcm5hbWUiOiJNdWhhbW1hZCBUYXl5YWIifQ%3D%3D&utm_source=shared-certificate&utm_medium=lms&utm_campaign=shared-certificate-promotion"
        },
        {
            "name": "Scientific Computing with Python",
            "issuer": "freeCodeCamp",
            "url": "https://www.freecodecamp.org/certification/Tayyab885/scientific-computing-with-python-v7"
        },
        {
            "name": "Statistics",
            "issuer": "365 Data Science",
            "url": "https://learn.365datascience.com/certificates/CC-EC4896E8AD/"
        },
        {
            "name": "Python (Basic)",
            "issuer": "HackerRank",
            "url": "https://www.hackerrank.com/certificates/9ce1e3043a5a"
        },
        {
            "name": "SQL (Basic)",
            "issuer": "HackerRank",
            "url": "https://www.hackerrank.com/certificates/a2a976e2c4bc"
        }
    ]
    
    cert_col1, cert_col2 = st.columns(2)
    
    for idx, cert in enumerate(certifications):
        with cert_col1 if idx % 2 == 0 else cert_col2:
            st.markdown(f"""
                <div class="glass-card">
                    <h4 style="color: #a78bfa; margin-bottom: 10px;">{cert['name']}</h4>
                    <p style="color: #9ca3af; margin-bottom: 15px;">{cert['issuer']}</p>
                    <a href="{cert['url']}" target="_blank" class="custom-button">
                        View Certificate
                    </a>
                </div>
            """, unsafe_allow_html=True)

# PROJECTS PAGE
elif selected_page == 'Projects':
    st.markdown('<h1 class="gradient-text">💼 Projects</h1>', unsafe_allow_html=True)
    st.markdown('<p class="intro-text">Explore my portfolio of data science and machine learning projects</p>', unsafe_allow_html=True)
    
    projects = [
        {
            "title": "🎬 Lip Reading Using Deep Learning",
            "image": "Images/lipread.png",
            "description": """
                Developed an advanced lip-reading system using deep learning for accurate speech recognition from video.
            """,
            "highlights": [
                "Built TensorFlow model with Conv3D and Bidirectional LSTM",
                "Implemented efficient data pipeline with TensorFlow's Dataset API",
                "Optimized performance using CTC loss and learning rate scheduling",
                "Created Streamlit app for real-time predictions"
            ],
            "tech": ["TensorFlow", "LSTM", "Conv3D", "Streamlit", "Computer Vision"],
            "github": "https://github.com/Tayyab885/Lip-Reading-Project-Using-Deep-Learning",
            "demo": None
        },
        {
            "title": "🤖 AutoGPT YouTube Title and Script Generator",
            "image": "Images/youtube.jpg",
            "description": """
                AI-powered content creation tool leveraging OpenAI's GPT to generate engaging YouTube titles and scripts.
            """,
            "highlights": [
                "Integrated OpenAI's GPT model for creative content generation",
                "Implemented Wikipedia research for enhanced script quality",
                "Built intuitive Streamlit interface with history tracking",
                "Streamlined content creation workflow for creators"
            ],
            "tech": ["OpenAI GPT", "LangChain", "Python", "Streamlit", "NLP"],
            "github": "https://github.com/Tayyab885/AutoGPT-YouTube-Title-and-Script-Generator",
            "demo": None
        },
        {
            "title": "📈 Stock Market Prediction Using LSTM",
            "image": "Images/stock_market.jpg",
            "description": """
                Advanced time series forecasting system for stock price prediction using LSTM neural networks.
            """,
            "highlights": [
                "Implemented LSTM model for sequential data analysis",
                "Achieved accurate price predictions with comprehensive data preprocessing",
                "Generated 30-day future forecasts with confidence intervals",
                "Optimized model architecture for financial time series"
            ],
            "tech": ["LSTM", "TensorFlow", "Keras", "Time Series", "Financial Analysis"],
            "github": "https://github.com/Tayyab885/Stock-Price-Prediction-And-Forecasting-Using-LSTM",
            "demo": None
        },
        {
            "title": "🌿 Cotton Disease Prediction",
            "image": "Images/cotton_disease.jpg",
            "description": """
                Deep learning-based disease classification system for cotton plants using image recognition.
            """,
            "highlights": [
                "Achieved 87% accuracy in disease classification",
                "Developed CNN architecture with optimized layers",
                "Processed and augmented agricultural image datasets",
                "Deployed model for real-world agricultural applications"
            ],
            "tech": ["CNN", "Image Classification", "TensorFlow", "Computer Vision"],
            "github": "https://github.com/Tayyab885/Cotton-Disease-Prediction",
            "demo": None
        },
        {
            "title": "🏥 Chronic Kidney Disease Prediction",
            "image": "Images/chronic.webp",
            "description": """
                Complete AutoML web application for predicting chronic kidney disease with data analysis capabilities.
            """,
            "highlights": [
                "Implemented 3 classification algorithms with 98% accuracy",
                "Built automated data cleaning and EDA pipeline",
                "Created interactive visualizations and analysis reports",
                "Deployed on Streamlit Cloud for public access"
            ],
            "tech": ["AutoML", "Scikit-learn", "Pandas", "Streamlit", "Healthcare AI"],
            "github": "https://github.com/Tayyab885/Chronic_Kidney_DIsease_Prediction",
            "demo": "https://tayyab885-chronic-kidney-disease-prediction-app-s4cofm.streamlit.app/"
        },
        {
            "title": "📚 Book Recommendation System",
            "image": "Images/book.webp",
            "description": """
                Collaborative filtering-based recommendation engine for personalized book suggestions.
            """,
            "highlights": [
                "Implemented instance-based collaborative filtering",
                "Built searchable database with book details",
                "Generated personalized recommendations using similarity scores",
                "Deployed interactive web app with user-friendly interface"
            ],
            "tech": ["Collaborative Filtering", "Machine Learning", "Streamlit", "Python"],
            "github": "https://github.com/Tayyab885/BookRecommendationSystem",
            "demo": "https://tayyab885-bookrecommendationsystem-recommendation-zecywg.streamlitapp.com/"
        },
        {
            "title": "🛒 Superstore Sales Analysis",
            "image": "Images/superstore.jpg",
            "description": """
                Comprehensive sales analytics project combining data preprocessing, SQL analysis, and insights generation.
            """,
            "highlights": [
                "Performed extensive data cleaning with Pandas",
                "Conducted SQL analysis for business insights",
                "Identified key trends in customer behavior and sales performance",
                "Generated actionable recommendations for business optimization"
            ],
            "tech": ["SQL", "Pandas", "Data Analysis", "Business Intelligence", "Streamlit"],
            "github": "https://github.com/Tayyab885/Superstore-Sales-Analysis",
            "demo": None
        },
        {
            "title": "🦠 COVID-19 Data Analysis",
            "image": "Images/covid.jpg",
            "description": """
                In-depth analysis of COVID-19 data using SQL for infection rates, death rates, and vaccination statistics.
            """,
            "highlights": [
                "Calculated country-wise infection and death percentages",
                "Analyzed vaccination rates across different regions",
                "Identified trends and patterns in pandemic spread",
                "Generated insights for data-driven decision making"
            ],
            "tech": ["SQL", "Data Analysis", "Statistics", "Public Health Data"],
            "github": "https://github.com/Tayyab885/Covid-19-Data-Analysis-Using-SQL",
            "demo": None
        },
        {
            "title": "🧹 Data Cleaning Using SQL",
            "image": "Images/datacleaning.webp",
            "description": """
                Comprehensive data cleaning project on Nashville Housing Data using advanced SQL techniques.
            """,
            "highlights": [
                "Standardized and cleaned large housing dataset",
                "Implemented string manipulation for address parsing",
                "Handled missing values and data inconsistencies",
                "Transformed data for improved analysis quality"
            ],
            "tech": ["SQL", "Data Cleaning", "Data Transformation", "ETL"],
            "github": "https://github.com/Tayyab885/Nashville-Housing-Data-Cleaning-Using-SQL",
            "demo": None
        }
    ]
    
    # Display projects
    for idx, project in enumerate(projects):
        st.markdown('<div class="project-card">', unsafe_allow_html=True)
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.image(project['image'], width='stretch')
        
        with col2:
            st.markdown(f'<h3 class="project-title">{project["title"]}</h3>', unsafe_allow_html=True)
            st.markdown(f'<p class="project-desc">{project["description"]}</p>', unsafe_allow_html=True)
            
            st.markdown('<p class="project-desc"><strong>Key Highlights:</strong></p>', unsafe_allow_html=True)
            for highlight in project['highlights']:
                st.markdown(f'<p class="project-desc">• {highlight}</p>', unsafe_allow_html=True)
            
            # Tech stack
            tech_tags = ''.join([f'<span class="skill-tag">{tech}</span>' for tech in project['tech']])
            st.markdown(f'<div style="margin: 15px 0;">{tech_tags}</div>', unsafe_allow_html=True)
            
            # Buttons
            button_html = f'<a href="{project["github"]}" target="_blank" class="custom-button github-button">View on GitHub</a>'
            if project.get('demo'):
                button_html += f' <a href="{project["demo"]}" target="_blank" class="custom-button">Live Demo</a>'
            st.markdown(button_html, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('<hr style="border: 1px solid rgba(96, 165, 250, 0.2); margin: 30px 0;">', unsafe_allow_html=True)
    
    # Call to action
    st.markdown(f"""
        <div class="glass-card" style="text-align: center; padding: 40px;">
            <h2 style="color: #60a5fa; margin-bottom: 20px;">Want to see more?</h2>
            <p class="intro-text">Check out my GitHub for more projects and contributions!</p>
            <a href="{GITHUB_URL}" target="_blank" class="custom-button github-button" style="font-size: 1.2rem; padding: 15px 40px;">
                Visit My GitHub
            </a>
        </div>
    """, unsafe_allow_html=True)

# CONTACT PAGE
elif selected_page == 'Contact':
    st.markdown('<h1 class="gradient-text">📞 Get In Touch</h1>', unsafe_allow_html=True)
    
    st.markdown("""
        <div class="glass-card">
            <p class="intro-text">
                I'm always open to discussing new projects, creative ideas, or opportunities to be part of your vision. 
                Whether you want to collaborate on a data science project or just want to say hi, feel free to reach out!</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Contact Methods
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
            <div class="glass-card" style="text-align: center;">
                <h2 style="color: #60a5fa; font-size: 3rem;">💼</h2>
                <h3 class="subheading">Professional Network</h3>
                <p class="intro-text">Connect with me on LinkedIn for professional networking and opportunities.</p>
                <a href="{}" target="_blank" class="custom-button linkedin-button">
                    Connect on LinkedIn
                </a>
            </div>
        """.format(LINKEDIN_URL), unsafe_allow_html=True)
        
        st.markdown("""
            <div class="glass-card" style="text-align: center;">
                <h2 style="color: #60a5fa; font-size: 3rem;">💻</h2>
                <h3 class="subheading">Open Source</h3>
                <p class="intro-text">Check out my code, contribute to projects, or star repositories you find interesting.</p>
                <a href="{}" target="_blank" class="custom-button github-button">
                    Visit GitHub Profile
                </a>
            </div>
        """.format(GITHUB_URL), unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class="glass-card" style="text-align: center;">
                <h2 style="color: #60a5fa; font-size: 3rem;">📧</h2>
                <h3 class="subheading">Email Me</h3>
                <p class="intro-text">For project inquiries, collaborations, or just to say hello.</p>
                <a href="mailto:{}" class="custom-button">
                    Send an Email
                </a>
            </div>
        """.format(EMAIL), unsafe_allow_html=True)
        
        st.markdown("""
            <div class="glass-card" style="text-align: center;">
                <h2 style="color: #60a5fa; font-size: 3rem;">📱</h2>
                <h3 class="subheading">Social Media</h3>
                <p class="intro-text">Follow me on social platforms to stay updated with my latest work and insights.</p>
                <div style="margin-top: 20px;">
                    <a href="{}" target="_blank" class="custom-button linkedin-button">LinkedIn</a>
                    <a href="{}" target="_blank" class="custom-button github-button">GitHub</a>
                </div>
            </div>
        """.format(LINKEDIN_URL, GITHUB_URL), unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Contact Form Section
    st.markdown('<h2 class="section-header">📝 Send Me a Message</h2>', unsafe_allow_html=True)
    
    st.markdown("""
        <div class="glass-card">
            <p class="intro-text">
                Fill out the form below and I'll get back to you as soon as possible!
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    with st.form("contact_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            name = st.text_input("Your Name *", placeholder="John Doe")
            email = st.text_input("Your Email *", placeholder="john@example.com")
        
        with col2:
            subject = st.text_input("Subject *", placeholder="Project Collaboration")
            phone = st.text_input("Phone Number (Optional)", placeholder="+92 300 1234567")
        
        message = st.text_area(
            "Your Message *",
            placeholder="Tell me about your project or inquiry...",
            height=200
        )
        
        # Form submission
        submitted = st.form_submit_button("Send Message", type="primary")
        
        if submitted:
            if name and email and subject and message:
                st.success("✅ Thank you for your message! I'll get back to you soon.")
                st.balloons()
            else:
                st.error("❌ Please fill in all required fields (marked with *).")
    
    st.markdown("---")
    
    # Collaboration Interests
    st.markdown('<h2 class="section-header">🤝 What I\'m Looking For</h2>', unsafe_allow_html=True)
    
    interests_col1, interests_col2, interests_col3 = st.columns(3)
    
    with interests_col1:
        st.markdown("""
            <div class="glass-card" style="text-align: center; min-height: 250px;">
                <h2 style="color: #60a5fa; font-size: 2.5rem;">🚀</h2>
                <h3 class="subheading">Exciting Projects</h3>
                <p class="intro-text">
                    ML/AI projects that push boundaries and solve real-world problems
                </p>
            </div>
        """, unsafe_allow_html=True)
    
    with interests_col2:
        st.markdown("""
            <div class="glass-card" style="text-align: center; min-height: 250px;">
                <h2 style="color: #a78bfa; font-size: 2.5rem;">💼</h2>
                <h3 class="subheading">Career Opportunities</h3>
                <p class="intro-text">
                    Full-time roles, freelance work, or consulting in data science and ML
                </p>
            </div>
        """, unsafe_allow_html=True)
    
    with interests_col3:
        st.markdown("""
            <div class="glass-card" style="text-align: center; min-height: 250px;">
                <h2 style="color: #f472b6; font-size: 2.5rem;">🎓</h2>
                <h3 class="subheading">Learning & Growth</h3>
                <p class="intro-text">
                    Open source contributions, mentorship, and knowledge sharing
                </p>
            </div>
        """, unsafe_allow_html=True)
    
    # Footer
    st.markdown("---")
    st.markdown("""
        <div style="text-align: center; padding: 30px;">
            <p style="color: #9ca3af; font-size: 1.1rem;">
                Made with ❤️ by Muhammad Tayyab | © 2025 All Rights Reserved
            </p>
            <p style="color: #60a5fa; font-size: 0.9rem; margin-top: 10px;">
                "Turning data into insights, one project at a time"
            </p>
        </div>
    """, unsafe_allow_html=True)
