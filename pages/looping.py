import streamlit as st
import streamlit.components.v1 as components
import time

banner_url = "https://upload.wikimedia.org/wikipedia/commons/e/e5/Network_switches.jpg"
st.session_state["show_loop_errors"] = False

st.markdown("""
<style>

:root {
    scroll-behavior: smooth
    color: var(--text-color);
    padding-bottom: 4px;
}

/* ── Force full width & remove default padding ── */
[data-testid="stAppViewContainer"], 
[data-testid="stMain"], 
[data-testid="stMainBlockContainer"], 
[data-testid="stVerticalBlock"] {
    max-width: 100% !important;
    width: 100% !important;
    padding: 0 !important;
}

[data-testid="stMain"] > div {
    padding: 0 !important;
    max-width: 100% !important;
}

[data-testid="block-container"] {
    padding: 0 !important;
    max-width: 100% !important;
}

/* Force the component iframe to span full width */
iframe[title*="components.html"] {
    width: 100% !important;
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

 .section-img-wrap {
    width: 40%;
}

.section-img-wrap img {
    width: 100%;
    border-radius: 4px;
    object-fit: cover;
    transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out, background-color 0.2s ease-in-out;
}

.section-img-wrap img:hover {
    background-color: #47d7ac;
    color: var(--text-color); 
    transform: scale(1.05); 
    box-shadow: 0 4px 8px rgba(0,0,0,0.2);
}

.section-img-wrap small {
    display: block;
    margin-top: 6px;
    font-size: 0.8rem;
    color: #999;
}

.section-img-button img {
    width: 100%;
    border-radius: 4px;
    object-fit: cover;
    transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out, background-color 0.2s ease-in-out;
}

.section-img-button h2 {
    font-size: 1.9rem;
    margin-bottom: 1rem;
    color: var(--text-color); 
}

.section-img-button {
    padding: 4rem;
    color: var(--text-color); 
    font-size: 1.5rem;
    line-height: 1.7;
}

.section-img-button img:hover {
    background-color: #47d7ac;
    color: var(--text-color); 
    transform: scale(1.05); 
    box-shadow: 0 4px 8px rgba(0,0,0,0.2);
}

.broadcast-img {
    width: 100%;
    flex: 1;
    object-fit: cover;
    border-radius: 4px;
    min-height: 300px;
    transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
}

.broadcast-img:hover {
    transform: scale(1.05);
    box-shadow: 0 4px 8px rgba(0,0,0,0.2);
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

/* ── Bottom Padding ── */
.bottom-spacer {
    height: 8rem;
}

.animation {
    font-size: 1.9rem;
    margin-bottom: 1rem;
    color: white;
}

.animation-heading h1 {
    margin: 0;
    color: var(--text-color); 
}

.animation-heading {
    padding: 4rem 4rem 1rem;
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
        <div class="section-img-button">
            <h2>Chaos in the Network</h2>
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

    if st.session_state.show_loop_errors:

        terminal = st.empty()

        msgs = [
            "Initializing network...",
            "Connecting to switch cluster...",
            "Establishing redundant links...",
            "Sending broadcast frame...",
            "Monitoring traffic...",
            "Forwarding test frames...",
            "[INFO] Redundant topology detected",
            "[INFO] Learning MAC addresses...",
            "[WARNING] Duplicate frames detected",
            "[WARNING] Broadcast traffic exceeding threshold",
            "[ERROR] Switching loop detected",
            "[ERROR] MAC address table instability",
            "[ERROR] Broadcast storm in progress",
            "[CRITICAL] CPU utilization: 100%",
            "[CRITICAL] Packet loss: 94%",
            "[CRITICAL] Network unreachable"
        ]

        colors = (["white"] * 6) + (["#ff4444"] * 10)

        shown = []

        for line, color in zip(msgs, colors):
            shown.append(
                f'<div style="color:{color};margin:2px 0;">$ {line}</div>'
            )

            terminal.markdown(f"""
    <div style="margin:0.5rem 4rem;border-radius:8px;overflow:hidden;
    box-shadow:0 4px 20px rgba(0,0,0,.6);">

    <div style="background:#3a3a3a;padding:8px 12px;">
    <span style="width:12px;height:12px;border-radius:50%;background:#ff5f57;display:inline-block;"></span>
    <span style="width:12px;height:12px;border-radius:50%;background:#febc2e;display:inline-block;"></span>
    <span style="width:12px;height:12px;border-radius:50%;background:#ff4444;display:inline-block;"></span>
    <span style="font-family:'Courier New', monospace;color:#aaa;margin-left:8px;">
    network-sim — bash
    </span>
    </div>

    <div style="
    background:#181818;
    padding:18px;
    font-family:'Courier New', monospace;
    line-height:1.8;
    min-height:420px;
    ">
    {''.join(shown)}
    <span style="color:#aaa;">▋</span>
    </div>

    </div>
    """, unsafe_allow_html=True)

            time.sleep(0.45)

with col_img:
    st.markdown("""
<div style="padding: 4rem 4rem 4rem 0; display: flex; flex-direction: column; height: 100%;">
    <img src="https://upload.wikimedia.org/wikipedia/commons/a/ab/Broadcast_storm.png"
         class="broadcast-img"
         style="min-height: 850px; width: 100%; object-fit: contain; background: white; border-radius: 4px;">
    <small style="display: block; margin-top: 6px; font-size: 0.8rem; color: #999;">
        Image: FastLizard4, CC BY-SA 3.0, via Wikimedia Commons
    </small>
</div>
""", unsafe_allow_html=True)


def render_broadcast_storm():
    components.html("""
    <link href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@latest/dist/tabler-icons.min.css" rel="stylesheet">
    <style>
      /* Streamlit default font stack */
      :root {
        --font-sans: "Source Sans Pro", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        --font-mono: 'Courier New', monospace;
        --bg-dark: #0e1117;
        --text-primary: #ffffff;
        --text-secondary: #888888;
        --accent: #47d7ac;
        --danger: #ff4444;
        --success: #44cc66;
        --fill-danger: #ff4444;
      }
      body {
        background-color: transparent;
        font-family: var(--font-sans);
        margin: 0;
        padding: 0;
        box-sizing: border-box;
      }
      .sim-container {
        background-color: var(--bg-card);
        /* 4rem horizontal padding aligns with the rest of your site */
        padding: 3rem 4rem; 
        border-radius: 8px;
        color: var(--text-primary);
        width: 100%;
        box-sizing: border-box;
      }
      .btn {
        background-color: #2a2a2a;
        color: #ffffff;
        border: 1px solid var(--accent);
        padding: 10px 24px;
        border-radius: 4px;
        cursor: pointer;
        font-size: 15px;
        font-family: var(--font-sans);
        transition: all 0.2s ease-in-out;
        display: inline-flex;
        align-items: center;
        justify-content: center;
      }
      .btn:hover {
        background-color: var(--accent);
        color: #000000;
        transform: scale(1.02);
      }
      .stats-row {
        display: flex;
        justify-content: center;
        gap: 40px;
        margin-bottom: 1.5rem;
      }
      .stat-box {
        text-align: center;
      }
      .stat-label {
        font-size: 12px;
        color: var(--text-secondary);
        margin: 0 0 5px 0;
        text-transform: uppercase;
        letter-spacing: 1px;
        font-family: var(--font-sans);
      }
      .stat-value {
        font-size: 28px;
        font-weight: 500;
        margin: 0;
        color: #888888;
        font-family: var(--font-sans); /* Uses Streamlit font */
      }
      /* Exception: keep status monospace to distinguish it */
      #status-text { 
        font-family: var(--font-mono) !important; 
      }
      .svg-wrap {
        position: relative;
        background: #111111;
        border: 1px solid #333;
        border-radius: 6px;
        padding: 1rem;
        width: 100%;
        height: 550px; /* Fixed height prevents clipping */
        display: flex;
        align-items: center;
        justify-content: center;
        box-sizing: border-box;
      }
      /* SVG Elements */
      .c-gray rect {
        fill: #262626;
        stroke: #555555;
        stroke-width: 1.5;
      }
      .th { 
        fill: #ffffff; 
        font-size: 14px; 
        font-weight: 600; 
        font-family: var(--font-sans);
      }
      .ts { 
        fill: #888888; 
        font-size: 11px; 
        font-family: var(--font-sans);
      }
      line { 
        stroke: #555555 !important; 
        stroke-width: 2 !important; 
      }
      #caption-text { 
        fill: #666666; 
        font-size: 12px; 
        font-family: var(--font-sans); 
        font-style: italic;
      }
    </style>

    <div class="sim-container">
      <div style="text-align: center; margin-bottom: 1.5rem;">
        <button id="toggle-btn" class="btn">
          <i class="ti ti-player-play" aria-hidden="true" style="vertical-align: -2px; margin-right: 6px;"></i>Trigger broadcast storm
        </button>
      </div>

      <div class="stats-row">
        <div class="stat-box">
          <p class="stat-label">Frames in flight</p>
          <p class="stat-value" id="frame-count">0</p>
        </div>
        <div class="stat-box">
          <p class="stat-label">Network load</p>
          <p class="stat-value" id="cpu-load">0%</p>
        </div>
        <div class="stat-box">
          <p class="stat-label">Status</p>
          <p class="stat-value" style="color: var(--success);" id="status-text">Idle</p>
        </div>
      </div>

      <div id="shake-wrap" class="svg-wrap">
        <!-- preserveAspectRatio ensures the SVG scales correctly without clipping -->
        <svg width="100%" height="100%" viewBox="0 0 680 380" preserveAspectRatio="xMidYMid meet" role="img" id="storm-svg">
          <title>Broadcast storm simulation across a five-switch network</title>
          <desc>Five interconnected switches with redundant links. When triggered, broadcast frames multiply exponentially and loop endlessly, illustrating a network-wide broadcast storm and eventual outage.</desc>

          <line x1="120" y1="80" x2="340" y2="80" id="wire-1"/>
          <line x1="340" y1="80" x2="560" y2="80" id="wire-2"/>
          <line x1="120" y1="80" x2="120" y2="280" id="wire-3"/>
          <line x1="560" y1="80" x2="560" y2="280" id="wire-4"/>
          <line x1="120" y1="280" x2="340" y2="280" id="wire-5"/>
          <line x1="340" y1="280" x2="560" y2="280" id="wire-6"/>
          <line x1="340" y1="80" x2="340" y2="280" id="wire-7"/>

          <g class="c-gray"><rect x="80" y="50" width="80" height="60" rx="6"/><text x="120" y="76" text-anchor="middle" class="th">Switch A</text><text x="120" y="92" text-anchor="middle" class="ts">Core</text></g>
          <g class="c-gray"><rect x="300" y="50" width="80" height="60" rx="6"/><text x="340" y="76" text-anchor="middle" class="th">Switch B</text><text x="340" y="92" text-anchor="middle" class="ts">Core</text></g>
          <g class="c-gray"><rect x="520" y="50" width="80" height="60" rx="6"/><text x="560" y="76" text-anchor="middle" class="th">Switch C</text><text x="560" y="92" text-anchor="middle" class="ts">Core</text></g>
          <g class="c-gray"><rect x="80" y="250" width="80" height="60" rx="6"/><text x="120" y="276" text-anchor="middle" class="th">Switch D</text><text x="120" y="292" text-anchor="middle" class="ts">Access</text></g>
          <g class="c-gray"><rect x="300" y="250" width="80" height="60" rx="6"/><text x="340" y="276" text-anchor="middle" class="th">Switch E</text><text x="340" y="292" text-anchor="middle" class="ts">Access</text></g>
          <g class="c-gray"><rect x="520" y="250" width="80" height="60" rx="6"/><text x="560" y="276" text-anchor="middle" class="th">Switch F</text><text x="560" y="292" text-anchor="middle" class="ts">Access</text></g>

          <g id="packet-layer"></g>

          <text x="340" y="345" text-anchor="middle" class="ts" id="caption-text">A fully meshed network with no spanning tree — every loop is a path for frames to multiply</text>
        </svg>
      </div>
    </div>

    <script>
      let running = false;
      let crashed = false;
      let frameCount = 0;
      let animId = null;
      let spawnInterval = null;
      let escalateInterval = null;
      let spawnRate = 1;

      const btn = document.getElementById('toggle-btn');
      const countEl = document.getElementById('frame-count');
      const cpuEl = document.getElementById('cpu-load');
      const statusEl = document.getElementById('status-text');
      const layer = document.getElementById('packet-layer');
      const shakeWrap = document.getElementById('shake-wrap');
      const svgEl = document.getElementById('storm-svg');

      const links = [
        {x1:120,y1:80,x2:340,y2:80},
        {x1:340,y1:80,x2:560,y2:80},
        {x1:120,y1:80,x2:120,y2:280},
        {x1:560,y1:80,x2:560,y2:280},
        {x1:120,y1:280,x2:340,y2:280},
        {x1:340,y1:280,x2:560,y2:280},
        {x1:340,y1:80,x2:340,y2:280}
      ];

      const packets = [];

      function spawnPacket() {
        if (packets.length > 90) return;
        const link = links[Math.floor(Math.random() * links.length)];
        const forward = Math.random() > 0.5;
        const sx = forward ? link.x1 : link.x2;
        const sy = forward ? link.y1 : link.y2;
        const ex = forward ? link.x2 : link.x1;
        const ey = forward ? link.y2 : link.y1;
        const circle = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
        circle.setAttribute('cx', sx);
        circle.setAttribute('cy', sy);
        circle.setAttribute('r', 3.5);
        circle.setAttribute('fill', 'var(--fill-danger)');
        layer.appendChild(circle);
        packets.push({el: circle, sx, sy, ex, ey, t: 0, speed: 0.01 + Math.random() * 0.01});
      }

      function tick() {
        if (crashed) return;
        packets.forEach(p => {
          p.t += p.speed;
          if (p.t >= 1) {
            const link = links[Math.floor(Math.random() * links.length)];
            const forward = Math.random() > 0.5;
            p.sx = forward ? link.x1 : link.x2;
            p.sy = forward ? link.y1 : link.y2;
            p.ex = forward ? link.x2 : link.x1;
            p.ey = forward ? link.y2 : link.y1;
            p.t = 0;
          }
          const cx = p.sx + (p.ex - p.sx) * p.t;
          const cy = p.sy + (p.ey - p.sy) * p.t;
          p.el.setAttribute('cx', cx);
          p.el.setAttribute('cy', cy);
        });

        countEl.textContent = packets.length;
        const load = Math.min(100, Math.round(packets.length * 1.1));
        cpuEl.textContent = load + '%';
        cpuEl.style.color = load > 70 ? '#ff5555' : load > 30 ? '#ffaa33' : '#ffffff';

        if (load > 50 && load <= 90) {
          const shake = (load - 50) / 10;
          shakeWrap.style.transform = `translate(${(Math.random()-0.5)*shake}px, ${(Math.random()-0.5)*shake}px)`;
        }

        if (load >= 95 && !crashed) {
          triggerCrash();
        }

        if (!crashed) {
          animId = requestAnimationFrame(tick);
        }
      }

      function triggerCrash() {
        crashed = true;
        running = false;
        clearInterval(spawnInterval);
        clearInterval(escalateInterval);
        cancelAnimationFrame(animId);
        statusEl.textContent = 'Crashed';
        statusEl.style.color = '#ff5555';
        shakeWrap.style.transform = 'translate(0,0)';
        svgEl.style.opacity='0.25';
        svgEl.style.filter='grayscale(100%)';
        btn.style.display = 'none';

        // Break out of the iframe and inject the overlay into the main Streamlit page
        try {
          const parentDoc = window.parent.document;
          if (!parentDoc.getElementById('site-crash-overlay')) {
            const overlayHTML = `
            <style>
              #site-crash-overlay {
                position: fixed;
                top: 0; left: 0; width: 100vw; height: 100vh;
                background: rgba(10, 10, 10, 0.98);
                display: flex;
                align-items: center;
                justify-content: center;
                flex-direction: column;
                z-index: 99999;
                text-align: center;
                padding: 2rem;
                font-family: "Source Sans Pro", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
                color: #ffffff;
                backdrop-filter: blur(5px);
                box-sizing: border-box;
              }
              #site-crash-overlay .crash-icon { font-size: 4rem; color: #ff4444; margin-bottom: 2rem; animation: cpulse 1.5s infinite; }
              #site-crash-overlay .crash-title { font-size: 2.5rem; color: #ff4444; margin-bottom: 1.5rem; text-transform: uppercase; letter-spacing: 2px; text-shadow: 0 0 10px rgba(255, 68, 68, 0.5); }
              #site-crash-overlay .crash-text { font-size: 1.2rem; max-width: 600px; line-height: 1.6; margin-bottom: 2.5rem; color: #ddd; }

              /* Button styling matching the Streamlit primary button */
              #site-crash-overlay .reboot-btn {
                background-color: #28c840;
                color: #ffffff;
                border: 1px solid #28c840;
                padding: 0.6rem 1.5rem;
                border-radius: 8px;
                cursor: pointer;
                font-size: 1rem;
                font-weight: 400;
                font-family: "Source Sans Pro", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
                transition: all 0.2s ease-in-out;
                animation: cpulse 2s infinite;
                text-transform: uppercase;
                letter-spacing: 1px;
                box-shadow: none;
              }
              #site-crash-overlay .reboot-btn:hover {
                background-color: #1fa832;
                border: 1px solid #1fa832;
                color: #ffffff;
                transform: scale(1.02);
              }
              @keyframes cpulse { 0% { opacity: 1; transform: scale(1); } 50% { opacity: 0.7; transform: scale(0.98); } 100% { opacity: 1; transform: scale(1); } }
            </style>
            <div id="site-crash-overlay">
              <div class="crash-icon">⚠</div>
              <div class="crash-title">Network Crash Simulated</div>
              <div class="crash-text">
                The site crashed due to a broadcast storm, a common failure in early networked 
                systems. Click the button below to reboot the simulated network.
              </div>
              <button id="reboot-btn" class="reboot-btn">Reboot Network</button>
            </div>`;

            parentDoc.body.insertAdjacentHTML('beforeend', overlayHTML);

            // Listen for click on the reboot button to reset everything
            window.parent.crashReset = function(e) {
              const overlay = parentDoc.getElementById('site-crash-overlay');
              if (overlay) {
                overlay.remove();
                const rBtn = parentDoc.getElementById('reboot-btn');
                if (rBtn) rBtn.removeEventListener('click', window.parent.crashReset);
                reset(); // Call reset inside the iframe
              }
            };

            const rebootBtn = parentDoc.getElementById('reboot-btn');
            if (rebootBtn) {
              rebootBtn.addEventListener('click', window.parent.crashReset);
            }
          }
        } catch(e) {
          console.error("Cannot inject overlay into parent window", e);
        }
      }

      function reset() {
        layer.innerHTML='';
        packets.length=0;

        countEl.textContent = '0';
        cpuEl.textContent = '0%';
        cpuEl.style.color = 'var(--text-primary)';
        statusEl.textContent = 'Idle';
        statusEl.style.color = '#44cc66';
        svgEl.style.filter='';
        svgEl.style.opacity='1';
        shakeWrap.style.transform = 'translate(0,0)';
        btn.style.display = 'inline-flex';
        btn.innerHTML = '<i class="ti ti-player-play" aria-hidden="true" style="vertical-align:-2px;margin-right:4px;"></i>Trigger broadcast storm';
        crashed = false;
        running = false;
        spawnRate = 1;
      }

      btn.addEventListener('click', () => {
        running = !running;
        if (running) {
          btn.innerHTML = '<i class="ti ti-player-pause" aria-hidden="true" style="vertical-align:-2px;margin-right:4px;"></i>Stop storm';
          statusEl.textContent = 'Storming';
          statusEl.style.color = '#ff5555';
          spawnInterval = setInterval(() => { for(let i=0;i<spawnRate;i++) spawnPacket(); }, 80);
          escalateInterval = setInterval(() => { spawnRate = Math.min(spawnRate + 1, 6); }, 1000);
          tick();
        } else {
          clearInterval(spawnInterval);
          clearInterval(escalateInterval);
          cancelAnimationFrame(animId);
          reset();
        }
      });
    </script>
    """, height=800)  # Adjusted height for proper framing


st.space(50)

st.markdown("""
<div class="animation-heading">
    <h1>Broadcast Storm Emergence</h1>
</div>
""", unsafe_allow_html=True)

render_broadcast_storm()

# Add bottom spacer for padding
st.markdown('<div class="bottom-spacer"></div>', unsafe_allow_html=True)
