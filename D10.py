import numpy as np
import streamlit as st

n = int(st.number_input('Number of dice to roll: ', format = '%i',value = 0))
AutoSucc = int(st.number_input('Number of auto successes: ', format = '%i',value = 0))
TargetNumber = st.slider('Select the target number for the roll', min_value=1, max_value=10,value=7)
DoubleThresh = st.slider('Double ALL above and including', min_value=1, max_value=10,value=10)
NoDoubleCheck = st.checkbox('No doubles')



Roll = np.random.randint(1,11,n)

Successes = AutoSucc



st.write('<p style="color:DodgerBlue;">Your Roll is: </p>',unsafe_allow_html=True)
NoSucCounter=0
DoubleCounter=0
for i in sorted(Roll):
    if i>=DoubleThresh:
        if NoDoubleCheck:
            Successes = Successes+1
        else:
            Successes = Successes+2
        #st.write(i,': Double Success')
    elif i >= TargetNumber:
        Successes = Successes+1
        DoubleCounter=DoubleCounter+1
        #st.write(i,': Success')
    else:
        #st.write(i,': No Success')
        NoSucCounter = NoSucCounter+1

StringRoll = str(sorted(Roll))
NoSuc = f"<p style=\"color:#ff0000;\">{StringRoll[0:NoSucCounter*3+1]} </p>"
Suc   = f"<p style=\"color:#009900;\"> {StringRoll[NoSucCounter*3+1:(DoubleCounter+NoSucCounter)*3+1]} </p>"
DoubleSuc   = f"<p style=\"color:#3366ff;\"> {StringRoll[(DoubleCounter+NoSucCounter)*3+1:]} </p>"

RollDisp = NoSuc + Suc + DoubleSuc

if NoDoubleCheck:
    Suc   = f"<p style=\"color:#009900;\"> {StringRoll[NoSucCounter*3+1:]} </p>"
    RollDisp = NoSuc + Suc


st.write(RollDisp,unsafe_allow_html=True)

#st.write('length: ',len(StringRoll))
#st.write('Counter 1: ', NoSucCounter)
#st.write('Counter 2: ', NoSucCounter+DoubleCounter)
#st.write(StringRoll)

st.text(StringRoll)
st.write('Number of successes is ' + str(Successes) )

if Successes == 0:
    for i in Roll:
        if i == 1:
            st.write('You have botched, F in the chat');
            break
