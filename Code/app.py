import streamlit as st
import pandas as pd
import plotly.express as px

# App title
st.set_page_config(page_title="Casualties Daily Data Analysis", layout="wide")
st.title(" Casualties Daily Data Analysis")

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("casualties_daily.csv")

df = load_data()

# Show data preview
st.subheader("Data Preview")
st.dataframe(df.head())

# Sidebar filters
st.sidebar.header("Filter Data")
columns = df.columns.tolist()

# Choose X-axis and Y-axis
x_axis = st.sidebar.selectbox("X-axis", columns, index=0)
y_axis = st.sidebar.selectbox("Y-axis", columns, index=1)

# Plot type
plot_type = st.sidebar.selectbox("Plot Type", ["Line", "Bar", "Scatter"])

# Create plot
st.subheader(f"{plot_type} Plot of {y_axis} vs {x_axis}")
if plot_type == "Line":
    fig = px.line(df, x=x_axis, y=y_axis, title=f"{y_axis} over {x_axis}")
elif plot_type == "Bar":
    fig = px.bar(df, x=x_axis, y=y_axis, title=f"{y_axis} by {x_axis}")
elif plot_type == "Scatter":
    fig = px.scatter(df, x=x_axis, y=y_axis, title=f"{y_axis} vs {x_axis}")

fig.update_layout(hovermode="x unified")
st.plotly_chart(fig, use_container_width=True)

# Summary statistics
st.subheader("Summary Statistics")
st.write(df.describe())

# Download filtered data
st.download_button(
    label="Download Data as CSV",
    data=df.to_csv(index=False).encode("utf-8"),
    file_name="filtered_data.csv",
    mime="text/csv",
)

