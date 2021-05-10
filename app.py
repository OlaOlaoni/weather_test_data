import streamlit as st
import one, two, third, four, five, six, seven, eight, nine, ten

# st.title("The site is under Upgrade...")

st.title('Weather Report Dashboard')

st.markdown("The dashboard will visualize the correlation between the Standard and Constructed instrument for the Trial Readings Data")

# Sidebar Navigation
st.sidebar.write('# Trial Readings')
options = st.sidebar.radio('Select across 10 trial reading:', 
    ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten'])

if options == 'one':
    one.home()
elif options == 'two':
    two.home()
elif options == 'three':
    third.home()
elif options == 'four':
    four.home()
elif options == 'five':
    five.home()
elif options == 'six':
    six.home()
elif options == 'seven':
    seven.home()
elif options == 'eight':
    eight.home()
elif options == 'nine':
    nine.home()
elif options == 'ten':
    ten.home()