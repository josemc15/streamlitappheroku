# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 14:09:23 2022

@author: mcjos
"""

import pickle 
import streamlit as st


#loading the models

Employee_models = pickle.load(open('C:/Users/mcjos/Downloads/Employee_model (1).pkl','rb'))

st.title('Employee Performance')


# getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
         EMP_ID = st.text_input('EMP_ID')
        
    with col2:
       Age = st.text_input('Age')
    
    with col3:
        Gender  = st.text_input('Gender')
    
    with col1:
         Scope_of_Work  = st.text_input('Scope of Work')
    
    with col2:
        Skill_of_employee = st.text_input('Skill of employee')
    
    with col3:
        Experience = st.text_input('Experience(Years)')
    
    with col1:
       Productivity = st.text_input('Productivity')
     
     
   # code for Prediction
    Productivity = ''
    
    # creating a button for Prediction
    
    if st.button('Productivity'):
        Employee_prediction = Employee_models.predict([[EMP_ID,Age,Gender,Scope_of_Work,Skill_of_employee,Experience,Productivity]])
        
      
        if (Employee_prediction[0] == 0):
         Productivity = 'Good'
        else:
          Productivity = 'bad'
    
    st.success(Productivity)
