import streamlit as st

banner_url = "https://upload.wikimedia.org/wikipedia/commons/e/e5/Network_switches.jpg"

st.markdown("""
<style>

[data-testid="stAppViewContainer"] { padding: 0 !important; }
section[data-testid="stMain"] { padding: 0 !important; }
[data-testid="stMainBlockContainer"] { max-width: 100% !important; padding: 0 !important; }
[data-testid="stMain"] > div { padding: 0 !important; }
[data-testid="block-container"] { padding: 0 !important; }

/* ── Hide sidebar ── */
[data-testid="stSidebar"] { display: none !important; }
[data-testid="stSidebarCollapsedControl"] { display: none !important; }

/* ── Hero ── */
.hero { position: relative; width: 100vw; height: 70vh; overflow: hidden; }
.hero img { width: 100%; height: 100%; object-fit: cover; filter: grayscale(100%) contrast(1.2) brightness(0.75); }
.hero-text { position: absolute; top: 50%; left: 0; right: 0; transform: translateY(-50%); color: white; text-align: center; }
.hero-text h1 { font-size: 3rem; margin: 0; padding: 0; line-height: 1; }
.hero-text p { font-size: 1.2rem; opacity: 0.85; margin: 0.5rem 0 0 0; padding: 0; }

/* ── Caption ── */
.hero-caption { text-align: left; font-size: 0.9rem; color: #666; margin-top: 8px; margin-bottom: 24px; padding-left: 1rem; }

/* ── Interview meta ── */
.interview-meta { padding: 2rem 8rem 2rem; color: white; font-size: 1rem; line-height: 1.6; }

/* ── Transcript ── */
.transcript { padding: 2rem 8rem 4rem 8rem; }

/* ── Each exchange ── */
.exchange { display: flex; gap: 1.5rem; margin-bottom: 1.5rem; align-items: flex-start; }

/* ── Speaker label ── */
.speaker { min-width: 120px; font-weight: bold; font-size: 0.95rem; padding-top: 2px; }
.speaker.aarav { color: #6eb5ff; }
.speaker.chris { color: #28c840; }

/* ── Dialogue ── */
.dialogue { font-size: 1.05rem; color: #ddd; line-height: 1.7; }

/* ── Timestamp ── */
.timestamp { font-size: 0.75rem; color: #555; margin-top: 2px; }

/* ── Video player ── */
[data-testid="stVideo"] {
    padding: 0 8rem;
    margin-bottom: 2rem;
}

[data-testid="stVideo"] video,
[data-testid="stVideo"] iframe {
    border-radius: 8px;
    width: 100% !important;
}

</style>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="hero">
    <img src="{banner_url}">
    <div class="hero-text">
        <h1>Expert Interview</h1>
        <p>Chris Grabosky, Solutions Architect Manager at MongoDB</p>
    </div>
</div>
<div class="hero-caption">
    Image: Jon 'ShakataGaNai' Davis, CC BY-SA 3.0, via Wikimedia Commons
</div>
<div class="interview-meta">
    <p><strong>Interviewee:</strong> Chris Grabosky, Solutions Architect Manager, MongoDB</p>
    <p><strong>Interviewer:</strong> Aarav Mehta</p>
    <p><strong>Date:</strong> June 2026</p>
    <p><strong>Format:</strong> Video call (Zoom)</p>
</div>
""", unsafe_allow_html=True)

VIDEO_URL = "https://youtu.be/AWBwfK8-jz4"
st.video(VIDEO_URL)
