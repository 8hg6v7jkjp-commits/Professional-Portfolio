import streamlit as st

st.set_page_config(
    page_title="Nathan Kasperek | Portfolio",
    page_icon="📊",
    layout="wide"
)

# =========================================================
# HEADER
# =========================================================

st.title("Nathan Kasperek")

st.subheader("Marketing Major | Aspiring Marketing Analyst")

st.write(
    "Marquette, Michigan | "
    "(734) 626-6907 | "
    "natkas0627@gmail.com"
)


col1, col2 = st.columns(2)

with col1:
    st.image("profile_picture.png", width=200)

with col2:
    st.subheader("Important Links")
    st.link_button(
        "LinkedIn",
        "https://www.linkedin.com/in/nathan-kasperek-412494391/",
        width = "stretch"
    )

    st.link_button(
            "GitHub",
            "https://github.com/8hg6v7jkjp-commits",
            width = "stretch"
        )
    with open("Kasperek_Resume.pdf", "rb") as pdf:
        pdf_bytes = pdf.read()

    st.download_button(
        label="Download My Resume",
        data=pdf_bytes,
        file_name="Kasperek_Resume.pdf",
        mime="application/pdf",
        width="stretch"
    )

st.divider()


# =========================================================
# ABOUT ME
# =========================================================

with st.expander("About Me", expanded=True):

    st.write("""
    I am a Marketing major with a growing interest in data analytics, programming, and business decision-making. I enjoy solving problems using code, and I spend my free time programming and building apps for my personal life. I’m particularly interested in finding ways to apply customer segmentation using technology to better understand who an organization's customer's are.

Some of my other academic interests include philosophy, psychology and mathematics. I enjoy exploring how things work and learning through experimentation and hands-on projects. I am a naturally curious and independent learner who enjoys teaching myself new skills and applying what I learn to real-world problems.

Outside of academics and programming, I enjoy hiking, biking, snowboarding, music, weightlifting and spending time with friends.

    """)
