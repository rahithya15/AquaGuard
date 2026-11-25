import os
import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
import folium
from folium.plugins import MarkerCluster

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")

def load_data():
    reports_path = os.path.join(DATA_DIR, "symptom_reports.csv")
    sources_path = os.path.join(DATA_DIR, "water_sources.csv")
    if not os.path.exists(reports_path) or not os.path.exists(sources_path):
        raise FileNotFoundError("Data files are missing. Run: python generate_data.py")
    return pd.read_csv(reports_path), pd.read_csv(sources_path)

def analyze_data(reports, eps_km=0.5, min_samples=5):
    df = reports.copy()
    coords = np.radians(df[["latitude", "longitude"]].astype(float).to_numpy())
    model = DBSCAN(eps=eps_km / 6371.0088, min_samples=min_samples, metric="haversine")
    df["cluster"] = model.fit_predict(coords)
    clustered = df[df.cluster != -1]
    summary = (clustered.groupby("cluster")
               .agg(report_count=("report_id", "count"),
                    avg_latitude=("latitude", "mean"),
                    avg_longitude=("longitude", "mean"))
               .reset_index())
    return df, summary

def make_map(reports, sources):
    center = [reports.latitude.mean(), reports.longitude.mean()]
    m = folium.Map(location=center, zoom_start=12)
    group = MarkerCluster().add_to(m)
    for _, r in reports.iterrows():
        color = "gray" if int(r.cluster) == -1 else "red"
        folium.CircleMarker(
            [r.latitude, r.longitude], radius=5, color=color, fill=True,
            popup=f"Report: {r.report_id}<br>Cluster: {r.cluster}"
        ).add_to(group)
    for _, s in sources.iterrows():
        folium.Marker(
            [s.latitude, s.longitude], tooltip=str(s.source_name),
            icon=folium.Icon(color="blue", icon="tint", prefix="fa")
        ).add_to(m)
    return m.get_root().render()

def nearest_source_distances(reports, sources):
    result = reports.copy()
    distances = []
    for _, r in result.iterrows():
        lat1, lon1 = np.radians([r.latitude, r.longitude])
        lat2 = np.radians(sources.latitude.to_numpy(dtype=float))
        lon2 = np.radians(sources.longitude.to_numpy(dtype=float))
        a = np.sin((lat2-lat1)/2)**2 + np.cos(lat1)*np.cos(lat2)*np.sin((lon2-lon1)/2)**2
        d = 6371.0088 * 2 * np.arcsin(np.sqrt(a))
        distances.append(float(np.min(d)))
    result["nearest_water_source_km"] = distances
    return result
