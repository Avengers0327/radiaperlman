import streamlit as st
import time

banner_url = "https://upload.wikimedia.org/wikipedia/commons/e/e5/Network_switches.jpg"
st.session_state["show_loop_errors"] = False

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
        <h1>Infinite Looping</h1>
    </div>
</div>

<div class="hero-caption">
    Image: Jon 'ShakataGaNai' Davis, CC BY-SA 3.0 <https://creativecommons.org/licenses/by-sa/3.0>, via Wikimedia Commons
</div>

<div class="section">
    <div class="section-img-wrap">
        <img src="https://upload.wikimedia.org/wikipedia/commons/5/5a/ARPANET_-_MILNT_Diagram_1984.jpg">
        <small>Defence Systems Agency, Public domain, via Wikimedia Commons</small>
    </div>
    <div class="section-text">
        <h2>An Interconnected World</h2>
        <p>As time passed, computer networks expanded beyond ARPANET, and Ethernet became more widely 
        adopted. This meant that accessibility to networks was easier, faster, and more interconnected, 
        but also meant that more devices would connect, increasing network complexity. To increase 
        reliability of important networks under high traffic, engineers added redundancies. Multiple 
        redundant links help to increase reliability as if one link fails, another can be used.</p>
    </div>
</div>


""", unsafe_allow_html=True)

col_text, col_img = st.columns([55, 40])

with col_text:
    st.markdown("""
<div style="padding: 4rem; color: white; font-size: 1.5rem; line-height: 1.7;">
    <h2 style="font-size: 1.9rem; margin-bottom: 1rem; color: white;">Chaos in the Network</h2>
    <p>However, this redundancy created broadcast storms and switching loops, which consist of data 
    spiraling endlessly in infinite loops. Since the data is looping, switches recognize the spiraling 
    data as legitimate traffic, and continue the loop. This means that the data is constantly sent in 
    a loop, until the network is overwhelmed. This has catastrophic consequences, such as network 
    slowdowns, crashes, and communication failures. These issues, at the time, were typically solved 
    by removing backup links. This meant that redundancy and stability could not coexist.</p>
</div>
""", unsafe_allow_html=True)

    b_left, b_mid, b_right = st.columns([1, 2, 1])
    with b_mid:
        if st.button("⚠ SIMULATE LOOP", type="primary", use_container_width=True):
            st.session_state["show_loop_errors"] = True

    if st.session_state.get("show_loop_errors"):
        msgs = [
            "$ Initializing network simulation...",
            "$ Connecting to switch cluster...",
            "$ Establishing redundant links...",
            "$ Sending broadcast frame...",
            "$ Monitoring traffic...",
            "$ Forwarding test frames...",
        ]

        errors = [
            "[INFO] Redundant topology detected",
            "[INFO] Learning MAC addresses...",
            "[WARNING] Duplicate frames detected",
            "[WARNING] Broadcast traffic exceeding threshold",
            "[ERROR] Switching loop detected",
            "[ERROR] MAC address table instability",
            "[ERROR] Broadcast storm in progress",
            "[CRITICAL] CPU utilization: 100%",
            "[CRITICAL] Packet loss: 94%",
            "[CRITICAL] Network unreachable",
        ]

        all_lines = [(msg, "white") for msg in msgs] + [(err, "#ff4444") for err in errors]
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
    <img src="https://upload.wikimedia.org/wikipedia/commons/a/ab/Broadcast_storm.png"
         style="width: 100%; flex: 1; object-fit: cover; border-radius: 4px; min-height: 300px;">
    <small style="display: block; margin-top: 6px; font-size: 0.8rem; color: #999;">
        Image: FastLizard4, CC BY-SA 3.0, via Wikimedia Commons
    </small>
</div>
""", unsafe_allow_html=True)
