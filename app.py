import streamlit as st

LINKEDIN_URL = 'https://www.linkedin.com/in/muhammad-tayyab-9b965b1b1/'
GITHUB_URL = 'https://github.com/Tayyab885'

# Set page config and page title
st.set_page_config(page_title='My Portfolio', page_icon=':rocket:', layout='wide')

# Set page background color and text color
st.markdown(
    """
    <style>
    .header {
        padding: 30px;
        margin-bottom: 30px;
    }
    .header img {
        border-radius: 50%;
        width: 200px;
        height: 200px;
        object-fit: cover;
    }
    .header h1 {
        font-size: 48px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .header p {
        font-size: 24px;
        line-height: 1.5;
    }
    .about p {
        font-size: 18px;
        line-height: 1.5;
    }
    .project {
        display: flex;
        flex-direction: row;
        align-items: center;
        margin-bottom: 30px;
    }
    .project img {
        margin-right: 30px;
        border-radius: 5px;
        object-fit: cover;
    }
    .project h2 {
        font-size: 24px;
        margin-bottom: 10px;
    }
    .project p {
        font-size: 16px;
        line-height: 1.5;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# Add header image and text


# Create navigation menu
nav_options = ('Home', 'Resume', 'Projects')
nav_choice = st.sidebar.radio('Navigation', nav_options, index=0)

# Create content for each page
if nav_choice == 'Home':
    header_container = st.container()
    with header_container:
        col1, col2 = st.columns([2, 3])
        with col1:
            st.image('Images/me.png', caption='', use_column_width=True)
        with col2:
            st.markdown('<div class="header"><h1>Welcome to My Portfolio</h1><h3>A Bit About Me:</h3><p>I am a highly motivated individual with a passion for data science and machine learning. I have a strong foundation in statistical and machine learning methods, as well as proficiency in Python and experience with data wrangling and deep learning techniques. I am eager to continue learning and expanding my skills in the field.</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="about"><h2>About Me</h2><p>My name is Muhammad Tayyab and I am a highly motivated individual with a strong passion for data science and machine learning. With a solid foundation in statistical and machine learning methods, I possess proficiency in Python and experience in data wrangling and deep learning techniques. I constantly strive to expand my knowledge and skills in the field, and am always eager to take on new challenges. I am excited to contribute my expertise to any project or team, and to continue growing as a data scientist and machine learning enthusiast. <br>In addition to my technical skills, I also have strong communication and teamwork abilities. I believe that effective collaboration and communication are essential in any successful data science project. I enjoy working with others to identify and solve complex problems, and I am always open to feedback and new ideas. I am committed to using my skills and experience to make a meaningful impact and drive positive change in any organization I work with.</p><p style="font-size: 20px; font-weight: bold;">You can find me on <a href="{LINKEDIN_URL}">LinkedIn</a> and <a href="{GITHUB_URL}">Github</a>.</p></div>'.format(LINKEDIN_URL=LINKEDIN_URL, GITHUB_URL=GITHUB_URL), unsafe_allow_html=True)


# Create Resume page
if nav_choice == 'Resume':
    st.markdown('<h1>My Resume</h1>', unsafe_allow_html=True)
    st.markdown('<h2>Education</h2>', unsafe_allow_html=True)
    st.markdown('<ul><li>B.S. in Computer Science, Riphah International University, 2018 - 2022</li></ul>', unsafe_allow_html=True)
    st.markdown('<h2>Work Experience</h2>', unsafe_allow_html=True)
    st.markdown('<ul><li>Data Science Intern, Craftive Apparels, Aug 2022 - Feb 2023</li></ul>', unsafe_allow_html=True)
    ## Skills
    st.markdown('<h2>Skills</h2>', unsafe_allow_html=True)
    st.markdown('<ul><li>Proficient in Python programming language and experienced in working with SQL.</li><li>Skilled in data preparation, cleaning, and feature engineering, as well as performing exploratory data analysis and visualization using Matplotlib and Seaborn.</li><li>Knowledgeable in linear algebra, statistics, predictive modeling, and machine learning algorithms, including deep learning with TensorFlow and Keras.</li><li>Familiarity with computer vision using OpenCV and building web apps using Streamlit.</li><li>Competent in web scraping using Beautiful Soup.</li></ul>', unsafe_allow_html=True)
    st.markdown('<h2>Tools & Technologies</h2>', unsafe_allow_html=True)
    st.markdown('<ul><li>Programming Languages: Python, Java</li></ul>', unsafe_allow_html=True)
    st.markdown('<ul><li>Databases: MySQL, SQL Server</li></ul>', unsafe_allow_html=True)
    st.markdown('<ul><li>Data Wrangling and Manipulation: Pandas, NumPy</li></ul>', unsafe_allow_html=True)
    st.markdown('<ul><li>Data Visualization: Matplotlib, Seaborn, PowerBi</li></ul>', unsafe_allow_html=True)
    st.markdown('<ul><li>Machine Learning: Scikit-Learn</li></ul>', unsafe_allow_html=True)
    st.markdown('<ul><li>Deep Learning: TensorFlow and Keras</li></ul>', unsafe_allow_html=True)
    st.markdown('<ul><li>Web Scraping: Beautiful Soup</li></ul>', unsafe_allow_html=True)
    st.markdown('<ul><li>Computer Vision: OpenCV</li></ul>', unsafe_allow_html=True)
    st.markdown('<ul><li>Others: Microsoft Office, Streamlit, Git and GitHub, Jupyter Notebook, Anaconda, Google Colab</li></ul>', unsafe_allow_html=True)
    ## Certifications
    st.markdown('<h2>Certifications</h2>', unsafe_allow_html=True)
    st.markdown('<ul><li><a href="https://learn.365datascience.com/c/eb5a7bcc9d/">Introduction to Data and Data Science</a> - 365 Data Science</li></ul>', unsafe_allow_html=True)
    st.markdown('<ul><li><a href="https://learn.365datascience.com/certificates/CC-EC4896E8AD/">Statistics</a> - 365 Data Science</li></ul>', unsafe_allow_html=True)
    st.markdown('<ul><li><a href="https://learn.365datascience.com/c/05d779eba3/">Mathematics</a> - 365 Data Science</li></ul>', unsafe_allow_html=True)
    st.markdown('<ul><li><a href="https://learn.365datascience.com/c/b1879ab550/">Data Cleaning and Preprocessing with Pandas</a> - 365 Data Science</li></ul>', unsafe_allow_html=True)
    st.markdown('<ul><li><a href="https://learn.365datascience.com/certificates/CC-F2AC711D5E/">Machine Learning in Python</a> - 365 Data Science</li></ul>', unsafe_allow_html=True)
    st.markdown('<ul><li><a href="https://www.hackerrank.com/certificates/9ce1e3043a5a">Python (Basic)</a> - HackerRank</li></ul>', unsafe_allow_html=True)
    st.markdown('<ul><li><a href="https://www.hackerrank.com/certificates/97bdd0473225">Problem Solving (Basic)</a> - HackerRank</li></ul>', unsafe_allow_html=True)
    st.markdown('<ul><li><a href="https://www.hackerrank.com/certificates/a2a976e2c4bc">SQL (Basic)</a> - HackerRank</li></ul>', unsafe_allow_html=True)
    st.markdown('<ul><li><a href="https://www.simplilearn.com/skillup-certificate-landing?token=eyJjb3Vyc2VfaWQiOiI2ODQiLCJjZXJ0aWZpY2F0ZV91cmwiOiJodHRwczpcL1wvY2VydGlmaWNhdGVzLnNpbXBsaWNkbi5uZXRcL3NoYXJlXC90aHVtYl8zODQ4NjI4XzE2NjU1ODk4NTMucG5nIiwidXNlcm5hbWUiOiJNdWhhbW1hZCBUYXl5YWIifQ%3D%3D&utm_source=shared-certificate&utm_medium=lms&utm_campaign=shared-certificate-promotion&referrer=https%3A%2F%2Flms.simplilearn.com%2Fcourses%2F2772%2FData%2520Science%2520with%2520Python%2Fcertificate%2Fdownload-skillup&%24web_only=true&_branch_match_id=1108517453658877229&_branch_referrer=H4sIAAAAAAAAA8soKSkottLXL87MLcjJ1EssKNDLyczL1k%2FVT0kJzcoOrswxKUkCAGUzxPclAAAA">Applied Data Science with Python</a> - Simplilearn</li></ul>', unsafe_allow_html=True)
    st.markdown('<ul><li><a href="https://www.freecodecamp.org/certification/Tayyab885/scientific-computing-with-python-v7">Scientific Computing with Python</a> - freeCodeCamp</li></ul>', unsafe_allow_html=True)


    
if nav_choice == 'Projects':
    st.markdown('<h1>Projects</h2>', unsafe_allow_html=True)
    
    # Project 1
    with st.container():
        col1, col2 = st.columns([2, 3])
        col1.image('Images/lipread.png', caption='', use_column_width=True)
        col2.markdown('<h2>Lip Reading Using Deep Learning:</h2><ul><li>Developed a TensorFlow-based lip-reading model with Conv3D and Bidirectional LSTM for accurate interpretation of lip movements and speech recognition from videos.</li><li>Implemented an efficient data pipeline using TensorFlow\'s Dataset API for seamless training and evaluation of the lip-reading model.</li><li>Optimized model performance through TensorFlow\'s CTC loss function and learning rate scheduler, ensuring effective convergence and minimized training loss.</li><li>Created a user-friendly Streamlit app for real-time lip-reading predictions, enhancing model accessibility and usability.</li><li><a href="https://github.com/Tayyab885/Lip-Reading-Project-Using-Deep-Learning">GitHub link</a></li></ul>', unsafe_allow_html=True)

    st.markdown('<hr>', unsafe_allow_html=True)
    
    # Project 2
    with st.container():
        col1, col2 = st.columns([2, 3])
        col1.image('Images/youtube.jpg', caption='', use_column_width=True)
        col2.markdown('<h2>AutoGPT YouTube Title and Script Generator:</h2><ul><li>Built a YouTube Title and Script Generator app using Python and OpenAI\'s GPT language model to assist content creators in generating engaging video content.</li><li>Utilized the langchain library to interact with the GPT model, enabling the app to quickly generate video titles and scripts based on prompts.</li><li>Implemented a Wikipedia research input to help generate script content, enhancing the app\'s ability to produce high-quality scripts.</li><li>Developed an intuitive Streamlit app interface that displays the generated title and script, as well as the title history, script history, and Wikipedia research history.</li><li>Demonstrated the value of AI in streamlining content creation processes, highlighting the potential for future AI-powered tools to enhance creative output.</li><li><a href="https://github.com/Tayyab885/AutoGPT-YouTube-Title-and-Script-Generator">GitHub link</a></li></ul>', unsafe_allow_html=True)

    st.markdown('<hr>', unsafe_allow_html=True)

    # Project 3
    with st.container():
        col1, col2 = st.columns([2, 3])
        col1.image('Images/chronic.webp', caption='', use_column_width=True)
        col2.markdown('<h2>Chronic Kidney Disease Prediction:</h2><ul><li>An AutoML webapp capable of predicting chronic kidney disease as well as cleaning the data, generating an analysis report, and visualizing the data using different kinds of graphs.</li><li>Implemented three different classification algorithms and achieved an accuracy score of 98%.</li><li>Built using Streamlit and deployed on the Streamlit cloud.</li><li><a href="https://tayyab885-chronic-kidney-disease-prediction-app-s4cofm.streamlit.app/">Web app link</a></li><li><a href="https://github.com/Tayyab885/Chronic_Kidney_DIsease_Prediction">GitHub Link</a> </li></ul>', unsafe_allow_html=True)

    st.markdown('<hr>', unsafe_allow_html=True)

    # Project 4
    with st.container():
        col1, col2 = st.columns([2, 3])
        col1.image('Images/book.webp', caption='', use_column_width=True)
        col2.markdown('<h2>Book Recommendation System:</h2><ul><li>An instance-based or Collaborative Filtering based machine learning project built in Python.</li><li>Users can search through various books and look through their details.</li><li>Provides a list of top-rated books.</li><li>Recommends books based on similarity score.</li><li>Built using Streamlit and deployed on the Streamlit cloud.</li><li><a href="https://tayyab885-bookrecommendationsystem-recommendation-zecywg.streamlitapp.com/">Web app link</a></li><li><a href="https://github.com/Tayyab885/BookRecommendationSystem">GitHub link</a></li></ul>', unsafe_allow_html=True)

    st.markdown('<hr>', unsafe_allow_html=True)
    
    # Project 5
    with st.container():
        col1, col2 = st.columns([2, 3])
        col1.image('Images/superstore.jpg', caption='', use_column_width=True)
        col2.markdown('<h2>Superstore Sales Analysis:</h2><ul><li>Performed data pre-processing using Python and Pandas to clean and refine the Superstore Sales dataset, removing duplicates, handling null values, and removing irrelevant data.</li><li>Conducted SQL analysis on the cleaned dataset to identify trends and insights in customer behavior, sales performance, and operational aspects of the superstore.</li><li>Generated queries to identify the top three customers with the highest total value of orders, calculate the percentage of total orders that were shipped on the same date, and determine the most demanded sub-category in the west region.</li><li>Analyzed the sales data to determine which customer segment was more likely to choose first-class shipping, which city was least contributing to total revenue, and what the average time for orders to get shipped after an order was placed.</li><li>Built using Streamlit and deployed on the Streamlit cloud.</li><li><a href="https://github.com/Tayyab885/Superstore-Sales-Analysis">GitHub link</a></li></ul>', unsafe_allow_html=True)


    st.markdown('<hr>', unsafe_allow_html=True)
    
    # Project 6
    with st.container():
        col1, col2 = st.columns([2, 3])
        col1.image('Images/covid.jpg', caption='', use_column_width=True)
        col2.markdown('<h2>Covid-19 Data Analysis:</h2><ul><li>Analyzed Covid-19 data using SQL to calculate death rates, infection percentages, and vaccination rates.</li><li>Conducted data analysis to inform decision-making and understand Covid-19 trends.</li><li>Identified countries and continents with the highest Covid-19 infection and death rates per population.</li><li>Calculated the percentage of the population in Pakistan that has been infected with Covid-19.</li><li>Analyzed Covid-19 vaccination data in Pakistan, including calculating the percentage of the population that has been vaccinated so far.</li><li><a href="https://github.com/Tayyab885/Covid-19-Data-Analysis-Using-SQL">GitHub link</a></li></ul>', unsafe_allow_html=True)

    st.markdown('<hr>', unsafe_allow_html=True)
    
    # Project 7
    with st.container():
        col1, col2 = st.columns([2, 3])
        col1.image('Images/datacleaning.webp', caption='', use_column_width=True)
        col2.markdown('<h2>Data Cleaning Using SQL:</h2><ul><li>Cleaned and standardized Nashville Housing Data using SQL queries, ensuring data integrity and consistency.</li><li>Employed string manipulation functions and data transformation techniques to populate missing property addresses and split address fields into separate columns.</li><li>Enhanced data quality by converting and standardizing date formats, facilitating accurate analysis and reporting.</li><li>Implemented data cleaning strategies to handle missing values and update null entries, resulting in a more comprehensive and reliable dataset.</li><li><a href="https://github.com/Tayyab885/Nashville-Housing-Data-Cleaning-Using-SQL">GitHub link</a></li></ul>', unsafe_allow_html=True)

    st.markdown('<hr>', unsafe_allow_html=True)
    
    # Display closing statement
    st.markdown('<p style="font-size: 24px; font-weight: bold;">For more projects, please visit my <a href="https://github.com/Tayyab885">GitHub</a>.</p>', unsafe_allow_html=True)

        
st.markdown('</div>', unsafe_allow_html=True)
        
