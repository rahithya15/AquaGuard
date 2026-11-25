import streamlit as st
import pandas as pd
from aqua_utils import load_data, analyze_data, make_map

st.set_page_config(page_title="AquaGuard", page_icon="💧", layout="wide")
st.title("💧 AquaGuard")
st.subheader("Spatial Detection of Potential Water-Borne Disease Clusters")
st.caption("Academic prototype using synthetic demonstration data. It is not a medical or public-health decision tool.")

reports, sources = load_data()
analyzed, summary = analyze_data(reports)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Symptom reports", len(analyzed))
c2.metric("Water sources", len(sources))
c3.metric("DBSCAN clusters", int(analyzed.loc[analyzed.cluster != -1, "cluster"].nunique()))
c4.metric("Noise / unclustered", int((analyzed.cluster == -1).sum()))

st.markdown("### Cluster overview")
st.dataframe(summary, use_container_width=True)
st.markdown("### Report locations")
st.components.v1.html(make_map(analyzed, sources), height=520, scrolling=False)
st.info("Use the pages in the left sidebar to explore reports, tune DBSCAN, inspect water sources, and view prototype validation.")
