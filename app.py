
import streamlit as st
import pandas as pd
import plotly.express as px

# Clear cache
# st.cache_data.clear()

# Load DataFrame from pickle
# df = pd.read_pickle("tv_show_sentiment.pk1")

# Streamlit UI
st.title("TV Show Sentiment Dashboard")
st.write("This dashboard visualizes Reddit sentiment analysis for various TV shows.")

# Dropdown filter
selected_network = st.selectbox("Filter by Network:", ["All"] + df["Network"].unique().tolist())

# Filter data
if selected_network != "All":
    df = df[df["Network"] == selected_network]

# Display Data Table
st.subheader("Sentiment Data Table")
st.dataframe(df)

# Create a bar chart for sentiment analysis
st.subheader("Sentiment Analysis by Show")
fig = px.bar(df, x="Show", y=["Average Sentiment", "Median Sentiment"], 
             barmode="group", title="TV Show Sentiment Scores")
st.plotly_chart(fig)

# Show best & worst sentiment shows
st.subheader("Best & Worst Sentiment Shows")
best_show = df.loc[df["Average Sentiment"].idxmax()]
worst_show = df.loc[df["Average Sentiment"].idxmin()]

st.success(f"Most Positively Received: {best_show['Show']} ({best_show['Average Sentiment']:.2f})")
st.error(f"Most Negatively Received: {worst_show['Show']} ({worst_show['Average Sentiment']:.2f})")
