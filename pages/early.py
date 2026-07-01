import streamlit as st

banner_url = "https://upload.wikimedia.org/wikipedia/commons/8/8b/Arpanet_logical_map%2C_march_1977_PDP-10.png"

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

.section-img-wrap,
.stp-diagram,
.image-hover {
    width:40%;
    overflow:hidden;
    border-radius:4px;
}

.section-img-wrap img,
.stp-diagram img,
.datacenter-img{

    width:100%;
    display:block;
    border-radius:4px;

    object-fit:contain;

    transition:
        transform .25s ease,
        box-shadow .25s ease;
}

.section-img-wrap img:hover,
.stp-diagram img:hover,
.datacenter-img:hover{

    transform:scale(1.05);

    box-shadow:0 8px 20px rgba(0,0,0,.35);
}

.section-img-wrap small,

.stp-diagram small {
    display:block;
    margin-top:6px;
    font-size:.8rem;
    color:#999;
}

.section-text {
   width: 55%;
   font-size: 1.5rem;
   color: var(--text-color); 
   line-height: 1.7;
}


.section-text h2 {
   font-size: 1.9rem;
   margin-bottom: 1rem;
   color: var(--text-color); 
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
        <h1>The Early Internet</h1>
    </div>
</div>

<div class="hero-caption">
    Image: The Computer History Museum, CC0, via Wikimedia Commons
</div>

<div class="section">
    <div class="section-img-wrap">
        <img src="https://upload.wikimedia.org/wikipedia/commons/8/85/ARPANET_1970_Map.png">
        <small>Image: UCLA and BBN, CC BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0>, via Wikimedia Commons</small>
    </div>
    <div class="section-text">
        <h2>A New Kind of Network</h2>
        <p>The first major early network was the ARPANET, built to link computers in universities across 
          the United States in the late-1960s. This network started with only four computers in UCLA, UCSB, 
          Stanford University, and the University of  Utah, later being expanded nationwide. The network 
          connecting these universities was enabled through a technology known as “packet switching.” This 
          means that data is sent in multiple small chunks (packets), instead of one, large circuit stream 
          (a continuous data broadcast). The packets are reassembled at the receiving computer, to form a message. 
          However, unlike modern networks, the ARPANET was decentralized, meaning that no one computer controls the network. 
          This means that the network was highly efficient, as no single point of failure could bring down the entire network. 
          However, decentralization came with many flaws of its own.</p>
    </div>
</div>

<div class="section reverse">
    <div class="section-img-wrap">
        <img src="https://upload.wikimedia.org/wikipedia/commons/0/04/Interface_Message_Processor_Front_Panel.jpg">
        <small>Image: FastLizard4, CC BY-SA 3.0 <https://creativecommons.org/licenses/by-sa/3.0>, via Wikimedia Commonsl</small>
    </div>
    <div class="section-text">
        <h2>The Cracks Appear</h2>
        <p>This is because after the original message is broken into chunks, they are routed through
        early routers known as intermediate machines (IMPs). These IMPs did not have standardized paths
        for data to travel along, meaning that each packet could take its own route to the receiving
        computer. In smaller, simpler networks, this allows for higher reliability, as if one path is 
        blocked, the packets can take another. However, as networks scaled and more paths were added, 
        IMPs had no standardized way to direct packets, meaning packets could become misdirected and 
        start an infinite loop. These are called broadcast storms.</p>
    </div>
</div>

""", unsafe_allow_html=True)
