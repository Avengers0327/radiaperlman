import streamlit as st
import time

banner_url = "https://upload.wikimedia.org/wikipedia/commons/e/e5/Network_switches.jpg"
st.session_state["show_stp"] = False

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
    max-height: 500px;
    border-radius: 4px;
    object-fit: contain;
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

/* ── Simulate button ── */
div[data-testid="stButton"] > button {
    background-color: #28c840 !important;
    border-color: #28c840 !important;
    color: white !important;
}

div[data-testid="stButton"] > button:hover {
    background-color: #1fa832 !important;
    border-color: #1fa832 !important;
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
        <h1>Spanning Tree Protocol</h1>
    </div>
</div>

<div class="hero-caption">
    Image: Jon 'ShakataGaNai' Davis, CC BY-SA 3.0 <https://creativecommons.org/licenses/by-sa/3.0>, via Wikimedia Commons
</div>

<div class="section">
    <div class="section-img-wrap">
        <img src="https://upload.wikimedia.org/wikipedia/commons/2/2e/Spanning_tree_topology.png">
        <small>ReneOFD at German Wikipedia., CC BY-SA 3.0 <http://creativecommons.org/licenses/by-sa/3.0/>, via Wikimedia Commons</small>
    </div>
    <div class="section-text">
        <h2>Perlman's Solution</h2>
        <p>Radia Perlman recognized that the tradeoff between redundancy and stability should not exist. Perlman’s
        goal was to keep redundant paths in networks without causing loops. Her solution to this was the Spanning Tree 
        Protocol (STP). Rather than directly removing redundant paths, STP temporarily disables them. STP does this by 
        making the network structure into a “tree.” First, STP elects a “root” switch, to be the roots of the “spanning tree.”
        STP then examines all possible paths for packets to take, and chooses one safe, efficient path. After the path is 
        chosen, the others are blocked off. This prevents looping by making the paths a looped signal would take disabled.</p>
    </div>
</div>


""", unsafe_allow_html=True)

col_text, col_img = st.columns([55, 40])

with col_text:
    st.markdown("""
<div style="padding: 4rem; color: white; font-size: 1.5rem; line-height: 1.7;">
    <h2 style="font-size: 1.9rem; margin-bottom: 1rem; color: white;">STP in Action</h2>
    <p>This means that ethernet engineers no longer had the dilemma of redundancy vs. stability. STP opened the doors for 
    fault-tolerant Ethernet networks without the constant fear of broadcast storms. This made networks dramatically more 
    reliable, stable, and scalable. This reliability allowed Ethernet networks to scale at an unprecedented rate, paving the 
    way for enterprise LANs and the widespread deployment of large-scale networks 
</p>
</div>
""", unsafe_allow_html=True)

    b_left, b_mid, b_right = st.columns([1, 2, 1])
    with b_mid:
        if st.button("SIMULATE STP", type="primary", use_container_width=True):
            st.session_state["show_stp"] = True

    if st.session_state.get("show_stp"):
        msgs = [
            "$ Initializing network...",
            "$ Connecting to switch cluster...",
            "$ Establishing redundant links...",
            "$ Sending broadcast frame...",
            "$ Monitoring traffic...",
            "$ Detecting topology...",
        ]

        results = [
            "[INFO] Root bridge elected",
            "[INFO] Calculating spanning tree...",
            "[INFO] Selecting best paths",
            "[INFO] Blocking redundant ports",
            "[INFO] Loop-free topology established",
            "[INFO] Broadcast frame forwarded successfully",
            "[INFO] Backup links standing by",
            "[SUCCESS] Redundancy preserved",
            "[SUCCESS] Network stable",
            "[SUCCESS] Broadcast storm prevented",
        ]

        all_lines = [(msg, "white") for msg in msgs] + [(res, "#28c840") for res in results]
        lines_html = "".join(
            f'<div style="color:{color}; margin: 2px 0;">$ {line}</div>'
            for line, color in all_lines
        )
        st.markdown(f"""
<div style="margin: 0.5rem 4rem 1rem 4rem; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 20px rgba(0,0,0,0.6);">
  <div style="background: #3a3a3a; padding: 8px 12px; display: flex; align-items: center; gap: 6px;">
    <span style="width:12px;height:12px;border-radius:50%;background:#ff5f57;display:inline-block;"></span>
    <span style="width:12px;height:12px;border-radius:50%;background:#febc2e;display:inline-block;"></span>
    <span style="width:12px;height:12px;border-radius:50%;background:#28c840;display:inline-block;"></span>
    <span style="font-family:monospace;font-size:0.75rem;color:#aaa;margin-left:8px;">network-sim — bash</span>
  </div>
  <div style="background: #1a1a1a; padding: 16px 20px; font-family: 'Courier New', monospace; font-size: 0.95rem; line-height: 1.8; min-height: 420px;">
    {lines_html}
    <span style="color:#aaa;">▋</span>
  </div>
</div>
""", unsafe_allow_html=True)
        time.sleep(0.5)

with col_img:
    st.markdown("""
<div style="padding: 4rem 4rem 4rem 0; display: flex; flex-direction: column; height: 100%;">
    <img src="https://upload.wikimedia.org/wikipedia/commons/5/5d/BalticServers_data_center.jpg"
         style="width: 100%; flex: 1; object-fit: cover; border-radius: 4px; min-height: 900px;">
    <small style="display: block; margin-top: 6px; font-size: 0.8rem; color: #999;">
        Image: BalticServers.com, CC BY-SA 3.0, via Wikimedia Commons
    </small>
</div>
""", unsafe_allow_html=True)
