import streamlit as st
import pandas as pd
import numpy as np

# Scatter Plot
st.header('Scatter Plot on Map')

data = pd.DataFrame(
    np.random.randn(100, 2) / [100, 100] + [40.7128, -74.0060],
    columns=['lat', 'lon']
)

st.map(data)

# Area Chart
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["Stock A", "Stock B", "Stock C"])

st.header("Area Chart")
st.area_chart(chart_data)