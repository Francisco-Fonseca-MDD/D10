import numpy as np
import streamlit as st

n = int(st.number_input('Number of dice to roll: ', format = '%i',value = 0))
AutoSucc = int(st.number_input('Number of auto successes: ', format = '%i',value = 0))
TargetNumber = int(st.number_input('Target Number for success: ', format = '%i',value = 7))
DoubleThresh = int(st.number_input('Double all above and including: ', format = '%i',value = 10))


Roll = np.random.randint(1,11,n)

Successes = AutoSucc

for i in Roll:
    if i>=TargetNumber:
        Successes = Successes+1
        if i >= DoubleThresh :
            Successes = Successes+1

st.table(sorted(Roll))
st.write('Number of successes is ' + str(Successes))

if Successes == 0:
    for i in Roll:
        if i == 1:
            st.write('You have botched, F in the chat');
            break
