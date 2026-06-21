# Radia Perlman & the Spanning Tree Protocol
### Lowell Milken Institute Discovery Award Submission

An interactive history research website exploring Radia Perlman's invention of the 
Spanning Tree Protocol (STP) in 1985 and its lasting impact on modern networking.

---

## Pages

- **Home** — Introduction and thesis statement
- **Thesis** — Full written thesis
- **The Early Internet** — ARPANET, packet switching, and early network architecture
- **Infinite Looping** — The broadcast storm problem and its consequences
- **Spanning Tree Protocol** — Perlman's solution and interactive STP simulation
- **Legacy** — STP's lasting impact on modern networking

---

## Running Locally

### Prerequisites
- Python 3.10+
- pip

### Installation

```bash
git clone https://github.com/yourusername/radia-perlman
cd radia-perlman
pip install -r requirements.txt
```

### Running

```bash
streamlit run main.py
```

Then open `http://localhost:8501` in your browser.

---

## Project Structure
main.py              # Entry point and navigation

pages/

home.py                Home page
thesis.py              Thesis page
early_internet.py      The Early Internet page
infinite_loop.py       Infinite Looping page
stp.py                 Spanning Tree Protocol page
legacy.py              Legacy page
cited.py               Works cited
---

## Dependencies
streamlit>=1.36.0

---

## Image Credits

All images sourced from Wikimedia Commons under Creative Commons licenses.
Full attributions displayed on each page.

---

## Research

Built for the Lowell Milken Institute Discovery Award.  
Subject: Radia Perlman and the invention of the Spanning Tree Protocol (1985).
