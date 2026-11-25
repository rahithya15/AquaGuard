AQUAGUARD - MULTI-PAGE STREAMLIT PROJECT

1. Open this folder in VS Code.
2. Create and activate a virtual environment:
   python -m venv venv
   .\venv\Scripts\Activate.ps1
3. Install libraries:
   python -m pip install -r requirements.txt
4. Generate demo data:
   python generate_data.py
5. Start the dashboard:
   python -m streamlit run app.py

Pages are available in the left sidebar:
- Home Dashboard
- Data Explorer
- DBSCAN Analysis
- Water Source Analysis
- Validation
- About Project

IMPORTANT:
The included dataset is synthetic demo data, not real patient or outbreak data.
DBSCAN clusters show spatial density only; they do not prove an outbreak or water contamination.
