import streamlit as st
from PIL import Image
import plotly.express as px
from backend import get_data

# Add title, text input, slider, selectbox and subheader
st.title("Weather forecast for the next days")
place = st.text_input("Place: ")
days = st.slider("Forecast days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

if place:
    # Get the temperature/sky data
    filtered_data = get_data(place, days)

    if option == 'Temperature':
        # Create a temperature plot
        temperatures = [dict['main']['temp'] for dict in filtered_data]
        dates = [dict['dt_txt'] for dict in filtered_data]
        figure = px.line(x=dates, y=temperatures, labels={'x': 'Date',
                                                          'y': 'Temperature, °C'})
        st.plotly_chart(figure)

    if option == 'Sky':
        sky_conds = [dict['weather'][0]['main'] for dict in filtered_data]

        images = {'Clear': 'D:/Non-uni-studying/Python/weather_forecast/images/clear.jpg',
                  'Clouds': 'D:/Non-uni-studying/Python/weather_forecast/images/cloud.jpg',
                  'Rain': 'D:/Non-uni-studying/Python/weather_forecast/images/rain.jpg',
                  'Snow': 'D:/Non-uni-studying/Python/weather_forecast/images/snow.jpg'}
        image_paths = [images[condition] for condition in sky_conds]

        st.image(image_paths, width=115)