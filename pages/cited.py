import streamlit as st

banner_url = "https://upload.wikimedia.org/wikipedia/commons/e/e8/Radia_Perlman_%2820175426302%29.jpg"

st.markdown("""
<style>

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

.citations {
    font-size: 1.5rem; 
    text-align: left;
    font-weight: bold;  
    color: white;
    padding: 4rem 8rem; 
    line-height: 1.7; 
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
        <h1>Works Cited</h1>
    </div>
</div>

<div class="hero-caption">
    Image: Jalisco Campus Party, CC BY 2.0 <https://creativecommons.org/licenses/by/2.0>, via Wikimedia Commons
</div>

<div class="citations">
    <p>Henn, S. (2014, October 21). When women stopped coding. NPR. https://www.npr.org/sections/money/2014/10/21/357629765/when-women-stopped-coding</p>
    <p>Radia Perlman | Lemelson. (n.d.). https://lemelson.mit.edu/resources/radia-perlman</p>
    <p>Rosen, R. J. (2014, March 5). Radia Perlman: Don't call me the mother of the internet. The Atlantic. https://www.theatlantic.com/technology/archive/2014/03/radia-perlman-dont-call-me-the-mother-of-the-internet/284146/</p>
    <p>Schwab, K. (2021, March 18). How tech pioneer Radia Perlman overcame bias to invent a core component of the internet. Fast Company. https://www.fastcompany.com/90615239/radia-perlman-internet-pioneer-gender-bias</p>
    <p>What is the purpose of the Spanning Tree Protocol (STP)? (2026, March 4). Omnitron Systems. https://www.omnitron-systems.com/blog/what-is-the-purpose-of-the-spanning-tree-protocol-stp</p>
</div>

<div style="
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    z-index: 9999;
    background: rgba(0,0,0,0.6);
    backdrop-filter: blur(8px);
    display: flex;
    justify-content: center;
    gap: 3rem;
    padding: 1rem 2rem;
">
    <a href="/Home" style="color:white; text-decoration:none; font-size:1rem; font-weight:600; opacity:0.85;">Home</a>
    <a href="/Thesis" style="color:white; text-decoration:none; font-size:1rem; font-weight:600; opacity:0.85;">Thesis</a>
    <a href="/The_Early_Internet" style="color:white; text-decoration:none; font-size:1rem; font-weight:600; opacity:0.85;">The Early Internet</a>
    <a href="/Infinite_Looping" style="color:white; text-decoration:none; font-size:1rem; font-weight:600; opacity:0.85;">Infinite Looping</a>
    <a href="/Spanning_Tree_Protocol" style="color:white; text-decoration:none; font-size:1rem; font-weight:600; opacity:0.85;">STP</a>
    <a href="/Legacy" style="color:white; text-decoration:none; font-size:1rem; font-weight:600; opacity:0.85;">Legacy</a>
</div>

""", unsafe_allow_html=True)
