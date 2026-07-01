import streamlit as st

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

.thesis {
    font-size: 1.5rem; 
    text-align: center;
    font-weight: bold;  
    color: var(--text-color);;
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
        <h1>Thesis</h1>
    </div>
</div>

<div class="hero-caption">
    Image: Jalisco Campus Party, CC BY 2.0 <https://creativecommons.org/licenses/by/2.0>, via Wikimedia Commons
</div>

<div class="thesis">
  <p>During the rise of the internet, data packets were looping endlessly between multi-device networks. 
  This actively hindered inter-device connectivity. Data looping caused network unreliability, crashing, 
  and other significant challenges, causing network scalability to be near impossible. In response to this 
  critical limitation, Radia Perlman introduced a protocol (the Spanning Tree Protocol, or STP) to eliminate 
  these loops, allowing networks to thrive and complex multidevice networks to form.
</p>
</div>
</div>

""", unsafe_allow_html=True)
