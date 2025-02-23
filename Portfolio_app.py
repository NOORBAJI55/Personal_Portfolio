

import streamlit as st
from PIL import Image


import streamlit as st
from PIL import Image

# Set page config (MUST be the first Streamlit command)
st.set_page_config(page_title="Shaik Noor Baji - Portfolio", page_icon=":rocket:", layout="wide")

# Load profile picture
profile_pic = "IMG-20230828-WA0006.jpg"  # Use uploaded image



# Load profile picture
# profile_pic = "IMG-20230828-WA0006.jpg"  # Use uploaded image
profile_pic = "IMG-20230828-WA0006.jpg"
st.image(profile_pic, width=200)

# Set page config
st.set_page_config(page_title="Shaik Noor Baji - Portfolio", page_icon=":rocket:", layout="wide")

# Apply custom CSS for better styling
st.markdown(
    """
    <style>
        body {background-color: #f4f4f4;}
        .main {background-color: #ffffff; padding: 20px; border-radius: 10px;}
        h1 {color: #2E86C1;}
        h2 {color: #2874A6;}
        h3 {color: #21618C;}
        .stButton button {background-color: #2874A6; color: white; border-radius: 10px;}
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About Me", "Internships", "Projects", "Skills", "Certificates", "Contact"])

# Home Page
if page == "Home":
    st.title("Shaik Noor Baji")
    st.image(profile_pic, width=200)
    st.write("### Aspiring Data Scientist & Full-Stack Developer")
    st.write("Passionate about AI, Machine Learning, and Web Development. Experienced in Python, Java, MERN Stack, and Cloud Technologies.")
    st.write("[LinkedIn](https://www.linkedin.com/in/shaik-noor-baji/) | [GitHub](https://github.com/NOORBAJI55)")

# About Me
elif page == "About Me":
    st.header("About Me")
    st.image(profile_pic, width=150)
    st.write("### Education")
    st.write("- **B.Tech (CSE)** - NRI Institute of Technology (CGPA: 7.69)")
    st.write("- **Intermediate (MPC)** - Sri Vagdevi Jr College (82.6%)")
    st.write("- **SSC** - Kumar Public School (CGPA: 9.8)")

# Internships
elif page == "Internships":
    st.header("Internships")
    st.subheader("HMI Engineering Services (Feb 2023 – Jun 2023)")
    st.write("- Full Stack Java Developer - Improved service processes and optimized workflows.")
    st.subheader("BIST TECHNOLOGIES (Jun 2024 – Jul 2024)")
    st.write("- Machine Learning - Developed predictive models and data analytics.")
    st.subheader("ExcelR (May 2024 – Jul 2024)")
    st.write("- MERN Stack - Built and deployed full-stack applications.")

# Projects
elif page == "Projects":
    st.header("Projects")
    st.write("### Blog Application")
    st.write("Technologies: Flask, SQLite3, HTML, CSS")
    st.write("A dynamic blog platform with CRUD operations.")
    st.write("[GitHub](https://github.com/NOORBAJI55)")
    
    st.write("### Days Calculator")
    st.write("A Python-based CLI app to calculate days lived from birth.")
    st.write("[GitHub](https://github.com/NOORBAJI55/DaysCalculator)")
    
    st.write("### YouTube Downloader")
    st.write("A web app to download YouTube videos and audio.")
    st.write("[Live App](https://youtube-video-audio-downloader-online.streamlit.app/)")
    
# Skills
elif page == "Skills":
    st.header("Technical Skills")
    st.write("- Python, Java, C, HTML/CSS, JavaScript, SQL, Flask")
    st.write("- Developer Tools: VS Code, Eclipse, Google Cloud Platform")
    st.write("- Technologies: GitHub, MERN Stack, Machine Learning")

# Certificates
elif page == "Certificates":
    st.header("Certifications")
    st.write("- Microsoft: Azure Data Engineer, Azure AI Engineer")
    st.write("- IBM: Data Analysis, Data Visualization, Python for Data Science")
    st.write("- NPTEL: IoT Technology (72%, Elite Badge)")
    st.write("- AWS: Introduction to Machine Learning")
    st.write("- Great Learning: Flask Python")
    st.write("- Coursera: Google Ads for Beginners")
    st.write("- Simplilearn: Power BI, Generative AI")
    st.write("- GUVI: Generative AI, Python")

# Contact
elif page == "Contact":
    st.header("Contact Information")
    st.write("📧 Email: shaiknoorbaji35@gmail.com")
    st.write("📞 Phone: +91 9505163556")
    st.write("[LinkedIn](https://www.linkedin.com/in/shaik-noor-baji/) | [GitHub](https://github.com/NOORBAJI55)")
