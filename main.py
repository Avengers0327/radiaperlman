import streamlit as st

st.set_page_config(layout="wide")

pg = st.navigation([
    st.Page("pages/home.py", title="Home", icon=None),
    st.Page("pages/thesis.py", title="Thesis", icon=None),
    st.Page("pages/early.py", title="The Early Internet", icon=None),
    st.Page("pages/looping.py", title="Infinite Looping", icon=None),
    st.Page("pages/stp.py", title="Spanning Tree Protocol", icon=None),
    st.Page("pages/legacy.py", title="Legacy", icon=None),
    st.Page("pages/interview.py", title="Interview", icon=None),
    st.Page("pages/written.py", title="Written Materials", icon=None),
], position="top")

pg.run()
