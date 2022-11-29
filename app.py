# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 14:09:23 2022

@author: mcjos
"""

import pickle 
import streamlit as st
from streamlit_option_menu import option_menu

#loading the models

Employee_models = pickle.load(open('C:/Users/mcjos/Desktop/Project/Employee_model.pkl','rb'))

st.title('Employee Performance')


# getting the input data from the user
    col1, col2, col3 , col4 = st.columns(4)
    
    with col1:
        EMP_ID = st.text_input('EMP_ID')
        
    with col2:
       Scope_of_Work = st.text_input('Scope of Work')
    
    with col3:
        Skill  = st.text_input('Skill of employee')
    
    with col4:
         Temperature  = st.text_input('Temperature')
    
    with col1:
        Experience = st.text_input('Experience(Years)')
    
    with col2:
        Heart_Beat = st.text_input('Heart Beat(BPM)')
    
    with col3:
        Daily_wages = st.text_input('Daily wages')
     
     with col4:
         Noise_Detection   = st.text_input('Noise Detection ')
     
     with col1:
        Working_Hours_for_Day  = st.text_input('Working Hours for Day')
    
     with col2:
        Site = st.text_input('Site')    

   # code for Prediction
    Productivity = ''
    
    # creating a button for Prediction
    
    if st.button('Productivity'):
        Employee_prediction = Employee_models.predict([[EMP_ID,Scope_of_Work,Skill,Temperature,Experience,Heart_Beat,Daily_wages,Noise_Detection,Working_Hours_for_Day,Site]])
        
        if (Employee_prediction[0] == 0):
         Productivity = 'Good'
        else:
          Productivity = 'bad'
    
    st.success(Productivity)
