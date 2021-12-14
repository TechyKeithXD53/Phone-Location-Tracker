import phonenumbers
from phonenumbers.phonenumberutil import length_of_geographical_area_code
from phonenumbers import geocoder
from phonenumbers import carrier
import streamlit as st

def main():
    st.title("Phone Number Location Tracker & Also Service Operator")
    st.subheader("Build with Python & Streamlit")
    mobile_numbers = st.text_input("Enter Your Phone Numbers: ", type="password")
    if st.button("Track"):
        ch_number = phonenumbers.parse(mobile_numbers, "CH")
        true_location = geocoder.description_for_number(ch_number, "en")
        st.success("Country Name: {}".format(true_location))
        services_operator = phonenumbers.parse(mobile_numbers, "RO")
        true_services = carrier.name_for_number(services_operator, "en")
        st.success("Service Operator: {}".format(true_services))

if __name__ == "__main__":
    main()