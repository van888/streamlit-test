import time

import numpy as np
import pandas as pd
import plotly.figure_factory as ff
import pydeck as pdk
import requests

import streamlit as st
import streamlit.components.v1 as components

col1, col2 = st.columns(2)
col1.write("hello")
# @ DONE: TO RUN, AT TERMINAL, 'streamlit run file.py'
# @ DONE: INSTALLATION
# @ DONE: ST.WRITE HELLO WORLD
# @ DONE: CREATE BUTTON
col2.button("click me")
st.markdown("""___""")
some_dict = {"key": "value", "plug": "play"}

some_list = [1, 2, 3]
col1.write(some_dict)
col2.write(some_list)

# @ DONE: SOME_DICT AND SOME LIST

st.sidebar.write("NYCEM APPLICATIONS")
# @ DONE: CREATE SIDEBAR
components.html("""<hr style="height:10px;border:none;color:#333;background-color:#333;" /> """)

df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))
st.dataframe(df)  # Same as st.write(df)
# @ DONE: DISPLAY DATA FRAME
components.html("""<hr style="height:10px;border:none;color:#333;background-color:#333;" /> """)

st.image("https://www.cb14youthconference.nyc/wp-content/uploads/2019/02/nycem-logo-cut-out.png")
# @DONE DISPLAY IMAGE

# @DONE: ESRI MAP COMPONENT
esri_html = '<iframe width="700" height="400" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="https://arcgis.com/apps/View/index.html?appid=6b6a075eca8d4899958fb273710a6806"></iframe>'
# st.markdown(esri_html, unsafe_allow_html=True)
st.write(esri_html, unsafe_allow_html=True)


# @TODO: FORMS
def display_forms():

    # @DONE DISPLAY DROPDOWN TEXTBOX
    option = st.selectbox("How would you like to be contacted?", ("Email", "Home phone", "Mobile phone"))

    st.write("You selected:", option)

    # @DONE: INPUT BOX
    if option == "Email":
        contact = st.text_input("Email: ")
    elif option == "Home phone":
        contact = st.text_input("Home phone:")
    elif option == "Mobile phone":
        contact = st.text_input("Mobile phone")
    else:
        st.write("Error: Contact option not recognized")

    st.write(f"Your {option} contact is {contact} ")

    with st.form("my_form"):
        st.write("Inside the form")
        slider_val = st.slider("Form slider")
        checkbox_val = st.checkbox("Form checkbox")
        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write("slider", slider_val, "checkbox", checkbox_val)
    st.write("Form ended.")


app_selected = st.sidebar.selectbox(
    "choose an app: ", ("GIS Map", "Forms", "DPG", "Weather", "Grants and Funding", "progress bar")
)
# TODO: CREATE SAMPLE DASH
st.header(app_selected)


# @DONE: WEATHER APP SWITCHED FROM SIDEBAR
# lga
# latitude = 40.7769271
# longitude = -73.8761599
# office = 'OKX'
# "gridX":36
# "gridY":38

# central park
LATITUDE = 40.7769271
LONGITUDE = -73.9687078
office = "OKX"
# "gridX":33
# "gridY":37

station = f"https://api.weather.gov/gridpoints/{office}/{36},{38}/stations"
forecast = f"https://api.weather.gov/gridpoints/{office}/{36},{38}/forecast"
hourly = f"https://api.weather.gov/gridpoints/{office}/{36},{38}/forecast/hourly"
# r = requests.get(f'https://api.weather.gov/points/{LATITUDE},{LONGITUDE}')
r = requests.get(forecast)
weather = r.json()


def display_weather():
    for forecast in weather["properties"]["periods"]:
        st.image(forecast["icon"])
        st.write(forecast["name"], "\n", "temp: ", forecast["temperature"], "windSpeed: ", forecast["windSpeed"])
        st.write("Wind Direction: ", forecast["windDirection"], "Short Forecast: ", forecast["shortForecast"])


