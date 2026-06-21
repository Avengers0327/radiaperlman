import streamlit as st

banner_url = "https://upload.wikimedia.org/wikipedia/commons/7/71/Radia_Perlman_%2819995453218%29.jpg"

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
    font-size: 3rem;
    margin: 0;
    padding: 0;
    line-height: 1;
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

/* ── Two column sections ── */
.section {
    display: flex;
    align-items: center;
    padding: 4rem;
    gap: 3rem;
}

.section.reverse {
    flex-direction: row-reverse;
}

.section-img-wrap {
    width: 40%;
}

.section-img-wrap img {
    width: 100%;
    border-radius: 4px;
    object-fit: cover;
}

.section-img-wrap small {
    display: block;
    margin-top: 6px;
    font-size: 0.8rem;
    color: #999;
}

.section-text {
    width: 55%;
    font-size: 1.5rem;
    color: white;
    line-height: 1.7;
}

.section-text h2 {
    font-size: 1.9rem;
    margin-bottom: 1rem;
    color: white;
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
        <h1>Legacy</h1>
    </div>
</div>

<div class="hero-caption">
    Jalisco Campus Party, CC BY 2.0 <https://creativecommons.org/licenses/by/2.0>, via Wikimedia Commons
</div>

<div class="section">
    <div class="section-img-wrap">
        <img src="https://upload.wikimedia.org/wikipedia/commons/8/8b/Radia_Perlman_%282009%29.jpg">
        <small>Image: Scientist-100, CC0, via Wikimedia Commons</small>
    </div>
    <div class="section-text">
        <h2>A New Era of Networking</h2>
        <p>Before STP, every redundant link added to a network had to be manually managed to prevent loops, 
        making large-scale network design a constant balancing act. After STP was created, engineers could 
        add redundancy that was managed automatically by Perlman’s protocol. This allowed networks to grow at
        a previously unheard of scale, without the risk of broadcast storms.
</p>
    </div>
</div>

<div class="section reverse">
    <div class="section-img-wrap">
        <img src="https://upload.wikimedia.org/wikipedia/commons/5/5d/BalticServers_data_center.jpg">
        <small>Image: BalticServers.com, CC BY-SA 3.0, via Wikimedia Commons</small>
    </div>
    <div class="section-text">
        <h2A Protocol That Changed Everything</h2>
        <p>Today, STP remains a foundational standard in network engineering, running in ethernets across the globe. 
        As networks became more complex, STP was updated with versions such as RSTP and MSTP, but each evolution held
        the same core principles as the original. STP enabled reliable ethernet and LAN connections, which are the 
        core infrastructure of the modern internet. Without solving the looping problem that Perlman did, the modern 
        internet would not have been possible.</p>
    </div>
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