import streamlit as st
st.title("title: Hello Geeks")
st.header("header: Hello Geeks")
st.subheader("subheader: Hello Geeks")
st.text("text: Hello Geeks")

st.markdown("# Hi")
st.markdown("## Hi")
st.markdown("### Hi")
st.markdown("#### Hi")

st.success("Success!")
st.info("Information!")
st.warning("Warning!")
st.error("Error!")

st.exception(ZeroDivisionError('Division not possible with 0'))
st.help(ZeroDivisionError)

st.write("range(1,10)")
st.write(range(1,10))
st.write(1*2*3)

st.code('x=10 \n '
        'for i in range(1,x): \n'
        '\tprint(i)')

st.checkbox('Male')
if(st.checkbox('Adult')):
    st.write("You're an Adult")


radioButton=st.radio('Select: ', ('Male','Female','Other'))
if(radioButton=='Male'):
    st.write("You're a male")
elif(radioButton=='Female'):
    st.write("You're are a Female")
else:
    st.write("You're are an Other")

st.subheader("Select Box")
selected=st.selectbox('Data Science: ',['Data Analysis','Image processing','Web scraping','Machine Learning','Computer vision'])
st.write("You have selected, "+selected)



st.subheader("Multi Select Box")
multiSelected=st.multiselect('Data Science: ',['Data Analysis','Image processing','Web scraping','Machine Learning','Computer vision','Deep learning','Natural processing Language'])
st.write("You have selected, ",len(multiSelected)," courses")


st.subheader("Button")
if(st.button("click me")):
    st.write("Thanks for clicking me")

st.subheader("Slider")
sliderVal=st.slider('Select the volume',1,100,step=1)
st.write("volume is: ",sliderVal)


st.subheader("Text Input")
st.text_input("Name: ")
st.text_input("Password: ", type='password')

st.subheader("Text Area")
st.text_area("Write about yourself in 20 words")

st.subheader("Number input")
st.number_input("select the number, ",18,110)

st.subheader("Date input")
st.date_input("select the Date, ")

st.subheader("Time input")
st.time_input("select the Time, ")
