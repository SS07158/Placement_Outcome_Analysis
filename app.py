import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sqlite3

st.title("Student Placements Analysis")
st.write("Interactive Analysis of Factors affecting Students Placements")

conn = sqlite3.connect("placements.db")
df = pd.read_sql("SELECT * FROM placements",conn)

st.write("Dataset preview")
st.dataframe(df.head())

st.sidebar.header("Filter Students")

min_gpa = st.sidebar.slider(
    "Minimum GPA",
    float(df['college_gpa'].min()),
    float(df['college_gpa'].max()),
    3.0
)

min_interships = st.sidebar.slider(
    "Minimum Interships",
    float(df['internships'].min()),
    float(df['internships'].max()),
    0.0
)

filtered_df = df[
    (df['college_gpa'] >= min_gpa) &
    (df['internships'] >= min_interships)
]

st.subheader("Filterd Results")
st.dataframe(filtered_df)

placement_rate = (
    filtered_df['placed'].sum() / len(filtered_df) * 100
    if len(filtered_df) > 0 else 0
 )

st.metric(
    label = "Placement Rate (%)",
    value=f"{placement_rate:.2f}"
)

st.subheader("Placement Distribution")

placement_counts = filtered_df['placed'].value_counts()

st.bar_chart(placement_counts)