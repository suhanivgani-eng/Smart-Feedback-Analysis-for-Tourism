import streamlit as st
import streamlit.components.v1 as components
import os

# 1. Page Configuration
st.set_page_config(page_title="Tourism Intelligence", layout="wide")

# 2. Function to load your files
def load_html():
    with open("index.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    
    # We need to inject the CSS and JS directly into the HTML 
    # because Streamlit components handle external files strictly.
    with open("styles.css", "r", encoding="utf-8") as c:
        css_content = f"<style>{c.read()}</style>"
        
    with open("app.js", "r", encoding="utf-8") as j:
        js_content = f"<script>{j.read()}</script>"
        
    # Combine them
    return html_content.replace('<link rel="stylesheet" href="styles.css" />', css_content).replace('<script src="app.js"></script>', js_content)

# 3. Render the App
st.markdown("### Tourism Feedback Dashboard") # Optional Streamlit header
full_app_code = load_html()
components.html(full_app_code, height=900, scrolling=True)
