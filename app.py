import streamlit as st

st.set_page_config(
    page_title="Mundial 2026",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Quitar márgenes y elementos visuales de Streamlit
st.markdown("""
<style>
    .block-container {
        padding: 0 !important;
        max-width: 100% !important;
    }

    header[data-testid="stHeader"] {
        display: none;
    }


    #MainMenu {
        visibility: hidden;
    }
</style>
""", unsafe_allow_html=True)

with open("index.html", "r", encoding="utf-8") as archivo:
    html = archivo.read()

with open("style.css", "r", encoding="utf-8") as archivo:
    css = archivo.read()

with open("script.js", "r", encoding="utf-8") as archivo:
    js = archivo.read()

html = html.replace(
    '<link rel="stylesheet" href="style.css">',
    f"<style>{css}</style>"
)

html = html.replace(
    '<script src="script.js"></script>',
    f"<script>{js}</script>"
)

st.html(
    html,
    width="stretch",
    unsafe_allow_javascript=True
)