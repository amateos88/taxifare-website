from datetime import datetime
from xmlrpc.client import DateTime
import streamlit as st
import requests
import datetime

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...


3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''

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
