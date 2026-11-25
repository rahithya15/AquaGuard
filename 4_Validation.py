import streamlit as st
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from aqua_utils import load_data, analyze_data
st.set_page_config(page_title="Validation", layout="wide")
st.title("📊 Prototype Validation")
reports, _ = load_data()
df, _ = analyze_data(reports)
actual = df.confirmed_case.astype(int)
predicted = (df.cluster != -1).astype(int)
a,b,c,d = st.columns(4)
a.metric("Accuracy", f"{accuracy_score(actual,predicted):.2%}")
b.metric("Precision", f"{precision_score(actual,predicted,zero_division=0):.2%}")
c.metric("Recall", f"{recall_score(actual,predicted,zero_division=0):.2%}")
d.metric("F1 score", f"{f1_score(actual,predicted,zero_division=0):.2%}")
st.write("Confusion matrix (rows = reference label, columns = model label)")
st.dataframe(confusion_matrix(actual, predicted), use_container_width=False)
st.warning("These metrics compare synthetic demo labels with a spatial-clustering flag. They are not evidence of real-world disease detection performance.")
