from optparse import Option
import streamlit as st 
c = 3*10^8
h = (6.26)*(10^-34) 
st.header('radiation characteristics :')
Options = ['wavelength','frequency','period']
item = st.selectbox('Select one', Options)
if item == 'frequency' : 
    st.number_input('Frequency Hz', key="f",value=1)
    f = st.session_state.f
    st.text('Frequency         : '+str(f)+' Hz')
    t = 1/int(f)
    st.text('Period            : '+str(t)+' s')
    lamda = c/f
    st.text('wavelength        : '+str(lamda)+' m')
    wn = 1/lamda 
    st.write('waves numbers    : '+str(wn)+' 1/m')
    ep = h*f 
    st.write('Energy of photon : '+str(ep)+' j')
    tem = 2897/lamda 
    st.write('Tempreture       : '+str(tem)+' k')
if item == 'wavelength' : 
    
    st.number_input('wavelength', key="lamda", step=0.000000000000001)
    lamda = st.session_state.lamda
    f = c/lamda
    st.text('wavelength        : '+str(lamda)+' m')
    st.text('Frequency         : '+str(f)+' Hz')
    t = 1/int(f)
    st.text('Period            : '+str(t)+' s')
    wn = 1/lamda 
    st.write('waves numbers    : '+str(wn)+' 1/m')
    ep = h*f 
    st.write('Energy of photon : '+str(ep)+' j')
    tem = 2897/lamda 
    st.write('Tempreture       : '+str(tem)+' k')

if item == 'period' : 
    
    st.number_input('period s', key="t", step = 0.0000000000001)
    t = st.session_state.t
    
    f = 1/t
    st.text('Period            : '+str(t)+' s')
    st.text('Frequency         : '+str(f)+' Hz')
    lamda = c/f
    st.text('wavelength        : '+str(lamda)+' m')
    wn = 1/lamda 
    st.write('waves numbers    : '+str(wn)+' 1/m')
    ep = h*f 
    st.write('Energy of photon : '+str(ep)+' j')
    tem = 2897/lamda 
    st.write('Tempreture       : '+str(tem)+' k')

