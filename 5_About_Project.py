import streamlit as st
st.set_page_config(page_title="About AquaGuard", layout="wide")
st.title("ℹ️ About AquaGuard")
st.markdown("""
### Project objective
AquaGuard is an academic prototype that explores spatial clustering of geo-tagged symptom reports and their proximity to mapped water sources.

### Workflow
1. Load symptom reports and water-source coordinates.
2. Apply DBSCAN using the Haversine distance metric.
3. Identify dense groups and unclustered reports.
4. Calculate distance from each report to its nearest listed water source.
5. Display exploratory summaries for review.

### Technologies
Python, Streamlit, Pandas, NumPy, Scikit-learn and Folium.

### Responsible use
The included records are synthetic. Spatial clusters do not establish causation, diagnose people, or confirm contaminated water. Real use would require authorized, anonymized, dated data and independent public-health investigation.
""")
