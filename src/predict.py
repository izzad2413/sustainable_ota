import streamlit as st
import pickle
import numpy as np

def load_model():
    model = pickle.load(open('./../models/mlp_model.pkl', 'rb'))
    return model

def show_predict_page():
    st.title('Malaysia Sustainable Tourism Accommodation Predictor')
    st.write('#### Welcome to the Malaysia Sustainable Accommodation Predictor, a web application that leverages machine learning to assess the sustainability of tourist accommodations in Malaysia. Input your data to predict sustainability scores and contribute to responsible tourism practices.')
    
    quality_rating = st.slider('Property Quality Rating', 0,5,0)
    preferred_partner = st.number_input('Does your Property subscribed to Booking.com Preferred Partner Program')
    count_room_types = st.number_input('How many times of room type you have')
    overall_reviews = st.number_input('testing')
    count_reviews = st.number_input('testingtt')
    count_topattractions = st.number_input('testingrtrt')
    count_closestairports = st.number_input('testinfgfgg')
    lan_eng_proportion = st.number_input('testinrtrg')
    lan_malay_proportion = st.number_input('testfgfgfging')
    average_all_closestairports_distances = st.number_input('tes7857ting')
    bathroom = st.slider('te657tsting')
    business_facilities = st.slider('testruruying')
    common_areas = st.slider('testryurying')
    languages_spoken = st.slider('tesryryrting')
    living_area = st.slider('testryring')
    miscellaneous = st.slider('tesyrtyrting')
    outdoors = st.slider('testfghgfhing')
    reception_services = st.slider('testrtyrying')
    safety_and_security = st.select_slider('234Slide to select', options=[1,'2'])
    services_and_extras = st.select_slider('Slide to select', options=[1,'2'])
    
    predict = st.button('Predict Sustaibility')
