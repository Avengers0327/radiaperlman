import streamlit as st
import streamlit.components.v1 as components
import time

banner_url = "https://upload.wikimedia.org/wikipedia/commons/e/e5/Network_switches.jpg"
st.session_state["show_stp"] = False

st.markdown("""
<style>

::root {
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
    border: none !important;
}

[data-testid="stMain"] > div {
    padding: 0 !important;
    max-width: 100% !important;
}

[data-testid="block-container"] {
    padding: 0 !important;
    max-width: 100% !important;
}

/* Remove the colored iframe lip */
iframe {
    border: none !important;
    box-shadow: none !important;
}

iframe[title*="components.html"] {
    width: 100% !important;
    border: none !important;
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
    max-height: 500px;
    border-radius: 4px;
    object-fit: contain;
}

.datacenter-img {
    width: 100%;
    object-fit: cover;
    border-radius: 4px;
    transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
    display: block;
}

.datacenter-img:hover {
    transform: scale(1.05);
    box-shadow: 0 4px 8px rgba(0,0,0,0.2);
}

.stp-diagram small {
    display: block;
    margin-top: 6px;
    font-size: 0.8rem;
    color: #999;
}

.stp-diagram {
    width: 40%;
}

.stp-diagram img {
    width: 100%;
    max-height: 500px;
    border-radius: 4px;
    object-fit: contain;
    background-color: #ffffff;
    transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
}

.stp-diagram small {
    display: block;
    margin-top: 6px;
    font-size: 0.8rem;
    color: #999;
}

.stp-diagram img:hover {
    transform: scale(1.05);
    box-shadow: 0 4px 12px rgba(0,0,0,.25);
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

/* ── Simulate button ── */
div[data-testid="stButton"] > button {
    background-color: #28c840 !important;
    border: 1px solid #28c840 !important;
    color: white !important;
    border-radius: 8px !important;
    padding: 0.5rem 1rem !important;
    font-weight: 400 !important;
    font-size: 0.875rem !important;
    line-height: 1.4 !important;
    transition: all 0.2s ease-in-out !important;
    box-shadow: none !important;
}

div[data-testid="stButton"] > button:hover {
    background-color: #1fa832 !important;
    border: 1px solid #1fa832 !important;
    color: white !important;
}

/* ── Hide sidebar ── */
[data-testid="stSidebar"] {
    display: none !important;
}

[data-testid="stSidebarCollapsedControl"] {
    display: none !important;
}

.storm-wrap {
    display: flex;
    width: 100%;
    gap: 0;
    align-items: stretch;
}

/* terminal + image share same height */
.storm-terminal {
    flex: 3;
}

.storm-image {
    flex: 2;
}

.storm-image img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
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

/* ── Closing Line Section ── */
.closing-section {
    padding: 2rem 4rem 6rem; /* Extra bottom padding */
    text-align: center;
    display: flex;
    justify-content: center;
}

.closing-line {
    font-size: 1.1rem;
    color: #888;
    line-height: 1.6;
    max-width: 1200px; /* Extended width */
    margin: 0 auto; /* Centers the block container itself */
    font-style: italic;
    padding-top: 2rem;
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
    <div class="stp-diagram image-hover">
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

col_text, col_img = st.columns(
    [3, 2],
    vertical_alignment="center"
)

with col_text:
    st.markdown("""
<div style="padding: 4rem; color: var(--text-color); font-size: 1.5rem; line-height: 1.7;">
    <h2 style="font-size: 1.9rem; margin-bottom: 1rem; color: var(--text-color);">STP in Action</h2>
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

    if st.session_state.show_stp:

        terminal = st.empty()

        msgs = [
            "Initializing network...",
            "Connecting to switch cluster...",
            "Establishing redundant links...",
            "Sending broadcast frame...",
            "Monitoring traffic...",
            "Detecting topology...",
            "Root bridge elected",
            "Calculating spanning tree...",
            "Selecting shortest paths",
            "Blocking redundant ports",
            "Loop-free topology established",
            "Broadcast frame forwarded",
            "Backup links standing by",
            "Redundancy preserved",
            "Network stable",
            "Broadcast storm prevented",
        ]

        colors = (
                ["white"] * 6 +
                ["#28c840"] * 10
        )

        shown = []

        for line, color in zip(msgs, colors):
            shown.append(
                f'<div style="color:{color};margin:2px 0;">$ {line}</div>'
            )

            terminal.markdown(f"""
                <div style="margin:0.5rem 4rem;border-radius:8px;overflow:hidden;
                box-shadow:0 4px 20px rgba(0,0,0,.6); border: none;">

                <div style="background:#3a3a3a;padding:8px 12px;">
                <span style="width:12px;height:12px;border-radius:50%;background:#ff5f57;display:inline-block;"></span>
                <span style="width:12px;height:12px;border-radius:50%;background:#febc2e;display:inline-block;"></span>
                <span style="width:12px;height:12px;border-radius:50%;background:#28c840;display:inline-block;"></span>
                <span style="font-family:monospace;color:#aaa;margin-left:8px;">
                network-sim — bash
                </span>
                </div>

                <div style="
                background:#181818;
                padding:18px;
                font-family:Courier New, monospace;
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
        <div class="image-hover">
        <img
            src="https://upload.wikimedia.org/wikipedia/commons/5/5d/BalticServers_data_center.jpg"
            class="datacenter-img"
            style="height:700px; object-fit:cover;">
        </div>

        <p style="font-size:.8rem;color:#999;margin-top:6px;">
        Image: BalticServers.com, CC BY-SA 3.0, via Wikimedia Commons
        </p>
""", unsafe_allow_html=True)


def render_stp_animation():
    components.html("""
    <link href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@latest/dist/tabler-icons.min.css" rel="stylesheet">
    <style>
      :root {
        --font-sans: "Source Sans Pro", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        --font-mono: 'Courier New', monospace;
        --bg-dark: #0e1117;
        --text-primary: #ffffff;
        --text-secondary: #888888;
        --accent: #28c840;
        --danger: #ff4444;
        --success: #28c840;
        --warning: #f39c12;
        --fill-danger: #ff4444;
        --fill-success: #28c840;
      }
      body {
        background-color: transparent;
        font-family: var(--font-sans);
        margin: 0;
        padding: 4rem 0;
        box-sizing: border-box;
        border: none !important;
      }
      .sim-container {
        background-color: var(--bg-card);
        padding: 3rem 4rem; 
        border-radius: 8px;
        color: var(--text-primary);
        width: 100%;
        box-sizing: border-box;
      }
      .btn {
        background-color: #28c840;
        color: #ffffff;
        border: 1px solid #28c840;
        padding: 0.5rem 1rem;
        border-radius: 8px;
        cursor: pointer;
        font-size: 0.875rem;
        font-weight: 400;
        font-family: var(--font-sans);
        line-height: 1.4;
        transition: all 0.2s ease-in-out;
        display: inline-flex;
        align-items: center;
        justify-content: center;
      }
      .btn:hover {
        background-color: #1fa832;
        color: #ffffff;
        border: 1px solid #1fa832;
      }
      .stats-row {
        display: flex;
        justify-content: center;
        gap: 40px;
        margin-bottom: 1.5rem;
      }
      .stat-box { text-align: center; }
      .stat-label {
        font-size: 12px;
        color: var(--text-secondary);
        margin: 0 0 5px 0;
        text-transform: uppercase;
        letter-spacing: 1px;
        font-family: var(--font-sans);
      }
      
      .stat-value {
        font-size: 24px;
        font-weight: 500;
        margin: 0;
        color: #888888;
        font-family: var(--font-sans);
      }
      #status-text { font-family: var(--font-mono) !important; }

      .svg-wrap {
        background: #111111;
        position: relative;
        border: 1px solid #333;
        border-radius: 6px;
        padding: 1rem;
        width: 100%;
        height: 550px; 
        display: flex;
        align-items: center;
        justify-content: center;
        box-sizing: border-box;
        box-shadow: none !important;
      }

      /* SVG Elements */
      .switch-grp {
        transition: transform 1.2s cubic-bezier(0.25, 0.8, 0.25, 1);
      }

      .c-gray rect {
        fill: #262626;
        stroke: #555555;
        stroke-width: 1.5;
        transition: stroke 0.5s ease, stroke-width 0.5s ease;
      }
      .c-gray rect.root {
        stroke: var(--accent);
        stroke-width: 3;
      }

      .th { fill: #ffffff; font-size: 14px; font-weight: 600; font-family: var(--font-sans); }
      .ts { fill: #888888; font-size: 11px; font-family: var(--font-sans); }

      .link {
        stroke: #444444;
        stroke-width: 2;
        transition: stroke 0.5s ease, stroke-width 0.5s ease, stroke-dasharray 0.5s ease, 
                    x1 1.2s cubic-bezier(0.25, 0.8, 0.25, 1), 
                    y1 1.2s cubic-bezier(0.25, 0.8, 0.25, 1), 
                    x2 1.2s cubic-bezier(0.25, 0.8, 0.25, 1), 
                    y2 1.2s cubic-bezier(0.25, 0.8, 0.25, 1);
      }
      .link.forwarding {
        stroke: var(--accent);
        stroke-width: 3;
      }
      .link.blocked {
        stroke: var(--warning);
        stroke-width: 2;
        stroke-dasharray: 6 4;
      }

      #caption-text { fill: #666666; font-size: 12px; font-family: var(--font-sans); font-style: italic; }

      .root-badge {
        opacity: 0;
        transition: opacity 0.5s ease;
      }
    </style>

    <div class="sim-container">
      <div style="text-align: center; margin-bottom: 1.5rem;">
        <button id="toggle-btn" class="btn">
          <i class="ti ti-bolt" aria-hidden="true" style="vertical-align: -2px; margin-right: 6px;"></i>Run STP Protocol
        </button>
      </div>

      <div class="stats-row">
        <div class="stat-box">
          <p class="stat-label">Root Bridge</p>
          <p class="stat-value" id="root-val" style="color: #888;">None</p>
        </div>
        <div class="stat-box">
          <p class="stat-label">Blocked Ports</p>
          <p class="stat-value" id="blocked-val">0</p>
        </div>
        <div class="stat-box">
          <p class="stat-label">Status</p>
          <p class="stat-value" style="color: var(--text-secondary);" id="status-text">Idle</p>
        </div>
      </div>

      <div id="shake-wrap" class="svg-wrap">
        <svg width="100%" height="100%" viewBox="0 0 680 380" preserveAspectRatio="xMidYMid meet" role="img" id="storm-svg">
          <title>Spanning Tree Protocol simulation</title>
          <desc>STP electing a root bridge, morphing into a tree, blocking redundant links, and allowing safe frame forwarding.</desc>

          <!-- Links -->
          <line x1="120" y1="80" x2="340" y2="80" class="link" id="wire-1"/>
          <line x1="340" y1="80" x2="560" y2="80" class="link" id="wire-2"/>
          <line x1="120" y1="80" x2="120" y2="280" class="link" id="wire-3"/>
          <line x1="560" y1="80" x2="560" y2="280" class="link" id="wire-4"/>
          <line x1="120" y1="280" x2="340" y2="280" class="link" id="wire-5"/>
          <line x1="340" y1="280" x2="560" y2="280" class="link" id="wire-6"/>
          <line x1="340" y1="80" x2="340" y2="280" class="link" id="wire-7"/>

          <g id="packet-layer"></g>

          <!-- Switches (Wrapped in transformable groups) -->
          <g class="switch-grp" id="sw-a" transform="translate(80, 50)">
            <g class="c-gray"><rect width="80" height="60" rx="6"/></g>
            <text x="40" y="26" text-anchor="middle" class="th">Switch A</text>
            <text x="40" y="42" text-anchor="middle" class="ts">Core</text>
            <g class="root-badge">
              <rect x="15" y="-18" width="50" height="15" rx="3" fill="#28c840"/>
              <text x="40" y="-7" text-anchor="middle" fill="#000" font-size="10" font-weight="bold" font-family="sans-serif">ROOT</text>
            </g>
          </g>

          <g class="switch-grp" id="sw-b" transform="translate(300, 50)">
            <g class="c-gray"><rect width="80" height="60" rx="6"/></g>
            <text x="40" y="26" text-anchor="middle" class="th">Switch B</text>
            <text x="40" y="42" text-anchor="middle" class="ts">Core</text>
          </g>

          <g class="switch-grp" id="sw-c" transform="translate(520, 50)">
            <g class="c-gray"><rect width="80" height="60" rx="6"/></g>
            <text x="40" y="26" text-anchor="middle" class="th">Switch C</text>
            <text x="40" y="42" text-anchor="middle" class="ts">Core</text>
          </g>

          <g class="switch-grp" id="sw-d" transform="translate(80, 250)">
            <g class="c-gray"><rect width="80" height="60" rx="6"/></g>
            <text x="40" y="26" text-anchor="middle" class="th">Switch D</text>
            <text x="40" y="42" text-anchor="middle" class="ts">Access</text>
          </g>

          <g class="switch-grp" id="sw-e" transform="translate(300, 250)">
            <g class="c-gray"><rect width="80" height="60" rx="6"/></g>
            <text x="40" y="26" text-anchor="middle" class="th">Switch E</text>
            <text x="40" y="42" text-anchor="middle" class="ts">Access</text>
          </g>

          <g class="switch-grp" id="sw-f" transform="translate(520, 250)">
            <g class="c-gray"><rect width="80" height="60" rx="6"/></g>
            <text x="40" y="26" text-anchor="middle" class="th">Switch F</text>
            <text x="40" y="42" text-anchor="middle" class="ts">Access</text>
          </g>

          <text x="340" y="345" text-anchor="middle" class="ts" id="caption-text">STP creates a loop-free logical topology while keeping physical redundancy</text>
        </svg>
      </div>
    </div>

    <script>
      let running = false;
      let animId = null;
      let spawnInterval = null;
      let phaseTimeouts = [];
      const packets = [];

      const btn = document.getElementById('toggle-btn');
      const rootVal = document.getElementById('root-val');
      const blockedVal = document.getElementById('blocked-val');
      const statusEl = document.getElementById('status-text');
      const layer = document.getElementById('packet-layer');

      // Tree topology definitions
      const forwardingLinks = ['wire-1', 'wire-2', 'wire-3', 'wire-4', 'wire-5'];
      const blockedLinks = ['wire-6', 'wire-7'];

      // Coordinates for packet spawning (Active tree only)
      const activePaths = [
        {x1:340, y1:70, x2:180, y2:170},  // A-B
        {x1:180, y1:170, x2:100, y2:280}, // B-C
        {x1:340, y1:70, x2:500, y2:170},  // A-D
        {x1:500, y1:170, x2:580, y2:280}, // D-E
        {x1:100, y1:280, x2:260, y2:280}  // C-F
      ];

      // Target tree coordinates for morphing
      const treeTransforms = {
        'sw-a': 'translate(300, 40)',
        'sw-b': 'translate(140, 140)',
        'sw-c': 'translate(60, 250)',
        'sw-d': 'translate(460, 140)',
        'sw-e': 'translate(540, 250)',
        'sw-f': 'translate(220, 250)'
      };

      const treeLineCoords = {
        'wire-1': {x1: 340, y1: 70, x2: 180, y2: 170},  // A-B
        'wire-2': {x1: 180, y1: 170, x2: 100, y2: 280}, // B-C
        'wire-3': {x1: 340, y1: 70, x2: 500, y2: 170},  // A-D
        'wire-4': {x1: 100, y1: 280, x2: 260, y2: 280}, // C-F
        'wire-5': {x1: 500, y1: 170, x2: 580, y2: 280}, // D-E
        'wire-6': {x1: 260, y1: 280, x2: 580, y2: 280}, // F-E (Blocked)
        'wire-7': {x1: 180, y1: 170, x2: 580, y2: 280}  // B-E (Blocked)
      };

      const initialTransforms = {
        'sw-a': 'translate(80, 50)',
        'sw-b': 'translate(300, 50)',
        'sw-c': 'translate(520, 50)',
        'sw-d': 'translate(80, 250)',
        'sw-e': 'translate(300, 250)',
        'sw-f': 'translate(520, 250)'
      };

      const initialLineCoords = {
        'wire-1': {x1: 120, y1: 80, x2: 340, y2: 80},
        'wire-2': {x1: 340, y1: 80, x2: 560, y2: 80},
        'wire-3': {x1: 120, y1: 80, x2: 120, y2: 280},
        'wire-4': {x1: 560, y1: 80, x2: 560, y2: 280},
        'wire-5': {x1: 120, y1: 280, x2: 340, y2: 280},
        'wire-6': {x1: 340, y1: 280, x2: 560, y2: 280},
        'wire-7': {x1: 340, y1: 80, x2: 340, y2: 280}
      };

      function clearTimeouts() {
        phaseTimeouts.forEach(t => clearTimeout(t));
        phaseTimeouts = [];
      }

      function reset() {
        running = false;
        clearInterval(spawnInterval);
        cancelAnimationFrame(animId);
        clearTimeouts();

        layer.innerHTML = '';
        packets.length = 0;

        rootVal.textContent = 'None';
        rootVal.style.color = '#888';
        blockedVal.textContent = '0';
        statusEl.textContent = 'Idle';
        statusEl.style.color = 'var(--text-secondary)';

        const badge = document.querySelector('.root-badge');
        if (badge) badge.style.opacity = '0';
        document.querySelector('#sw-a rect').classList.remove('root');

        // Revert Morph
        Object.keys(initialTransforms).forEach(id => {
          document.getElementById(id).setAttribute('transform', initialTransforms[id]);
        });
        Object.keys(initialLineCoords).forEach(id => {
          const el = document.getElementById(id);
          const c = initialLineCoords[id];
          el.setAttribute('x1', c.x1);
          el.setAttribute('y1', c.y1);
          el.setAttribute('x2', c.x2);
          el.setAttribute('y2', c.y2);
          el.classList.remove('forwarding', 'blocked');
        });

        btn.innerHTML = '<i class="ti ti-bolt" aria-hidden="true" style="vertical-align: -2px; margin-right: 6px;"></i>Run STP Protocol';
      }

      function spawnPacket() {
        if (packets.length > 15) return; // Keep traffic light
        const link = activePaths[Math.floor(Math.random() * activePaths.length)];
        const forward = Math.random() > 0.5;
        const sx = forward ? link.x1 : link.x2;
        const sy = forward ? link.y1 : link.y2;
        const ex = forward ? link.x2 : link.x1;
        const ey = forward ? link.y2 : link.y1;

        const circle = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
        circle.setAttribute('cx', sx);
        circle.setAttribute('cy', sy);
        circle.setAttribute('r', 3.5);
        circle.setAttribute('fill', 'var(--fill-success)');
        layer.appendChild(circle);
        packets.push({el: circle, sx, sy, ex, ey, t: 0, speed: 0.015});
      }

      function tick() {
        packets.forEach((p, index) => {
          p.t += p.speed;
          if (p.t >= 1) {
            p.el.remove();
            packets.splice(index, 1);
            return;
          }
          const cx = p.sx + (p.ex - p.sx) * p.t;
          const cy = p.sy + (p.ey - p.sy) * p.t;
          p.el.setAttribute('cx', cx);
          p.el.setAttribute('cy', cy);
        });

        if (running) {
          animId = requestAnimationFrame(tick);
        }
      }

      function startSTP() {
        reset(); // Ensure clean slate
        running = true;
        btn.innerHTML = '<i class="ti ti-refresh" aria-hidden="true" style="vertical-align: -2px; margin-right: 6px;"></i>Reset STP';

        // Phase 1: Elect Root Bridge
        statusEl.textContent = 'Electing Root...';
        statusEl.style.color = 'var(--warning)';
        phaseTimeouts.push(setTimeout(() => {
          const badge = document.querySelector('.root-badge');
          if (badge) badge.style.opacity = '1';
          document.querySelector('#sw-a rect').classList.add('root');
          rootVal.textContent = 'Switch A';
          rootVal.style.color = 'var(--accent)';
        }, 1500));

        // Phase 2: Morph into Tree
        phaseTimeouts.push(setTimeout(() => {
          statusEl.textContent = 'Calculating Tree';
          statusEl.style.color = 'var(--accent)';

          // Move Nodes
          Object.keys(treeTransforms).forEach(id => {
            document.getElementById(id).setAttribute('transform', treeTransforms[id]);
          });

          // Move Lines
          Object.keys(treeLineCoords).forEach(id => {
            const el = document.getElementById(id);
            const c = treeLineCoords[id];
            el.setAttribute('x1', c.x1);
            el.setAttribute('y1', c.y1);
            el.setAttribute('x2', c.x2);
            el.setAttribute('y2', c.y2);
          });
        }, 3000));

        // Phase 3: Block Redundant Ports
        phaseTimeouts.push(setTimeout(() => {
          statusEl.textContent = 'Blocking Ports';
          statusEl.style.color = 'var(--warning)';
          forwardingLinks.forEach(id => {
            document.getElementById(id).classList.add('forwarding');
          });
          blockedLinks.forEach(id => {
            document.getElementById(id).classList.add('blocked');
          });
          blockedVal.textContent = blockedLinks.length;
        }, 4800));

        // Phase 4: Loop-free Topology Active
        phaseTimeouts.push(setTimeout(() => {
          statusEl.textContent = 'Loop-Free';
          statusEl.style.color = 'var(--success)';
          // Start safe traffic forwarding
          spawnInterval = setInterval(spawnPacket, 600);
          tick();
        }, 6000));
      }

      btn.addEventListener('click', () => {
        if (running) {
          reset();
        } else {
          startSTP();
        }
      });
    </script>
    """, height=800)

st.space(50)

st.markdown("""
<div class="animation-heading">
    <h1 align = "center">STP Convergence Sequence</h1>
</div>
""", unsafe_allow_html=True)

render_stp_animation()

# Add a styled closing line section
st.markdown("""
<div class="closing-section">
    <p class="closing-line">
        Radia Perlman's Spanning Tree Protocol transformed Ethernet from a fragile shared medium into a robust, 
        self-healing architecture—forming the <strong>backbone of modern network infrastructure</strong>.
    </p>
</div>
""", unsafe_allow_html=True)
