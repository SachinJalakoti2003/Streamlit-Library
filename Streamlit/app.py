import streamlit as st

st.title("Hello World "  +  " Starting the Streamlit Library")
st.header("Sachin Jalakoti")
st.subheader("Sachin Jalakoti")
st.text("Welcome to Streaming")

st.markdown("# Hi")

st.success("I win the Game")
st.info("Information of the Game")
st.warning("You are not allow to use multiple user name")
st.error("Error in the Game as user name is not valid")

st.exception(ZeroDivisionError("Division not possible with zero"))
st.help(ZeroDivisionError)

st.write("Enjoy your day")
st.write(range(1,10))
st.write(1+2+5)

st.code('x=10\n'
       'for i in range(x):\n'
        '\tprint(i)' )

st.checkbox('Male')
if(st.checkbox('Adult')):
    st.write("You are an adult !")
  
radiobtn=  st.radio('Select  :',('Male','Female','Other'))

if(radiobtn=='Male'):
    st.write("You are a  Male")
elif(radiobtn=="Female"):
    st.write("You are Female")
elif(radiobtn=='other'):
    st.write("You are other gender")      


st.subheader("Select Box")
st.selectbox("Data Scicence :", ["Data analyst","web scripting","NLP","ML","Deep Learning"])      


st.subheader("MultiSelectBox")
multiselectBox=st.multiselect("Data Scicence :", ["Data analyst","web scripting","NLP","ML","Deep Learning"])      
st.write("You have selected",len(multiselectBox),"Courses")

st.subheader("Button")
if(st.button("click here")):
    st.write("successfully submited !")

st.subheader("Slider")
st.slider('Select  the level', 1,10, step=1)   
vol=st.slider('Select  the volume', 0,100, step=10)
st.write("Volume is",vol)  


st.subheader("User input")
name=st.text_input("Name :")
if(name):
    st.write("Hi",name)

username=st.text_input("Username :")
password=st.text_input("Password :",type="password")

st.subheader("Text Area")
st.text_area("Write about youself in 20 words",height=20)


st.subheader("Input Number")
st.number_input("Enter you age",18,65)


st.subheader("Input Date")
st.date_input("Enter you birth date :")

st.subheader("Input Time")
st.time_input("Set Your Timer")

st.subheader("Loading the CSV File")
df=st.file_uploader("Upload the CSV file :")
st.subheader("Loading the CSV File")
df=st.file_uploader("Upload the CSV file :",type=['csv','pdf','xlsx'])






