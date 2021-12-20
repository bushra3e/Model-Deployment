


import streamlit as st
import pickle
import numpy as np
import pandas as pd



def load_model():
    with open('noise.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

model = data['ml']



columns = ['id', 'Gender', 'Customer_Type', 'Age', 'Type_of_Travel', 'Class',
       'Flight_Distance', 'Inflight_wifi_service',
       'Departure/Arrival_time_convenient', 'Ease_of_Online_booking',
       'Gate_location', 'Food_and_drink', 'Online_boarding', 'Seat_comfort',
       'Inflight_entertainment', 'On-board_service', 'Leg_room_service',
       'Baggage_handling', 'Checkin_service', 'Inflight_service',
       'Cleanliness', 'Departure_Delay_in_Minutes', 'Arrival_Delay_in_Minutes',
       'satisfaction']



def show_predict_page():
    st.title(" Airline Passenger Satisfaction info ")

    st.write("""### We need some information for prediction""")

    Gender = (
        "Male",
        "Female"
     
    )

    Customer_Type = (
        "Loyal Customer",
        "disloyal Customer",
    )

    Type_of_Travel = ("Business travel","Personal Travel")
   
   
    Gender = st.selectbox("Gender", Gender)
    Customer_Type = st.selectbox(" Customer_Type",  Customer_Type)
    
   
  
    Type_of_Travel  = st.selectbox("Type_of_Travel ", Type_of_Travel )
   


    ok = st.button("Predict")

    if Gender == "Male":
        Gender = 1
    else:
        Gender = 0

    if Customer_Type == "Loyal Customer":
        Customer_Type = 1
    else:
        Customer_Type = 0



    if Type_of_Travel == "Business travel":
        Type_of_Travel  = 1
    else:
        Type_of_Travel  = 0




    if ok:
        X = np.array([[ 'id', 'Gender', 'Customer_Type', 'Age', 'Type_of_Travel', 'Class',
       'Flight_Distance', 'Inflight_wifi_service',
       'Departure/Arrival_time_convenient', 'Ease_of_Online_booking',
       'Gate_location', 'Food_and_drink', 'Online_boarding', 'Seat_comfort',
       'Inflight_entertainment', 'On-board_service', 'Leg_room_service',
       'Baggage_handling', 'Checkin_service', 'Inflight_service',
       'Cleanliness', 'Departure_Delay_in_Minutes', 'Arrival_Delay_in_Minutes',
       'satisfaction' ]])
        
        
        X = pd.DataFrame(columns=columns)
        
       
        prediction = model.predict(X)


        if prediction == 1:
            prediction = "neutral or dissatisfied"
        else:
            prediction = "satisfied"
            
        st.subheader(f"Is the restaurent going to close? \n {prediction}")


show_predict_page()