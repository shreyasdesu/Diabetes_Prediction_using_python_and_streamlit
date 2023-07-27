
import pickle
import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from PIL import Image


# loading the saved models

diabetes_model = pickle.load(open('C:/Users/Shreyas/Desktop/Diabetes_Prediction/saved models/diabetes_model.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Semester Project',
                          
                          ['Diabetes Prediction',
                           'Details'
                           
                           ],
                          icons=['heart', 'person'],
                          default_index=0)
    

# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    option = st.selectbox('What is your gender?',('Male', 'Female'))
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    
    with col1:
        if option=="Female":
            Pregnancies = st.number_input('Number of Pregnancies',key="Number of Pregnancies", min_value=0, max_value=1000, value=0, step=1)     
        else:
            Pregnancies=0
            
    with col2:
        Glucose = st.number_input('Glucose Level',key="Glucose Level", min_value=0, max_value=1000, value=0, step=1)
    
    with col3:
        BloodPressure = st.number_input('Blood Pressure value',key="Blood Pressure value", min_value=0, max_value=1000, value=0, step=1)
    
    with col1:
        SkinThickness = st.number_input('Skin Thickness value',key="Skin Thickness value", min_value=0, max_value=1000, value=0, step=1)
    
    with col2:
        Insulin = st.number_input('Insulin Level',key="Insulin Level", min_value=0, max_value=1000, value=0, step=1)
    
    with col3:
        BMI = st.number_input('BMI value',key="BMI value", min_value=0, max_value=1000, value=0, step=1)
    
    with col1:
        DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function value',key="Diabetes Pedigree Function value", min_value=0, max_value=1000, value=0, step=1)
    
    with col2:
        Age = st.number_input('Age of the Person',key="Age of the Person", min_value=0, max_value=1000, value=0, step=1)
    

  
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
            st.markdown(f'<p style="background-color:#ff4b4b;text-align:center;color:#ffffff;font-size:24px;border-radius:2%;">CHECK YOUR RESULTS</p>', unsafe_allow_html=True)
        
            st.markdown(f'<p style="text-align:center;color:#ff4b4b;font-size:16px;">You are suffered from Diabetes</p>', unsafe_allow_html=True)
        
            st.markdown(f'<p style="text-align:center;font-size:12px;">I am sorry to hear that you are suffering from diabetes. It must be challenging to manage your health condition, but please know that you are not alone, and there is help available to you. It takes a lot of courage and strength to deal with this, and I wish you all the best in your journey towards better health.</p>', unsafe_allow_html=True)


             ##################################################################################################################
            def load_data():
                return pd.DataFrame(
                    {
                        "Label": ["Pregnancies", "Glucose", "BloodPressure", "SkinThickness","Insulin","BMI","DiabetesPedigreeFunction","Age"],
                        "Value": [Pregnancies, Glucose, BloodPressure, SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age],
                    }
                )    
            df = load_data()
            st.dataframe(df)
            
            img1 = Image.open("diabetes/Bhujangasana.jpg")
            img2 = Image.open("diabetes/Dhanurasana.jpg")
            img3 = Image.open("diabetes/Mandukasana.jpg")
            img4 = Image.open("diabetes/Paschimottanasana.jpg")
            img5 = Image.open("diabetes/Pawanmuktasana.jpg")
            img6 = Image.open("diabetes/Purvottanasana.jpg")
            img7 = Image.open("diabetes/Sarvangasana.jpg")
            img8 = Image.open("diabetes/Shavasana.jpg")
            img9 = Image.open("diabetes/Surya Namaskar.jpg")
            img10 = Image.open("diabetes/Viparita Karani.jpg")


            st.subheader('Yoga Poses for Diabetes: Asanas to Help Control Blood Sugar Levels')

            col1, col2, col3 = st.columns(3)

            with col1:
                st.image(img1,caption='Bhujangasana')        

            with col2:
                st.image(img2,caption='Dhanurasana')

            with col3:
                st.image(img3,caption='Mandukasana')

            with col1:
                st.image(img4,caption='Paschimottanasana')        

            with col2:
                st.image(img5,caption='Pawanmuktasana')

            with col3:
                st.image(img6,caption='Purvottanasana')

            with col1:
                st.image(img7,caption='Sarvangasana')        

            with col2:
                st.image(img8,caption='Shavasana')

            with col3:
                st.image(img9,caption='Surya Namaskar')

            with col1:
                st.image(img10,caption='Viparita Karani')

            st.video("https://youtu.be/2Ij3i295XLE")
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)
    
if (selected == 'Details'):

    st.title('Details')

    st.subheader('Student Details:')

    st.text('Name: Shreyas Naik')

    st.text('Batch: T. Y. BSc (Computer Science)')
    
    

    st.subheader('Project Details:')

    st.text('Name: Diabetes Prediction using Machine Learning')

    st.text('Algorithm used: Support Vector Machine')
    
    st.text('Frontend: Streamlit')

    st.text('Backend: Python')
    