def display_metric():
    col1, col2, col3 = st.columns(3)
    col1.metric("Temperature", "70 °F", "1.2 °F")
    col2.metric("Wind", "9 mph", "-8%")
    col3.metric("Humidity", "86%", "4%")


# @DONE: SWITCH APP - CHARTS
def app_chart():
    x1 = np.random.randn(200) - 2
    x2 = np.random.randn(200)
    x3 = np.random.randn(200) + 2
    hist_data = [x1, x2, x3]
    group_labels = ["Group 1", "Group 2", "Group 3"]

    fig = ff.create_distplot(hist_data, group_labels, bin_size=[0.1, 0.25, 0.5])
    st.plotly_chart(fig, use_container_width=True)

    # st.write(forecast)


# st.write(weather)


# https://api.weather.gov/points/{latitude},{longitude}


# https://api.weather.gov/gridpoints/{office}/{grid X},{grid Y}/forecast

# https://www.google.com/maps/place/Central+Park/@40.7812199,-73.9687078,17z/data=!3m1!4b1!4m5!3m4!1s0x89c2589a018531e3:0xb9df1f7387a94119!8m2!3d40.7812199!4d-73.9665138

# central park https://www.google.com/maps/place/Central+Park+weather+observation+station/@40.7812199,-73.9687078,17z/data=!4m12!1m6!3m5!1s0x89c2589a018531e3:0xb9df1f7387a94119!2sCentral+Park!8m2!3d40.7812199!4d-73.9665138!3m4!1s0x89c259b0d661a77b:0x58f35d931f7793e9!8m2!3d40.7790352!4d-73.9692454
# lga https://www.google.com/maps/place/LaGuardia+Airport/@40.7769271,-73.8761599,17z/data=!3m2!4b1!5s0x89c25f894d83f791:0xad0170a7a5bb2630!4m5!3m4!1s0x89c25f8983424db5:0x772fc4660e9666b3!8m2!3d40.7769271!4d-73.8739659

# @DONE: GIS_MAP
def display_map():
    df = pd.DataFrame(np.random.randn(1000, 2) / [50, 50] + [LATITUDE, LONGITUDE], columns=["lat", "lon"])
    st.pydeck_chart(
        pdk.Deck(
            map_style="mapbox://styles/mapbox/light-v9",
            initial_view_state=pdk.ViewState(latitude=LATITUDE, longitude=LONGITUDE, zoom=11, pitch=50,),
            layers=[
                pdk.Layer(
                    "ScatterplotLayer",
                    data=df,
                    get_position="[lon, lat]",
                    get_color="[200, 30, 0, 160]",
                    get_radius=200,
                ),
            ],
        )
    )

    # pdk.Layer(
    #    'HexagonLayer',
    #    data=df,
    #    get_position='[lon, lat]',
    #    radius=200,
    #    elevation_scale=4,
    #    elevation_range=[0, 1000],
    #    pickable=True,
    #    extruded=True,
    # ),


def b_chart():
    chart_data = pd.DataFrame(np.random.randn(50, 3), columns=["a", "b", "c"])
    st.bar_chart(chart_data)


def l_chart():
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    st.line_chart(chart_data)


def progress_bar():
    my_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.05)
        my_bar.progress(percent_complete + 1)


def spinner():
    with st.spinner("Wait for it..."):
        time.sleep(1)
        st.success("Done!")


# TODO: CREATE COMPONENTS
# TODO: CONNECT MYSQL


if app_selected == "Weather":
    display_weather()
    st.markdown("""___""")
    display_metric()
if app_selected == "Grants and Funding":
    app_chart()
    b_chart()
    l_chart()
if app_selected == "GIS Map":
    display_map()
if app_selected == "progress bar":
    # st.balloons()
    # st.info('This is a purely informational message')
    progress_bar()
    st.markdown("""___""")
    spinner()
if app_selected == "Forms":
    display_forms()

