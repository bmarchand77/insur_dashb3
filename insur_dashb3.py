# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 22:29:05 2024

@author: bened
"""

import streamlit as st
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
data = pd.read_csv("data/vehicle_insurance_claims.csv", parse_dates=["Policy_Start_Date", "Policy_End_Date", "Claim_Date", "Payment_Date"])

# Title for the dashboard layout sections
st.write("Developed by Benedict Marchand")
st.title("Vehicle Insurance Claims Dashboard")
st.sidebar.header("Filters")

# Start and End Date filter for Claims
start_date = st.sidebar.date_input("Start Date", data["Claim_Date"].min())
end_date = st.sidebar.date_input("End Date", data["Claim_Date"].max())
filtered_data = data[(data["Claim_Date"] >= pd.to_datetime(start_date)) & (data["Claim_Date"] <= pd.to_datetime(end_date))]

# Filter for Dimensions or Paratmeters to analyse on
vehicle_make_filter = st.sidebar.multiselect("Vehicle Make", options=filtered_data["Vehicle_Make"].unique())
coverage_type_filter = st.sidebar.multiselect("Coverage Type", options=filtered_data["Coverage_Type"].unique())
region_filter = st.sidebar.multiselect("Region", options=filtered_data["Region_Name"].unique())
agent_filter = st.sidebar.multiselect("Agent", options=filtered_data["Agent_ID"].unique())
claim_type_filter = st.sidebar.multiselect("Claim Type", options=filtered_data["Claim_Type"].unique())
claim_status_filter = st.sidebar.multiselect("Claim Status", options=filtered_data["Claim_Status"].unique())

# Apply filters to data
if vehicle_make_filter:
    filtered_data = filtered_data[filtered_data["Vehicle_Make"].isin(vehicle_make_filter)]
if coverage_type_filter:
    filtered_data = filtered_data[filtered_data["Coverage_Type"].isin(coverage_type_filter)]
if region_filter:
    filtered_data = filtered_data[filtered_data["Region_Name"].isin(region_filter)]
if agent_filter:
    filtered_data = filtered_data[filtered_data["Agent_ID"].isin(agent_filter)]
if claim_type_filter:
    filtered_data = filtered_data[filtered_data["Claim_Type"].isin(claim_type_filter)]
if claim_status_filter:
    filtered_data = filtered_data[filtered_data["Claim_Status"].isin(claim_status_filter)]    

# Display the filtered datasets
st.write(f"Displaying {len(filtered_data)} records")
st.dataframe(filtered_data)

# Segments of Dashboard for Graphs
# Graphs will be place side by side  in columns for easier reference
st.header("Claims Trends")

# Segment 1: Time and Vehicle Trends
st.subheader("1. Time and Vehicle Trends")
col1, col2 = st.columns(2)

# Line Chart: Claims Over Time
with col1:
    st.subheader("Claims Over Time")
    filtered_data["Claim_Month"] = filtered_data["Claim_Date"].dt.to_period("M")
    claims_over_time = filtered_data.groupby("Claim_Month").size()
    fig, ax = plt.subplots()
    claims_over_time.plot(kind="line", ax=ax, marker='o', color="tab:blue")
    ax.set_ylabel("Number of Claims")
    ax.set_xlabel("Month")
    plt.xticks(rotation=45)
    st.pyplot(fig)

# Bar Chart: Claims by Vehicle Make
with col2:
    st.subheader("Claims by Vehicle Make")
    fig, ax = plt.subplots()
    sns.countplot(data=filtered_data, x="Vehicle_Make", order=filtered_data["Vehicle_Make"].value_counts().index, ax=ax, palette="viridis")
    plt.xticks(rotation=45)
    st.pyplot(fig)

# Segment 2: Coverage and Region Trends
st.subheader("2. Coverage and Region Trends")
col1, col2 = st.columns(2)

# Bar Chart: Claims by Coverage Type
with col1:
    st.subheader("Claims by Coverage Type")
    fig, ax = plt.subplots()
    sns.countplot(data=filtered_data, x="Coverage_Type", order=filtered_data["Coverage_Type"].value_counts().index, ax=ax, palette="plasma")
    plt.xticks(rotation=45)
    st.pyplot(fig)

# Pie Chart: Claims by Region
with col2:
    st.subheader("Claims by Region")
    region_counts = filtered_data["Region_Name"].value_counts()
    fig, ax = plt.subplots()
    ax.pie(region_counts, labels=region_counts.index, autopct="%1.1f%%", startangle=90, colors=sns.color_palette("Set2", len(region_counts)))
    ax.axis("equal")
    st.pyplot(fig)

# Segment 3: Agent and Deductible Trends
st.subheader("3. Agent and Deductible Trends")
col1, col2 = st.columns(2)

# Bar Chart: Claims by Agent
with col1:
    st.subheader("Claims by Agent")
    top_agents = filtered_data["Agent_ID"].value_counts().head(10)  # Show only top 10 agents
    fig, ax = plt.subplots()
    sns.barplot(y=top_agents.index, x=top_agents.values, palette="coolwarm", ax=ax)
    ax.set_xlabel("Number of Claims")
    ax.set_ylabel("Agent ID")
    st.pyplot(fig)

# Scatter Plot: Claim Amount vs Deductible
with col2:
    st.subheader("Claim Amount vs Deductible")
    fig, ax = plt.subplots()
    sns.scatterplot(data=filtered_data, x="Deductible", y="Claim_Amount", hue="Coverage_Type", style="Claim_Status", palette="tab10", ax=ax)
    ax.set_xlabel("Deductible Amount")
    ax.set_ylabel("Claim Amount")
    st.pyplot(fig)

# Segment 4: Claim Type Trends
st.subheader("4. Claim Type Trends")
col1, col2 = st.columns(2)

# Pie Chart: Claims by Claim Type
with col1:
    st.subheader("Claims by Claim Type")
    claim_type_counts = filtered_data["Claim_Type"].value_counts()
    fig, ax = plt.subplots()
    ax.pie(claim_type_counts, labels=claim_type_counts.index, autopct="%1.1f%%", startangle=90, colors=sns.color_palette("Set3", len(claim_type_counts)))
    ax.axis("equal")
    st.pyplot(fig)

# Additional Insights: Claims Amount by Claim Type
with col2:
    st.subheader("Average Claim Amount by Claim Type")
    avg_claim_amount = filtered_data.groupby("Claim_Type")["Claim_Amount"].mean().sort_values()
    fig, ax = plt.subplots()
    avg_claim_amount.plot(kind="barh", color="coral", ax=ax)
    ax.set_xlabel("Average Claim Amount")
    ax.set_ylabel("Claim Type")
    st.pyplot(fig)
