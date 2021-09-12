import pickle
import streamlit as st
import os 
from PIL import Image

#os.chdir('C:\\Users\\leven\\Desktop\\Streamlit_ML')
# loading the trained model
pickle_in = open('classifier.pkl', 'rb') 
classifier = pickle.load(pickle_in)
 
@st.cache()
  
# defining the function which will make the prediction using the data which the user inputs 
def prediction(Gender, Married, ApplicantIncome, LoanAmount, Credit_History):   
 
    # Pre-processing user input    
    if Gender == "Male":
        Gender = 0
    else:
        Gender = 1
 
    if Married == "Unmarried":
        Married = 0
    else:
        Married = 1
 
    if Credit_History == "Unclear Debts":
        Credit_History = 0
    else:
        Credit_History = 1  
 
    LoanAmount = LoanAmount / 1000
 
    # Making predictions 
    prediction = classifier.predict( 
        [[Gender, Married, ApplicantIncome, LoanAmount, Credit_History]])
     
    if prediction == 0:
        pred = 'Rejected'
    else:
        pred = 'Approved'
    return pred
      
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
# this is the main function in which we define our webpage  
def main():
    audio_file = open('audio_only.m4a', 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes,start_time=0, format='audio/m4a')
    st.image(Image.open('fibabanka_logo.jpg'), caption='Anlarız Hızla, Çözeriz Hızla',
             use_column_width=True)       
    # front end elements of the web page 
    local_css("style.txt")
    html_temp = """
    <div style ="background-color:rgb(1, 100, 168);padding:13px"> 
    <h1 style ="color:rgb(255,255,255);text-align:center;">Streamlit Loan Prediction ML App</h1> 
    </div> 
    """ 
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # following lines create boxes in which user can enter data required to make prediction 
    Gender = st.selectbox('Gender',("Male","Female"))
    Married = st.selectbox('Marital Status',("Unmarried","Married")) 
    ApplicantIncome = st.number_input("Applicants monthly income") 
    LoanAmount = st.number_input("Total loan amount")
    Credit_History = st.selectbox('Credit_History',("Unclear Debts","No Unclear Debts"))
    result =""
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(Gender, Married, ApplicantIncome, LoanAmount, Credit_History) 
        if result=='Approved':
            st.balloons()
            st.success('Your loan is {}'.format(result))
        else:
            st.error('Your loan is {}'.format(result))
        print(LoanAmount)
    
if __name__=='__main__': 
    main()
