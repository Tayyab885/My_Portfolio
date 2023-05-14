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
nav_choice = st.sidebar.radio('Navigation', nav_options)

# Create content for each page
if nav_choice == 'Home':
    header_container = st.container()
    with header_container:
        col1, col2 = st.columns([2, 3])
        with col1:
            st.image('Images/me.png', caption='', use_column_width=True)
        with col2:
            st.markdown('<div class="header"><h1>Welcome to My Portfolio</h1><h3>A Bit About Me:</h3><p>I am a highly motivated individual with a passion for data science and machine learning. I have a strong foundation in statistical and machine learning methods, as well as proficiency in Python and experience with data wrangling and deep learning techniques. I am eager to continue learning and expanding my skills in the field.</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="about"><h2>About Me</h2><p>My name is Muhammad Tayyab and I am a highly motivated individual with a strong passion for data science and machine learning. With a solid foundation in statistical and machine learning methods, I possess proficiency in Python and experience in data wrangling and deep learning techniques. I constantly strive to expand my knowledge and skills in the field, and am always eager to take on new challenges. I am excited to contribute my expertise to any project or team, and to continue growing as a data scientist and machine learning enthusiast. <br>In addition to my technical skills, I also have strong communication and teamwork abilities. I believe that effective collaboration and communication are essential in any successful data science project. I enjoy working with others to identify and solve complex problems, and I am always open to feedback and new ideas. I am committed to using my skills and experience to make a meaningful impact and drive positive change in any organization I work with.</p><p>You can find me on <a href="{LINKEDIN_URL}">LinkedIn</a> and <a href="{GITHUB_URL}">Github</a>.</p></div>'.format(LINKEDIN_URL=LINKEDIN_URL, GITHUB_URL=GITHUB_URL), unsafe_allow_html=True)


# Create Resume page
if nav_choice == 'Resume':
    st.write('<h1>My Resume</h1>', unsafe_allow_html=True)
    st.write('<h2>Education</h2>', unsafe_allow_html=True)
    st.write('<ul><li>B.S. in Computer Science, Riphah International University, 2018 - 2022</li></ul>', unsafe_allow_html=True)
    st.write('<h2>Work Experience</h2>', unsafe_allow_html=True)
    st.write('<ul><li>Data Science Intern, Craftive Apparels , Aug 2022 - Feb 2023</li></ul>', unsafe_allow_html=True)
    st.write('<h2>Skills</h2>', unsafe_allow_html=True)
    st.write('<ul><li>Proficient in Python programming language and experienced in working with SQL.</li><li>Skilled in data preparation, cleaning, and feature engineering, as well as performing exploratory data analysis and visualization using Matplotlib and Seaborn</li><li>Knowledgeable in linear algebra, statistics, predictive modeling, and machine learning algorithms, including deep learning with TensorFlow and Keras.</li><li>Familiarity with computer vision using OpenCV and building web apps using Streamlit.</li><li>Competent in web scraping using Beautiful Soup.</li></ul>', unsafe_allow_html=True)
    st.write('<h2>Tools & Technologies</h2>', unsafe_allow_html=True)
    st.write('<ul><li>Programming Languages:<ol>Python, Java</ol></li><li>Databases:<ol>MySQL, SQL Server</ol></li><li>Data Wrangling and Manipulation:<ol>Pandas, NumPy</ol></li><li>Data Visualization:<ol>Matplotlib, Seaborn, PowerBi</ol></li><li>Machine Learning:<ol>Scikit-Learn</ol></li><li>Deep Learning:<ol>Tensorflow and Keras</ol></li><li>Web Scraping:<ol>Beautiful Soup</ol></li><li>Computer Vision:<ol>OpenCV</ol></li><li>Others:<ol>Microsoft Office, Streamlit, Git and GitHub, Jupyter Notebook, Anaconda, Google Colab</ol></li></ul>', unsafe_allow_html=True)
    
