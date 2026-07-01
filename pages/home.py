import streamlit as st
from streamlit_theme import st_theme

banner_url = "https://upload.wikimedia.org/wikipedia/commons/9/9e/Radia_Perlman_%2820175369862%29.jpg"

theme = st_theme()

bg = theme["backgroundColor"]

if bg == "#0e1117":
    st.markdown("""
    <style>
    
    html {
        scroll-behavior: smooth
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
    
    /* ── Thesis link ── */
    .thesis-cta {
        text-align: center;
        margin: 3rem auto;
    }
    
    .thesis-cta a {
        font-size: 2rem;
        font-weight: bold;
        color: white;
        text-decoration: none;
        border-bottom: 3px solid white;
        padding-bottom: 4px;
    }
    
    .thesis-cta a:hover {
        opacity: 0.6;
    }
    
    /* ── Metadata block under thesis link ── */
    .thesis-meta {
        margin-top: 1.5rem;
        text-align: center;
    }
    
    .thesis-meta p {
        font-size: 2rem;
        font-weight: bold;
        color: white;
        padding-bottom: 4px;
        margin: 0.3rem 0;
    }
    
    /* ── Hide sidebar ── */
    [data-testid="stSidebar"] {
        display: none !important;
    }
    
    [data-testid="stSidebarCollapsedControl"] {
        display: none !important;
    }
    
    </style>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="hero">
        <img src="{banner_url}">
        <div class="hero-text">
            <h1>Breaking the Loop:</h1>
            <p>How Radia Perlman Made the Modern Internet Possible</p>
        </div>
    </div>
    
    <div class="hero-caption">
        Image: Jalisco Campus Party, CC BY 2.0, via Wikimedia Commons
    </div>
    
    <div class="thesis-cta">
        <div class="thesis-meta">
            <p>Name: </p>
            <p>Contest: </p>
            <p>Student-Composed Word Count: </p>
            <p>Process Paper Word Count: </p>
        </div>
    </div>
    """, unsafe_allow_html=True)
elif bg == "#ffffff":
    st.markdown("""
    <style>

    html {
        scroll-behavior: smooth
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

    /* ── Thesis link ── */
    .thesis-cta {
        text-align: center;
        margin: 3rem auto;
    }

    .thesis-cta a {
        font-size: 2rem;
        font-weight: bold;
        color: black;
        text-decoration: none;
        border-bottom: 3px solid black;
        padding-bottom: 4px;
    }

    .thesis-cta a:hover {
        opacity: 0.6;
    }

    /* ── Metadata block under thesis link ── */
    .thesis-meta {
        margin-top: 1.5rem;
        text-align: center;
    }

    .thesis-meta p {
        font-size: 2rem;
        font-weight: bold;
        color: black;
        padding-bottom: 4px;
        margin: 0.3rem 0;
    }

    /* ── Hide sidebar ── */
    [data-testid="stSidebar"] {
        display: none !important;
    }

    [data-testid="stSidebarCollapsedControl"] {
        display: none !important;
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="hero">
        <img src="{banner_url}">
        <div class="hero-text">
            <h1>Breaking the Loop:</h1>
            <p>How Radia Perlman Made the Modern Internet Possible</p>
        </div>
    </div>

    <div class="hero-caption">
        Image: Jalisco Campus Party, CC BY 2.0, via Wikimedia Commons
    </div>

    <div class="thesis-cta">
        <div class="thesis-meta">
            <p>Aarav Mehta</p>
            <p>Individual Website</p>
            <p>Middle School, Grade 7</p>
            <p>Student-Composed Word Count: 1199</p>
            <p>Process Paper Word Count: 435</p>
        </div>
</div>
    </div>
    """, unsafe_allow_html=True)
