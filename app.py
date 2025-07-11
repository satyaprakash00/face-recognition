import streamlit as st
import pandas as pd
import time 
from datetime import datetime

ts=time.time()
date=datetime.fromtimestamp(ts).strftime("%d-%m-%Y")
timestamp=datetime.fromtimestamp(ts).strftime("%H:%M-%S")

from streamlit_autorefresh import st_autorefresh

count = st_autorefresh(interval=2000, limit=100, key="fizzbuzzcounter")

if count == 0:
    st.write("Count is zero")
elif count % 3 == 0 and count % 5 == 0:
    st.write("FizzBuzz")
elif count % 3 == 0:
    st.write("Fizz")
elif count % 5 == 0:
    st.write("Buzz")
else:
    st.write(f"Count: {count}")


csv_path = f"Attendance/Attendance_{date}.csv"
try:
    df = pd.read_csv(csv_path)
    if df.empty:
        st.warning("Attendance file is empty.")
    else:
        try:
            styled_df = df.style.highlight_max(axis=0)
            st.write(styled_df.to_html(), unsafe_allow_html=True)
        except Exception as e:
            st.write("Could not display styled DataFrame:", e)
            st.dataframe(df)
except FileNotFoundError:
    st.error(f"Attendance file not found: {csv_path}")
except Exception as e:
    st.error(f"Error reading attendance file: {e}")