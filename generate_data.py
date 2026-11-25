import os
import numpy as np
import pandas as pd

os.makedirs("data", exist_ok=True)
rng = np.random.default_rng(42)
centers = [(30.9000, 75.8500), (30.9050, 75.8600), (30.8950, 75.8400)]
rows = []
for i in range(120):
    center = centers[i % len(centers)]
    rows.append({
        "report_id": f"R{i+1:03d}",
        "latitude": center[0] + rng.normal(0, 0.0015),
        "longitude": center[1] + rng.normal(0, 0.0015),
        "symptom": rng.choice(["Diarrhea", "Vomiting", "Fever", "Stomach pain"]),
        "report_date": str(pd.Timestamp("2026-10-01") + pd.Timedelta(days=int(rng.integers(0, 30)))),
        "confirmed_case": int(rng.integers(0, 2))
    })
for i in range(20):
    rows.append({
        "report_id": f"R{i+121:03d}",
        "latitude": 30.88 + rng.uniform(-0.02, 0.02),
        "longitude": 75.83 + rng.uniform(-0.02, 0.02),
        "symptom": rng.choice(["Diarrhea", "Vomiting", "Fever", "Stomach pain"]),
        "report_date": str(pd.Timestamp("2026-10-01") + pd.Timedelta(days=int(rng.integers(0, 30)))),
        "confirmed_case": int(rng.integers(0, 2))
    })
pd.DataFrame(rows).to_csv("data/symptom_reports.csv", index=False)
pd.DataFrame([
    {"source_id":"W1","source_name":"North Community Tap","latitude":30.901,"longitude":75.851},
    {"source_id":"W2","source_name":"Central Water Tank","latitude":30.906,"longitude":75.861},
    {"source_id":"W3","source_name":"South Public Well","latitude":30.894,"longitude":75.842},
    {"source_id":"W4","source_name":"East Supply Point","latitude":30.910,"longitude":75.875}
]).to_csv("data/water_sources.csv", index=False)
print("AquaGuard sample data created in the data folder.")
