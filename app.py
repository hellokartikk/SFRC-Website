
import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="Predicting Flexural Strength of SFRC",
    layout="wide"
)

# Load the HTML website
html_file = Path("index.html")

if not html_file.exists():
    st.error("index.html not found in the project folder.")
else:
    html_content = html_file.read_text(encoding="utf-8")
    components.html(html_content, height=1200, scrolling=True)
