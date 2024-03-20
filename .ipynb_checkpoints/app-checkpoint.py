import streamlit as st
import pandas as pd
from io import StringIO
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load your cleaned dataset
df = pd.read_csv("data/sales_predictions_cleaned.csv")

# App title
st.title("Sales Prediction Dashboard")

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
    buffer = StringIO()
    df.info(buf=buffer)
    s = buffer.getvalue()
    st.text(s)

# Null Values Display
st.header("Null Values in the Dataset")
if st.button("Show Null Values"):
    st.write(df.isnull().sum())

# Exploring individual columns
st.header("Explore Column Plots")
selected_column = st.selectbox("Select a column to explore", df.columns)

# Display appropriate plots for the selected column
if df[selected_column].dtype == 'object':
    # For categorical data, display a count plot
    fig = px.bar(df[selected_column].value_counts())
    st.plotly_chart(fig)
else:
    # For numerical data, display a histogram
    fig = px.histogram(df, x=selected_column)
    st.plotly_chart(fig)

# Feature vs Target Plots
st.header("Feature vs Target Plots")
feature_list = df.columns.drop('Item_Outlet_Sales')  # Assuming 'Item_Outlet_Sales' is the target
selected_feature = st.selectbox("Select a feature to explore against the target", feature_list)

# Display the appropriate plot of the feature versus the target
if df[selected_feature].dtype == 'object':
    # For categorical data, use a box plot
    fig = px.box(df, x=selected_feature, y="Item_Outlet_Sales")
    st.plotly_chart(fig)
else:
    # For numerical data, use a scatter plot with a custom color for the trendline
    fig = px.scatter(df, x=selected_feature, y="Item_Outlet_Sales", trendline="ols",
                     trendline_color_override='red')  # Change 'red' to any color you prefer
    st.plotly_chart(fig)