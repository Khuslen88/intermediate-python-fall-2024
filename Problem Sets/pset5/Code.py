import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

import streamlit as st
import plotly.express as px

# Title
st.title("Data Visualization App")

# Text inputs
values = st.text_input("Enter values separated by commas:", "10, 20, 30")

#Chart types
chart_type = st.selectbox("Select chart type:", ["Bar Chart", "Line Chart", "Pie Chart"])

# Processing inputs
try:
    data = list(map(int, values.split(",")))
except ValueError:
    st.error("Please enter valid numbers separated by commas.")
    data = []

# Plotting the data
if st.button("Generate Chart") and data:
    if chart_type == "Bar Chart":
        fig = px.bar(
            x=list(range(len(data))),
            y=data,
            labels={"x": "Index", "y": "Value"},
            title=f"Bar Chart for {values} Data"
        )

    elif chart_type == "Line Chart":
        fig = px.line(
            x=list(range(len(data))),
            y=data,
            labels={"x": "Index", "y": "Value"},
            title=f"Line Chart for {values} Data"
        )

    elif chart_type == "Pie Chart":
        fig = px.pie(
            names=[f"Item {i}" for i in range(len(data))],
            values=data,
            title=f"Pie Chart for {values} Data"
        )

    st.plotly_chart(fig)