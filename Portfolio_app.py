# import streamlit as st
# from PIL import Image

# # Set page configuration (Must be the first Streamlit command)
# st.set_page_config(page_title="Shaik Noor Baji - Portfolio", page_icon="🚀", layout="wide")

# # Load profile picture
# profile_pic = "IMG-20230828-WA0006.jpg"

# # Apply custom CSS for improved styling
# st.markdown(
#     """
#     <style>
#         body {background-color: #f8f9fa;}
#         .main {background-color: #ffffff; padding: 30px; border-radius: 12px; box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);}
#         h1 {color: #0056b3; font-size: 32px;}
#         h2 {color: #0073e6; font-size: 28px;}
#         h3 {color: #008cba; font-size: 24px;}
#         .stButton button {background-color: #0073e6; color: white; font-size: 16px; border-radius: 8px; padding: 10px 20px;}
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # Sidebar Navigation
# st.sidebar.title("📌 Navigation")
# page = st.sidebar.radio("Jump to Section", ["🏠 Home", "📖 About Me", "💼 Internships", "🚀 Projects", "📚 Skills", "🏅 Certifications", "📞 Contact"])

# # ---- Home Page ----
# if page == "🏠 Home":
#     st.title("🚀 Shaik Noor Baji")
#     st.image(profile_pic, width=200)
#     st.subheader("Aspiring Data Scientist & Full-Stack Developer")
#     st.write(
#         "Passionate about AI, Machine Learning, and Web Development. "
#         "Experienced in Python, Java, MERN Stack, and Cloud Technologies."
#     )
#     st.write("📌 [LinkedIn](https://www.linkedin.com/in/shaik-noor-baji/) | [GitHub](https://github.com/NOORBAJI55)")

# # ---- About Me ----
# elif page == "📖 About Me":
#     st.header("📖 About Me")
#     st.image(profile_pic, width=150)
#     st.write("### 🎓 Education")
#     st.write("- **B.Tech (CSE)** - NRI Institute of Technology (CGPA: 7.69)")
#     st.write("- **Intermediate (MPC)** - Sri Vagdevi Jr College (82.6%)")
#     st.write("- **SSC** - Kumar Public School (CGPA: 9.8)")

# # ---- Internships ----
# elif page == "💼 Internships":
#     st.header("💼 Internships")
    
#     st.subheader("HMI Engineering Services (Feb 2023 – Jun 2023)")
#     st.write("🔹 Full Stack Java Developer - Improved service processes and optimized workflows.")
    
#     st.subheader("BIST TECHNOLOGIES (Jun 2024 – Jul 2024)")
#     st.write("🔹 Machine Learning - Developed predictive models and data analytics.")
    
#     st.subheader("ExcelR (May 2024 – Jul 2024)")
#     st.write("🔹 MERN Stack - Built and deployed full-stack applications.")

# # ---- Projects ----
# elif page == "🚀 Projects":
#     st.header("🚀 Projects")
    
#     st.subheader("📝 Blog Application")
#     st.write("💡 Technologies: Flask, SQLite3, HTML, CSS")
#     st.write("📌 A dynamic blog platform with CRUD operations.")
#     st.write("[🔗 GitHub](https://github.com/NOORBAJI55)")
    
#     st.subheader("📅 Days Calculator")
#     st.write("🔹 A Python-based CLI app to calculate days lived from birth.")
#     st.write("[🔗 GitHub](https://github.com/NOORBAJI55/DaysCalculator)")
    
#     st.subheader("🎬 YouTube Downloader")
#     st.write("🔹 A web app to download YouTube videos and audio.")
#     st.write("[🌐 Live App](https://youtube-video-audio-downloader-online.streamlit.app/)")

# # ---- Skills ----
# elif page == "📚 Skills":
#     st.header("📚 Technical Skills")
#     st.write("✔️ Python, Java, C, HTML/CSS, JavaScript, SQL, Flask")
#     st.write("✔️ Developer Tools: VS Code, Eclipse, Google Cloud Platform")
#     st.write("✔️ Technologies: GitHub, MERN Stack, Machine Learning")

# # ---- Certifications ----
# elif page == "🏅 Certifications":
#     st.header("🏅 Certifications")
#     st.write("- 🏆 **Microsoft**: Azure Data Engineer, Azure AI Engineer")
#     st.write("- 🏆 **IBM**: Data Analysis, Data Visualization, Python for Data Science")
#     st.write("- 🏆 **NPTEL**: IoT Technology (72%, Elite Badge)")
#     st.write("- 🏆 **AWS**: Introduction to Machine Learning")
#     st.write("- 🏆 **Great Learning**: Flask Python")
#     st.write("- 🏆 **Coursera**: Google Ads for Beginners")
#     st.write("- 🏆 **Simplilearn**: Power BI, Generative AI")
#     st.write("- 🏆 **GUVI**: Generative AI, Python")

