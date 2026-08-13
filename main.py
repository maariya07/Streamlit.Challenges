import streamlit as st

st.title(" Adnan's Travels")
st.write(" Intercity buses, daily departures")
st.info(" Booking office :6am - 10pm")
Passenger = st.text_input(" Passenger ")
if Passenger:
    st.write(f" THe Passenger is: {Passenger}")
