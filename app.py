
import streamlit as st
import pandas as pd
import sys
import subprocess
try:
    import plotly.express as px
except ImportError:
    print("Plotly not found. Installing...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "plotly"])
    import plotly.express as px
    
# DataFrame should be in memory, don't read from a file
df = pd.DataFrame({
    'Show': ['Show1', 'Show2', 'Show3', 'Show4'],
    'Network': ['Network A', 'Network B', 'Network A', 'Network C'],
    'Average Sentiment': [0.7, -0.2, 0.5, 0.9],
    'Median Sentiment': [0.6, -0.3, 0.4, 0.8]
})

# Streamlit UI
st.title("📺 TV Show Sentiment Dashboard")
st.write("This dashboard visualizes Reddit sentiment analysis for various TV shows.")

# Dropdown filter
selected_network = st.selectbox("Filter by Network:", ["All"] + df["Network"].unique().tolist())

# Filter data
if selected_network != "All":
    df = df[df["Network"] == selected_network]

# Display Data Table
st.subheader("📊 Sentiment Data Table")
st.dataframe(df)

# Create a bar chart for sentiment analysis
st.subheader("📈 Sentiment Analysis by Show")
fig = px.bar(df, x="Show", y=["Average Sentiment", "Median Sentiment"], 
             barmode="group", title="TV Show Sentiment Scores")
st.plotly_chart(fig)

# Show best & worst sentiment shows
st.subheader("🏆 Best & Worst Sentiment Shows")
best_show = df.loc[df["Average Sentiment"].idxmax()]
worst_show = df.loc[df["Average Sentiment"].idxmin()]

st.success(f"🔥 Most Positively Received: {best_show['Show']} ({best_show['Average Sentiment']:.2f})")
st.error(f"💀 Most Negatively Received: {worst_show['Show']} ({worst_show['Average Sentiment']:.2f})")
