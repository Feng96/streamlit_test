import streamlit as st
import pandas as pd
import numpy as np

st.title("Hello World")

st.write("Here's our first attempt at using data to create a table:")

st.text("This is some text.")

st.markdown("This is some markdown.")

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/')
#DATA_URL = ('https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz')
data = pd.read_csv(DATA_URL, nrows=10)
st.write(data)