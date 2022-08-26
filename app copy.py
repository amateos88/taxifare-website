from datetime import datetime
from xmlrpc.client import DateTime
import streamlit as st
import requests
import datetime


url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')


date = st.date_input(label='2013-07-06 17:18:00')
time = st.time_input(label= 'hours, mins, seconds') #.strftime("%H:%M:%S")
#date_time = DateTime
#date_time = .strftime("%Y/%m/%d %H:%M:%S")
pickup_lon = st.number_input('longitud')
pickup_lat = st.number_input('latitude')
drop_long = st.number_input('dropoff long')
drop_lat = st.number_input('drop off lat')
passengers = st.number_input('how many humans are coming?')

#st.write(data, time)

if st.button('AlienBalls'):
    params = {
            'pickup_datetime': str(date) + ' ' + str(time),
            'pickup_longitude': pickup_lon,
            'pickup_latitude' : pickup_lat,
            'dropoff_longitude' : drop_long,
            'dropoff_latitude' : drop_lat,
            'passenger_count' : int(passengers),
            }

    response = requests.get(url, params=params)

    st.write(f"your cost will be: {round(response.json()['fare'], 2)} kilos of gold")
