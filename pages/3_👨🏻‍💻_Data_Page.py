import streamlit as st
import pandas as pd
import numpy as np

data = {
    "Product": ["Product A", "Product B", "Product C", "Product D", "Product E"],
    "Region": ["North", "South", "East", "West", "Central"],
    "Q1 Sales": np.random.randint(50, 200, 5),
    "Q2 Sales": np.random.randint(50, 200, 5),
    "Q3 Sales": np.random.randint(50, 200, 5),
    "Q4 Sales": np.random.randint(50, 200, 5),
}

dataframe = pd.DataFrame(data)
st.dataframe(dataframe)