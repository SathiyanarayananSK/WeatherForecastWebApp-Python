import streamlit as st
import  plotly.express as px
import backend

# Add title, text input, slider, selectbox and subheader
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of forecast days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} in {place}")

if place:
    try:
        # Get temperature/ sky data
        filtered_data = backend.get_data(place, days)

        if option == "Temperature":
            temperatures = [dic["main"]["temp"]/10 for dic in filtered_data]
            dates = [dic["dt_txt"] for dic in filtered_data]

            # Create temperature plot
            figure = px.line(x=dates, y=temperatures, labels={"x":"Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)
        elif option =="Sky":
            sky_conditions = [dic["weather"][0]["main"] for dic in filtered_data]
            image_paths = []
            for condition in sky_conditions:
                image_paths.append(f"images/{condition.lower()}.png")
            st.image(image_paths, width=115)
    except KeyError:
        st.write("That place does not exist")