# # ---- Contact ----
# elif page == "📞 Contact":
#     st.header("📞 Contact Information")
#     st.write("📧 **Email:** shaiknoorbaji35@gmail.com")
#     st.write("📞 **Phone:** +91 9505163556")
#     st.write("[🔗 LinkedIn](https://www.linkedin.com/in/shaik-noor-baji/) | [🔗 GitHub](https://github.com/NOORBAJI55)")


import streamlit as st
from PIL import Image

# Set page configuration
st.set_page_config(page_title="Shaik Noor Baji - Portfolio", page_icon="🚀", layout="wide")

# Load profile picture
profile_pic = "IMG-20230828-WA0006.jpg"

# Apply custom CSS for bright and engaging UI
st.markdown(
    """
    <style>
        body {background-color: #f8f9fa;}
        .main {background: linear-gradient(135deg, #ff9a9e, #fad0c4); padding: 30px; border-radius: 12px; box-shadow: 4px 4px 15px rgba(0, 0, 0, 0.2);}
        h1 {color: #ff5733; font-size: 36px; text-align: center;}
        h2 {color: #ff6f61; font-size: 28px;}
        h3 {color: #ff914d; font-size: 24px;}
        .stButton button {background: #ff4500; color: white; font-size: 18px; border-radius: 8px; padding: 12px 25px; font-weight: bold;}
        .stSidebar {background: linear-gradient(135deg, #ff758c, #ff7eb3);}
        .stSidebar .stRadio label {color: white; font-size: 18px; font-weight: bold;}
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar Navigation
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Jump to Section", ["🏠 Home", "📖 About Me", "💼 Internships", "🚀 Projects", "📚 Skills", "🏅 Certifications", "📞 Contact"])

# ---- Home Page ----
if page == "🏠 Home":
    st.title("🚀 Shaik Noor Baji")
    st.image(profile_pic, width=200)
    st.subheader("🔥 Aspiring Data Scientist & Full-Stack Developer")
    st.write(
        "💡 Passionate about AI, Machine Learning, and Web Development. "
        "Experienced in Python, Java, MERN Stack, and Cloud Technologies."
    )
    st.write("🔗 [LinkedIn](https://www.linkedin.com/in/shaik-noor-baji/) | 🔗 [GitHub](https://github.com/NOORBAJI55)")

# ---- About Me ----
elif page == "📖 About Me":
    st.header("📖 About Me")
    st.image(profile_pic, width=150)
    st.write("### 🎓 Education")
    st.write("- 📌 **B.Tech (CSE)** - NRI Institute of Technology (CGPA: 7.69)")
    st.write("- 📌 **Intermediate (MPC)** - Sri Vagdevi Jr College (82.6%)")
    st.write("- 📌 **SSC** - Kumar Public School (CGPA: 9.8)")

# ---- Internships ----
elif page == "💼 Internships":
    st.header("💼 Internships")
    
    st.subheader("🎯 HMI Engineering Services (Feb 2023 – Jun 2023)")
    st.write("🔹 Full Stack Java Developer - Improved service processes and optimized workflows.")
    
    st.subheader("🎯 BIST TECHNOLOGIES (Jun 2024 – Jul 2024)")
    st.write("🔹 Machine Learning - Developed predictive models and data analytics.")
    
    st.subheader("🎯 ExcelR (May 2024 – Jul 2024)")
    st.write("🔹 MERN Stack - Built and deployed full-stack applications.")

# ---- Projects ----
elif page == "🚀 Projects":
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

# ---- Skills ----
elif page == "📚 Skills":
    st.header("📚 Technical Skills")
    st.write("🔥 **Programming Languages:** Python, Java, C, HTML/CSS, JavaScript, SQL, Flask")
    st.write("🔥 **Developer Tools:** VS Code, Eclipse, Google Cloud Platform")
    st.write("🔥 **Technologies:** GitHub, MERN Stack, Machine Learning")

# ---- Certifications ----
elif page == "🏅 Certifications":
    st.header("🏅 Certifications")
    st.write("🏆 **Microsoft:** Azure Data Engineer, Azure AI Engineer")
    st.write("🏆 **IBM:** Data Analysis, Data Visualization, Python for Data Science")
    st.write("🏆 **NPTEL:** IoT Technology (72%, Elite Badge)")
    st.write("🏆 **AWS:** Introduction to Machine Learning")
    st.write("🏆 **Great Learning:** Flask Python")
    st.write("🏆 **Coursera:** Google Ads for Beginners")
    st.write("🏆 **Simplilearn:** Power BI, Generative AI")
    st.write("🏆 **GUVI:** Generative AI, Python")

# ---- Contact ----
elif page == "📞 Contact":
    st.header("📞 Contact Information")
    st.write("📧 **Email:** shaiknoorbaji35@gmail.com")
    st.write("📞 **Phone:** +91 9505163556")
    st.write("🔗 [LinkedIn](https://www.linkedin.com/in/shaik-noor-baji/) | 🔗 [GitHub](https://github.com/NOORBAJI55)")

