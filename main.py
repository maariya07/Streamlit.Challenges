import streamlit as st


with st.form(" Registration"):
    st.title(" Adnan's Travels")
    st.write("Intercity buses, daily departure")
    st.success(" Booking office 6am - 10pm")
    passenger = st.text_input("passenger")
    destination = st.text_input(" destination")
    seat = st.radio("seat", ["Standard", "Premium"])
   
    extra = st.checkbox("Extra luggage")
    

    submitted = st.form_submit_button("Book")
    if submitted:
        st.success("Booking Confirmed!")
        st.write(f" {passenger} , {destination}")
        st.write(f"Seat:{seat} ")
        if extra:
            st.write(" Extra luggage: Yes")
        else:
            st.write(" Extra luggage: No")
    
    
