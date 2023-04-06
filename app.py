import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from io import StringIO
st.title('Chingu login Analysis')

uploaded_file = st.file_uploader("Choose a csv file including 'date' column.")

if uploaded_file is not None:

 df = pd.read_csv(uploaded_file, sep=",", usecols=["date"])
 df = df.dropna(axis=0)

 date_list = pd.to_datetime(df.squeeze()).dt.date.tolist()
 date_list.sort()

 start_date = date_list[0]
 end_date = date_list[-1]
 day_count = (end_date - start_date).days + 1

 x = np.arange(start_date, end_date + timedelta(days=1), timedelta(days=1)).astype(datetime)
 y = np.zeros(day_count)

 for d in date_list:
     y[(d - start_date).days] += 1

 y_count = np.cumsum(y)
 df = pd.DataFrame({'date': x, 'count': y_count})

 st.area_chart(df.set_index('date'))
 col1, col2 = st.columns(2)
 col1.metric("rows", len(date_list))
 col2.metric("days", day_count)
 col3, col4 = st.columns(2)
 col3.metric("start", str(start_date))
 col4.metric("end", str(end_date))

