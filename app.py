import pandas as pd
import streamlit
import plotly.express as px 


vehicles_us = pd.read_csv("vehicles_us.csv")

vehicles_us.info()

print(vehicles_us.isna().sum())
