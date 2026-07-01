import streamlit as st
from streamlit_pdf_viewer import pdf_viewer

st.set_page_config(layout="wide")

banner_url = "https://upload.wikimedia.org/wikipedia/commons/e/e8/Radia_Perlman_%2820175426302%29.jpg"

st.markdown("""
<style>

::root {
    scroll-behavior: smooth
    color: var(--text-color);
    padding-bottom: 4px;
}

[data-testid="stAppViewContainer"] {
    padding: 0 !important;
}

section[data-testid="stMain"] {
    padding: 0 !important;
}

[data-testid="stMainBlockContainer"] {
    max-width: 100% !important;
    max-height: 100% !important;
    padding: 0 !important;
}

[data-testid="stMain"] > div {
    padding: 0 !important;
}

/* ── Layout ── */
[data-testid="block-container"] {
    padding: 0 !important;
}

/* ── Hero image container ── */
.hero {
    position: relative;
    width: 100vw;
    height: 70vh;
    overflow: hidden;
}

/* ── Hero image styling ── */
.hero img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    filter: grayscale(100%) contrast(1.2) brightness(0.75);
}

/* ── Centered text overlay on hero ── */
.hero-text {
    position: absolute;
    top: 50%;
    left: 0;
    right: 0;
    transform: translateY(-50%);
    color: white;
    text-align: center;
}

.hero-text h1 {
    font-size: 4rem;
    margin: 0;
    line-height: 1;
    color: white;
    text-shadow:
        0 0 8px rgba(0,0,0,0.9),
        0 0 20px rgba(0,0,0,0.7);
}

.hero-text p {
    font-size: 1.2rem;
    opacity: 0.85;
    margin: 0.5rem 0 0 0;
    padding: 0;
}

/* ── Image caption below hero ── */
.hero-caption {
    text-align: left;
    font-size: 0.9rem;
    color: #666;
    margin-top: 8px;
    margin-bottom: 24px;
    padding-left: 1rem;
}

.headings h1 {
    font-size: 3rem;
    line-height: 1;
    color: var(--text-color);
    text-align: center;
}


/* ── Hide sidebar ── */
[data-testid="stSidebar"] {
    display: none !important;
}

[data-testid="stSidebarCollapsedControl"] {
    display: none !important;
}

[data-testid="stElementContainer"]:has(canvas) {
    height: calc(100vh - 80px);
}

</style>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="hero">
    <img src="{banner_url}">
    <div class="hero-text">
        <h1>Written Materials</h1>
    </div>
</div>

<div class="hero-caption">
    Image: Jalisco Campus Party, CC BY 2.0 <https://creativecommons.org/licenses/by/2.0>, via Wikimedia Commons
</div>

""", unsafe_allow_html=True)

with open("process_paper.pdf", "rb") as f:
    process_paper = f.read()

with open("annotated.pdf", "rb") as f:
    annotated = f.read()


st.markdown("""
<div class="headings">
    <h1>Process Paper:</h1>
</div>
""", unsafe_allow_html=True)

st.space(50)

pdf_viewer(
    input=process_paper,
    width="45%",
    height=1400
)

st.space(50)

st.markdown("""
<div class="headings">
    <h1>Annotated Bibliography:</h1>
</div>
""", unsafe_allow_html=True)

st.space(50)

pdf_viewer(
    input=annotated,
    width="45%",
    height=1400
)