if nav_choice == 'Projects':
    st.markdown('<h1>Projects</h2>', unsafe_allow_html=True)
    
    # Project 1
    with st.container():
        col1, col2 = st.columns([2, 3])
        col1.image('Images/youtube.jpg', caption='', use_column_width=True)
        col2.markdown('<h2>AutoGPT YouTube Title and Script Generator:</h2><ul><li>Built a YouTube Title and Script Generator app using Python and OpenAI\'s GPT language model to assist content creators in generating engaging video content.</li><li>Utilized the langchain library to interact with the GPT model, enabling the app to quickly generate video titles and scripts based on prompts.</li><li>Implemented a Wikipedia research input to help generate script content, enhancing the app\'s ability to produce high-quality scripts.</li><li>Developed an intuitive Streamlit app interface that displays the generated title and script, as well as the title history, script history, and Wikipedia research history.</li><li>Demonstrated the value of AI in streamlining content creation processes, highlighting the potential for future AI-powered tools to enhance creative output.</li><li><a href="https://github.com/Tayyab885/AutoGPT-YouTube-Title-and-Script-Generator">GitHub link</a></li></ul>', unsafe_allow_html=True)

    st.markdown('<hr>', unsafe_allow_html=True)

    # Project 2
    with st.container():
        col1, col2 = st.columns([2, 3])
        col1.image('Images/chronic.webp', caption='', use_column_width=True)
        col2.markdown('<h2>Chronic Kidney Disease Prediction:</h2><ul><li>An AutoML webapp capable of predicting chronic kidney disease as well as cleaning the data, generating an analysis report, and visualizing the data using different kinds of graphs.</li><li>Implemented three different classification algorithms and achieved an accuracy score of 98%.</li><li>Built using Streamlit and deployed on the Streamlit cloud.</li><li><a href="https://tayyab885-chronic-kidney-disease-prediction-app-s4cofm.streamlit.app/">Web app link</a></li><li><a href="https://github.com/Tayyab885/Chronic_Kidney_DIsease_Prediction">GitHub Link</a> </li></ul>', unsafe_allow_html=True)

    st.markdown('<hr>', unsafe_allow_html=True)

    # Project 3
    with st.container():
        col1, col2 = st.columns([2, 3])
        col1.image('Images/book.webp', caption='', use_column_width=True)
        col2.markdown('<h2>Book Recommendation System:</h2><ul><li>An instance-based or Collaborative Filtering based machine learning project built in Python.</li><li>Users can search through various books and look through their details.</li><li>Provides a list of top-rated books.</li><li>Recommends books based on similarity score.</li><li>Built using Streamlit and deployed on the Streamlit cloud.</li><li><a href="https://tayyab885-bookrecommendationsystem-recommendation-zecywg.streamlitapp.com/">Web app link</a></li><li><a href="https://github.com/Tayyab885/BookRecommendationSystem">GitHub link</a></li></ul>', unsafe_allow_html=True)

    st.markdown('<hr>', unsafe_allow_html=True)
    
    # Project 4
    with st.container():
        col1, col2 = st.columns([2, 3])
        col1.image('Images/superstore.jpg', caption='', use_column_width=True)
        col2.markdown('<h2>Superstore Sales Analysis:</h2><ul><li>Performed data pre-processing using Python and Pandas to clean and refine the Superstore Sales dataset, removing duplicates, handling null values, and removing irrelevant data.</li><li>Conducted SQL analysis on the cleaned dataset to identify trends and insights in customer behavior, sales performance, and operational aspects of the superstore.</li><li>Generated queries to identify the top three customers with the highest total value of orders, calculate the percentage of total orders that were shipped on the same date, and determine the most demanded sub-category in the west region.</li><li>Analyzed the sales data to determine which customer segment was more likely to choose first-class shipping, which city was least contributing to total revenue, and what the average time for orders to get shipped after an order was placed.</li><li>Built using Streamlit and deployed on the Streamlit cloud.</li><li><a href="https://github.com/Tayyab885/Superstore-Sales-Analysis">GitHub link</a></li></ul>', unsafe_allow_html=True)


    st.markdown('<hr>', unsafe_allow_html=True)
    
    # Project 5
    with st.container():
        col1, col2 = st.columns([2, 3])
        col1.image('Images/covid.jpg', caption='', use_column_width=True)
        col2.markdown('<h2>Covid-19 Data Analysis:</h2><ul><li>Analyzed Covid-19 data using SQL to calculate death rates, infection percentages, and vaccination rates.</li><li>Conducted data analysis to inform decision-making and understand Covid-19 trends.</li><li>Identified countries and continents with the highest Covid-19 infection and death rates per population.</li><li>Calculated the percentage of the population in Pakistan that has been infected with Covid-19.</li><li>Analyzed Covid-19 vaccination data in Pakistan, including calculating the percentage of the population that has been vaccinated so far.</li><li><a href="https://github.com/Tayyab885/Covid-19-Data-Analysis-Using-SQL">GitHub link</a></li></ul>', unsafe_allow_html=True)

    st.markdown('<hr>', unsafe_allow_html=True)




        
st.markdown('</div>', unsafe_allow_html=True)
        
