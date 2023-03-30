import streamlit as st

st.title('This is a title')

st.markdown('This is a markdown')

var1 = st.number_input('Number Input',min_value=0, max_value=10)

var2 = st.selectbox('Select Box',('1','2','3'))

if st.button('Button'):
    st.markdown(f'The sum of var1 and var2 is {var1 + int(var2)}')