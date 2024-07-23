import streamlit as st
import pickle
import pandas as pd

def load_model():
    with open('models/mlp_pipeline.pkl', 'rb') as file:
        loaded_pipeline = pickle.load(file)
        return loaded_pipeline


def show_predict_page():
    
    model = load_model()
    
    st.title('Malaysia Sustainable Tourism Accommodation Predictor')
    st.write('Welcome to the Malaysia Sustainable Accommodation Predictor, a web application that leverages machine learning to assess the sustainability of tourist accommodations in Malaysia. Input your data to predict sustainability and contribute to responsible tourism practices.')
    st.image('screenshot/malaysia_sustainable_ota-modified_v2.png')
    
    st.subheader('Basic Property Information')
    quality_rating = st.slider('Property Quality Rating', 0,5,0)
    preferred_partner = st.slider('Booking.com Preferred Partner Program', 0,1,0)
    count_room_types = st.slider('Number of Room Category', 1,7,1)
    
    st.subheader('Property Reviews')
    overall_reviews = st.slider('Current overall reviews',0.0,10.0,0.0)
    count_reviews = st.number_input('Current number of reviews')
    lan_eng_proportion = st.slider('Proportion of English reviews (%)',0.0,100.0,0.0)
    lan_malay_proportion = st.slider('Proportion of Malay reviews (%)',0.0,100.0,0.0)
    
    st.subheader('Property Surrounding')
    count_topattractions = st.slider('Number of nearest attraction',0,10,0)
    count_closestairports = st.slider('Number of nearest airport',0,3,0)
    average_all_closestairports_distances = st.number_input('The average distance to the nearest airport (km)')
    
    st.subheader('Property Services & Facilities Provided')
    st.write('The number of services and facilities provided by the property, including bathroom amenities, business facilities, and more, each encompassing a range of activities and services.')
    bathroom = st.slider('Bathroom', 1,5,1)
    business_facilities = st.slider('Business Service or Facilities',0,4,0)
    common_areas = st.slider('Common Area',0,3,0)
    languages_spoken = st.slider('Languages Spoken Available',1,47,1)
    living_area = st.slider('Living Area',1,5,1)
    miscellaneous = st.slider('Miscellaneous',1,19,1)
    outdoors = st.slider('Outdoors',0,15,0)
    reception_services = st.slider('Reception Service',1,10,1)
    safety_and_security = st.slider('Safety and Security',1,10,1)
    services_and_extras = st.slider('Other Extra Services',0,3,0)
    
    predict = st.button('Predict Sustainability')
    if predict:
        input_data = {
            'quality_rating': [quality_rating],
            'preferred_partner': [preferred_partner],
            'count_room_types': [count_room_types],
            'overall_reviews': [overall_reviews],
            'count_reviews': [count_reviews],
            'count_topattractions': [count_topattractions],
            'count_closestairports': [count_closestairports],
            'lan_eng_proportion': [lan_eng_proportion],
            'lan_malay_proportion': [lan_malay_proportion],
            'average_all_closestairports_distances': [average_all_closestairports_distances],
            'bathroom': [bathroom],
            'business_facilities': [business_facilities],
            'common_areas': [common_areas],
            'languages_spoken': [languages_spoken],
            'living_area': [living_area],
            'miscellaneous': [miscellaneous],
            'outdoors': [outdoors],
            'reception_services': [reception_services],
            'safety_&_security': [safety_and_security],
            'services_&_extras': [services_and_extras]
        }
        
        df = pd.DataFrame(input_data, index=[0])
        prediction = model.predict(df)[0]
        label = "Travel Sustainable" if prediction == 1 else "Non-travel Sustainable"
        
        st.subheader('Predicted Sustainability Status')
        st.write(f'The predicted sustainability is {label}')