import streamlit as st
from aqua_utils import load_data, analyze_data
st.set_page_config(page_title="DBSCAN Analysis", layout="wide")
st.title("🧭 DBSCAN Analysis")
eps = st.slider("Neighbourhood radius (km)", 0.1, 2.0, 0.5, 0.1)
minimum = st.slider("Minimum reports to form a cluster", 2, 15, 5)
reports, _ = load_data()
df, summary = analyze_data(reports, eps, minimum)
a, b = st.columns(2)
a.metric("Clusters found", int(df[df.cluster != -1].cluster.nunique()))
b.metric("Unclustered reports", int((df.cluster == -1).sum()))
st.dataframe(summary, use_container_width=True)
st.bar_chart(summary.set_index("cluster")["report_count"] if not summary.empty else [])
st.caption("DBSCAN groups nearby coordinates. Results depend on the selected radius and minimum sample count.")
