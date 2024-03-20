import streamlit as st
import pandas as pd

# Load your cleaned dataset
df = pd.read_csv("data/sales_predictions_cleaned.csv")

# App title
st.title("Project 1: Sales Prediction Dashboard")

# Interactive Pandas dataframe
st.header("Interactive Dataframe")
st.dataframe(df)

# Descriptive Statistics
st.header("Descriptive Statistics")
if st.button("Show Descriptive Statistics"):
    st.write(df.describe())

# Dataset Information
st.header("Dataset Information")
if st.button("Show Dataset Info"):
    buffer = io.StringIO()
    df.info(buf=buffer)
    s = buffer.getvalue()
    st.text(s)

# Null Values Display
st.header("Null Values in the Dataset")
if st.button("Show Null Values"):
    st.write(df.isnull().sum())