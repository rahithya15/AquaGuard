import streamlit as st
from aqua_utils import load_data, analyze_data, nearest_source_distances
st.set_page_config(page_title="Water Source Analysis", layout="wide")
st.title("🚰 Water Source Analysis")
threshold = st.slider("Distance threshold (km)", 0.1, 5.0, 1.0, 0.1)
reports, sources = load_data()
df, _ = analyze_data(reports)
df = nearest_source_distances(df, sources)
df["Within selected distance"] = df.nearest_water_source_km <= threshold
st.metric("Reports within threshold", int(df["Within selected distance"].sum()))
st.dataframe(df[["report_id", "symptom", "nearest_water_source_km", "Within selected distance"]], use_container_width=True)
st.markdown("### Water sources")
st.dataframe(sources, use_container_width=True)
