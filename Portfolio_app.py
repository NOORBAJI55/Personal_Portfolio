import streamlit as st
from PIL import Image

# # Set page configuration
st.set_page_config(page_title="Shaik Noor Baji - Portfolio", page_icon="🚀", layout="wide")

 # Load profile picture
profile_pic = "IMG-20230828-WA0006.jpg"


st.markdown(
    """
    <style>
        body {background-color: #f8f9fa;}
        .main {background: linear-gradient(135deg, #ff9a9e, #fad0c4); padding: 30px; border-radius: 12px; box-shadow: 4px 4px 15px rgba(0, 0, 0, 0.2);}
        h1 {color: #ff5733; font-size: 36px; text-align: center;}
        h2 {color: #ff6f61; font-size: 28px;}
        h3 {color: #ff914d; font-size: 24px;}
        .stButton button {background: #ff4500; color: white; font-size: 18px; border-radius: 8px; padding: 12px 25px; font-weight: bold;}
        .stSidebar {background: linear-gradient(135deg, #ff758c, #ff7eb3); padding: 20px; border-radius: 12px;}
        .stSidebar .stRadio label {color: white; font-size: 18px; font-weight: bold;}
        .nav-box {background-color: #ffffff; padding: 10px; margin: 10px 0; border-radius: 8px; text-align: center; font-weight: bold; box-shadow: 2px 2px 10px rgba(0,0,0,0.1);}
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar Navigation with Boxed Design
st.sidebar.title("📌 Quick Navigation")
st.sidebar.markdown('<div class="nav-box"><a href="#home">🏠 Home</a></div>', unsafe_allow_html=True)
st.sidebar.markdown('<div class="nav-box"><a href="#about-me">📖 About Me</a></div>', unsafe_allow_html=True)
st.sidebar.markdown('<div class="nav-box"><a href="#internships">💼 Internships</a></div>', unsafe_allow_html=True)
st.sidebar.markdown('<div class="nav-box"><a href="#projects">🚀 Projects</a></div>', unsafe_allow_html=True)
st.sidebar.markdown('<div class="nav-box"><a href="#skills">📚 Skills</a></div>', unsafe_allow_html=True)
st.sidebar.markdown('<div class="nav-box"><a href="#certifications">🏅 Certifications</a></div>', unsafe_allow_html=True)
st.sidebar.markdown('<div class="nav-box"><a href="#contact">📞 Contact</a></div>', unsafe_allow_html=True)

st.write("________________________________________________________________________________________________________________________________________________________________________________________")

 # ---- Home Section ----
st.markdown('<div class="hidden_anchor" id="home"></div>', unsafe_allow_html=True)
st.container()
st.title("🚀 Shaik Noor Baji")
st.image(profile_pic, width=200)
st.subheader("🔥 Aspiring Data Scientist & Full-Stack Developer")
st.write(
     "💡 Passionate about AI, Machine Learning, and Web Development. "
     "Experienced in Python, Java, MERN Stack, and Cloud Technologies."
 )
st.write("🔗 [LinkedIn](https://www.linkedin.com/in/shaik-noor-baji/) | 🔗 [GitHub](https://github.com/NOORBAJI55)")

st.write("________________________________________________________________________________________________________________________________________________________________________________________")

 # ---- About Me ----
st.markdown('<div class="hidden_anchor" id="about-me"></div>', unsafe_allow_html=True)
st.container()
st.header("📖 About Me")
# st.image(profile_pic, width=150)
st.write("### 🎓 Education")
st.write("- 📌 **B.Tech (CSE)** - NRI Institute of Technology (CGPA: 7.69)")
st.write("- 📌 **Intermediate (MPC)** - Sri Vagdevi Jr College (82.6%)")
st.write("- 📌 **SSC** - Kumar Public School (CGPA: 9.8)")

st.write("________________________________________________________________________________________________________________________________________________________________________________________")

 # ---- Internships ----
st.markdown('<div class="hidden_anchor" id="internships"></div>', unsafe_allow_html=True)
st.container()
st.header("💼 Internships")

st.subheader("🎯 HMI Engineering Services (Feb 2023 – Jun 2023)")
st.write("🔹 Full Stack Java Developer - Improved service processes and optimized workflows.")

st.subheader("🎯 BIST TECHNOLOGIES (Jun 2024 – Jul 2024)")
st.write("🔹 Machine Learning - Developed predictive models and data analytics.")

st.subheader("🎯 ExcelR (May 2024 – Jul 2024)")
st.write("🔹 MERN Stack - Built and deployed full-stack applications.")

st.write("________________________________________________________________________________________________________________________________________________________________________________________")

 # ---- Projects ----
st.markdown('<div class="hidden_anchor" id="projects"></div>', unsafe_allow_html=True)
st.container()
st.header("🚀 Projects")

st.subheader("📝 Blog Application")
st.write("💡 Technologies: Flask, SQLite3, HTML, CSS")
st.write("📌 A dynamic blog platform with CRUD operations.")
st.write("[🔗 GitHub](https://github.com/NOORBAJI55)")

st.subheader("📅 Days Calculator")
st.write("🔹 A Python-based CLI app to calculate days lived from birth.")
st.write("[🔗 GitHub](https://github.com/NOORBAJI55/DaysCalculator)")

st.subheader("🎬 YouTube Downloader")
st.write("🔹 A web app to download YouTube videos and audio.")
st.write("[🌐 Live App](https://youtube-video-audio-downloader-online.streamlit.app/)")

st.subheader("Language_Detector 🔍")
st.write("🔹 A Python script that detects the language of a given text using the langdetect library. Supports detection of over 70 languages. Simply input a sentence, and the script will identify the language.#language-detection #NLP #Python #langdetect")
st.write("[🔗 GitHub](https://github.com/NOORBAJI55/Language_Detector)")

st.write("________________________________________________________________________________________________________________________________________________________________________________________")

 # ---- Skills ----
st.markdown('<div class="hidden_anchor" id="skills"></div>', unsafe_allow_html=True)
st.container()
st.header("📚 Technical Skills")
st.write("🔥 **Programming Languages:** Python, Java, C, HTML/CSS, JavaScript, SQL, Flask")
st.write("🔥 **Developer Tools:** VS Code, Eclipse, Google Cloud Platform")
st.write("🔥 **Technologies:** GitHub, MERN Stack, Machine Learning")

st.write("________________________________________________________________________________________________________________________________________________________________________________________")

 # ---- Certifications ----
st.markdown('<div class="hidden_anchor" id="certifications"></div>', unsafe_allow_html=True)
st.container()
st.header("🏅 Certifications")
st.write("🏆 **Microsoft:** Azure Data Engineer, Azure AI Engineer")
st.write("🏆 **IBM:** Data Analysis, Data Visualization, Python for Data Science")
st.write("🏆 **NPTEL:** IoT Technology (72%, Elite Badge)")
st.write("🏆 **AWS:** Introduction to Machine Learning")
st.write("🏆 **Great Learning:** Flask Python")
st.write("🏆 **Coursera:** Google Ads for Beginners")
st.write("🏆 **Simplilearn:** Power BI, Generative AI")
st.write("🏆 **GUVI:** Generative AI, Python")

st.write("________________________________________________________________________________________________________________________________________________________________________________________")

# # ---- Contact ----
st.markdown('<div class="hidden_anchor" id="contact"></div>', unsafe_allow_html=True)
st.container()
st.header("📞 Contact Information")
st.write("📧 **Email:** shaiknoorbaji35@gmail.com")
st.write("📞 **Phone:** +91 9505163556")
st.write("🔗 [LinkedIn](https://www.linkedin.com/in/shaik-noor-baji/) | 🔗 [GitHub](https://github.com/NOORBAJI55)")
st.write("________________________________________________________________________________________________________________________________________________________________________________________")

