import streamlit as st
from aqua_utils import load_data, analyze_data
st.set_page_config(page_title="Data Explorer", layout="wide")
st.title("📋 Data Explorer")
reports, _ = load_data()
df, _ = analyze_data(reports)
clusters = ["All"] + sorted(df.cluster.unique().tolist())
choice = st.selectbox("Filter by DBSCAN cluster", clusters)
if choice != "All":
    df = df[df.cluster == choice]
st.dataframe(df, use_container_width=True)
st.download_button("Download filtered reports CSV", df.to_csv(index=False), "aquaguard_reports.csv", "text/csv")
