import streamlit as st 

st.title("PORTFOLIO")
st.markdown("<h2 style='background-color: hotpink; color: black;'>HARINI</h2>", unsafe_allow_html=True)
st.write("Welcome to my portfolio! im excited to share my projects and passions with you.dive in to see what i ve been working on!creativity meets dedicatiion,and each project is a step forward in my journey.explore ,and join e on this path of growth and innovation.by the way Thanks for stopping by my portfolio! I'm always exploring new ideas and pushing boundaries. Here you’ll find my latest projects and skills—I’m eager to connect and see where new opportunities might take us.")
col1, col2 = st.columns(2)

with col1:
    st.header("DESIGNATION")
    st.markdown(
        '<div style="background-color:aqua; padding:20px; border-radius:10px;color:black">Student</div>',
        unsafe_allow_html=True
    )

with col2:
    st.header("PROGRAMME")
    st.markdown(
        '<div style="background-color:aqua; padding:20px;border-radius:10px;color:black"> b tech ai and ds</div>',
        unsafe_allow_html=True
    )
    
import streamlit as st
st.image("https://wallpapers.com/images/hd/artificial-intelligence-circuit-board-69oj9x05ytbg0e7h.jpg",width=700)  



import streamlit as st

complexity = st.slider("About my skills:", min_value=1, max_value=2, value=2)

if complexity == 1:
    st.write("Hi, my name is Harini. I am currently pursuing my undergraduate studies at KGISL Institute of Technology in the Department of Artificial Intelligence and Data Science. I completed my higher secondary education at Vimal Jyothi Convent, where I laid the foundation for my academics.")
elif complexity == 2:
    st.write("my goal is to become data scientist.A data scientist is a professional who uses data to help organizations make better decisions and improve their operations. They use their skills in mathematics, statistics, and computer science to analyze large data sets and find patterns and trends")

st.markdown("""
    <h2 style="background: rgb(232,70,252);
    background: radial-gradient(circle, rgba(232,70,252,1) 19%, rgba(190,67,230,1) 38%, rgba(111,68,219,1) 51%, rgba(229,69,212,1) 59%, rgba(178,70,228,1) 69%, rgba(222,70,235,1) 84%, rgba(244,70,252,1) 98%);
    color: black; padding: 10px; text-align: center;">Skills</h2>
""", unsafe_allow_html=True)
skills = [
    "Python Programming",
    "html",
    "css",
    "javascript",
    "bootstrap"
    "web page developer"
    
]

# Displaying skills
for skill in skills:
    st.markdown(f"- {skill}")
    
    
st.image("https://img.freepik.com/premium-photo/4k-robot-cuteultra-instinchyper-realistic_605905-6006.jpg",width=700)  

import streamlit as st

col1, col2 = st.columns(2)

with col1:

    st.markdown(
      '<h2 style="background-color:hotpink;color:black;padding:20px;">GOAL</h2>',
        unsafe_allow_html=True
    )


st.text("")     

with col2:
    
    st.markdown(
         '<h2 style="background-color:hotpink;color:black;padding:20px;">CONTACT</h2>',
        unsafe_allow_html=True
       
    )

import streamlit as st

col1, col2 = st.columns(2)

with col1:

    st.markdown(
        '<h2 style="background-color:aqua;color:black;padding:20px;border-radius:35px;">data scientist</h2>',
        unsafe_allow_html=True
    )


st.text("")     

with col2:
    
    st.markdown(
        '<h2 style="background-color:aqua;color:black;padding:20px;border-radius:35px;">999776533</h2>',
        unsafe_allow_html=True
    )
    import streamlit as st

st.text("")  

st.text("") 

# Projects Section
st.header("Projects")
st.write("Here are some of the projects I've worked on:")

# Add individual project entries here
project_1 = "Project 1: [web page design]"
st.subheader(project_1)
st.write("i have desiged a webpage using basic html and css bootstrap and javascript it was website created for chocolate shop")
st.write("Technologies used: html,css,bootstrap etc.")

st.text("") 

project_2 = "Project 2: [login page  of social media]"
st.subheader(project_2)
st.write("i have desiged a loginpage using javascript ")
st.write("Technologies used: html,css,javascript etc.")





st.markdown("""
    <h2 style="background: rgb(232,70,252);
    background: radial-gradient(circle, rgba(232,70,252,1) 19%, rgba(190,67,230,1) 38%, rgba(111,68,219,1) 51%, rgba(229,69,212,1) 59%, rgba(178,70,228,1) 69%, rgba(222,70,235,1) 84%, rgba(244,70,252,1) 98%);
    color: black; padding: 10px; text-align: center;">EMAIL</h2>
""", unsafe_allow_html=True) 


st.text("") 

st.markdown("""
    <h2 style="background-color:lavender;color:black">harinimurugesan16018@gmail.com</h2>
""", unsafe_allow_html=True)


st.text("") 

st.text("")
st.markdown("""
    <h2 style="background: rgb(232,70,252);
    background: radial-gradient(circle, rgba(232,70,252,1) 19%, rgba(190,67,230,1) 38%, rgba(111,68,219,1) 51%, rgba(229,69,212,1) 59%, rgba(178,70,228,1) 69%, rgba(222,70,235,1) 84%, rgba(244,70,252,1) 98%);
    color: black; padding: 10px; text-align: center;">LINKED IN PROFILE</h2>
""", unsafe_allow_html=True) 

st.text("")

st.markdown("""
    <h2 style="background-color:lavender;color:black">harinimurugesan@linkedin </h2>
""", unsafe_allow_html=True)


st.header("Thank You for Visiting!")

st.write("I hope you enjoyed exploring my portfolio. I'm always excited to connect and discuss potential collaborations or opportunities. Please feel free to reach out!")



st.markdown("""
    <h1 style="background-color:hotpink;color:white">GET IN TOUCH!</h1>
""", unsafe_allow_html=True)
