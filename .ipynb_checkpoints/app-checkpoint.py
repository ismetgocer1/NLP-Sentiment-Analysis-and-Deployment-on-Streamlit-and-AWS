import streamlit as st

# text message
st.title ("Streamlit Tutorials")
st.text ("Hello streamlit")

#header / subheader 
st.header('This is a header')
st.subheader('This is a subheader')

#writing text
st.write("Writing example text with write function")

#importing image
from PIL import Image
img=Image.open("car.jpg")
st.image(img, width=400, caption="Car Prediction")


#chekbox

if st.checkbox("Hide/Seek"):
    st.text("You checked i show")
    

    
 

#multiselect 
profession = st.multiselect("Select your profession", ["Engineer", "Teacher", "Nurse", "IT"])
st.write("Your profession is", profession)


#date input 
import datetime
today=st.date_input("Today is" , datetime.datetime.now())

#time input  
my_time=st.time_input("Time is" , datetime.time(22,10))

# raw data 
st.text("display text")
st.code("import pandas as pd")

# multiple line 
with st.echo():
    import pandas as pd
    import numpy as np
    import seaborn as sns
    

# sidebar 
st.sidebar.title("This is a sidebar")

# st.balloons() 

# read a dataframe
import pandas as pd
df=pd.read_csv("Advertising.csv")
st.table(df.head()) 

#st.snow()

st.markdown(
    """
    <div style='background-color: orange; padding: 10px;'>
    <h1 style='color: white; text-align: center;'>Streamlit Arayüzü</h1>
    </div>
    """,
    unsafe_allow_html=True
)



#sidebar
st.sidebar.title("Sayının karesini hesaplama")
st.sidebar.markdown("## alt baslik")
a=st.sidebar.slider("input",0,5,2,1)
st.write("# sidebar input result")
st.success(a*a)
