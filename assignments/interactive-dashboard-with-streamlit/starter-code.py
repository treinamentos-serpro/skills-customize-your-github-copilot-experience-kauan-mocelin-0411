from pathlib import Path

import pandas as pd
import streamlit as st

DATA_FILE = Path(__file__).parent / "data.csv"

st.set_page_config(page_title="School Clubs Dashboard", page_icon="📊")
st.title("School Clubs Dashboard")
st.write("Explore aggregated school club participation data.")

data = pd.read_csv(DATA_FILE)

# TODO: Add category and club filters in the sidebar.
# TODO: Show the filtered data, summary metrics, and charts.