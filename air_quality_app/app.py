import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression



st.title("Air Quality Forecasting App")
st.write("This is an innovation designed to forecast the future statistics and health impacts of air pollution through the use of a machine learning model.")

co2 = st.slider("Select CO2 level", 300, 500, 400)
st.write(f"CO2 level selected: {co2} ppm")

data = pd.DataFrame({"Year": [2020, 2021, 2022], "CO2": [380, 385, co2]})
st.line_chart(data.set_index("Year"))

df = pd.read_csv("data/air_quality.csv")

city = st.selectbox("Select a city", df["City or Locality"].unique())

city_data = df[df["City or Locality"] == city]

st.subheader("Historical PM2.5 Levels")
st.line_chart(city_data.set_index("Version of the database")["PM2.5 (μg/m3)"])


change = city_data["PM2.5 (μg/m3)"].iloc[-1] - city_data["PM2.5 (μg/m3)"].iloc[0]
trending = st.write("increasing" if change > 0 else "decreasing" if change < 0 else "stable")

st.line_chart(city_data.set_index("Version of the database")["PM10 (μg/m3)"])