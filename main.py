import streamlit as st
left, center, right=st.columns([1,2,1])
with center:
    st.title ("Mahad's Shop")
    with st.form(" The Receipt"):
        costumer = st.text_input("Costumer")
        st.text_input("Item")
        quantity =st.number_input("Quantity", min_value= 0 , max_value= 500)
        price =st.number_input("Price", min_value= 0 , max_value= 500)
        submitted = st.form_submit_button("SUMBIT")
        if submitted:
            st.success("Receipt REady!")
            st.write(f"Name: {costumer}")
            Total = quantity * price
            st.write (f" Quantity: {quantity}")
        
            st.write(f"Total:  {Total}")

      
    
    
