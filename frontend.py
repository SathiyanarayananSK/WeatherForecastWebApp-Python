import streamlit as st
import plotly.express as px
import backend

# Set up the Streamlit app interface
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")  # Input field for the location
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of forecast days")  # Slider for forecast days
option = st.selectbox("Select data to view", ("Temperature", "Sky"))  # Dropdown to select data type
st.subheader(f"{option} for the next {days} in {place}")  # Display the selected option

if place:
    try:
        # Fetch weather data for the specified place and days
        filtered_data = backend.get_data(place, days)

        if option == "Temperature":
            # Extract temperature data and convert to Celsius
            temperatures = [dic["main"]["temp"] / 10 for dic in filtered_data]
            dates = [dic["dt_txt"] for dic in filtered_data]

            # Create a Plotly line chart for temperature trends
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)  # Display the chart in the app

        elif option == "Sky":
            # Extract sky conditions (e.g., Clear, Clouds, Rain)
            sky_conditions = [dic["weather"][0]["main"] for dic in filtered_data]
            image_paths = []
            for condition in sky_conditions:
                # Map sky conditions to corresponding image paths
                image_paths.append(f"images/{condition.lower()}.png")
            st.image(image_paths, width=115)  # Display sky condition images

    except KeyError:
        # Handle invalid location input
        st.write("That place does not exist")
