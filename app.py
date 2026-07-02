import streamlit as st
import pandas as pd
import numpy as np

# Page configuration (Isse app ka layout thoda wide ho jayega)
st.set_page_config(page_title="My Dashboard", layout="wide")

# Sidebar bana rahe hain
st.sidebar.header("User Settings ⚙️")
username = st.sidebar.text_input("Apna Naam Likhein:")

# Sidebar mein ek slider
chart_data_count = st.sidebar.slider("Kitna data dekhna hai?", min_value=10, max_value=100, value=20)

# Main Screen Layout
st.title("📊 My Smart Dashboard")

if username:
    st.subheader(f"Welcome back, {username}! ✨")
else:
    st.subheader("Welcome! Sidebar mein apna naam likhein.")

st.write("---") # Ek horizontal line line khinchne ke liye

# Ek random graph data generate kar rahe hain slider ke hisab se
st.write("### Live Data Chart")
chart_data = pd.DataFrame(
    np.random.randn(chart_data_count, 2),
    columns=['Sales', 'Profit']
)

# Graph ko screen par display karna
st.line_chart(chart_data)

# Ek success alert aur celebration animation
if st.sidebar.button("Celebrate! 🎉"):
    st.balloons()
    st.success("Badhai ho! Aapka pehla dashboard tayar hai.")