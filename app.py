
import streamlit as st
import pandas as pd
import numpy as np
import pandas
import pickle
import time



st.set_page_config(
    page_title="Depression Activity Monitor",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.title('Depression Activity Monitor')

# =-----------sidebar---------------_#
st.sidebar.title("UPLOAD YOUR DAYS ACITIVITY HERE 📈🏋🏻‍♂️")
st.sidebar.info("We accept all types of devices Apple watch, MI bands, Samsumg Smart Watch.....")
st.markdown(""" 
            * Depression is a **common and serious medical illness** that cause feeling of sadness   
            and **our team 'EPOCH' are here to tackle this issue in real life and help people 
                identify depression levels** and alert them  and advise them to get urgent medical care
            * The prediction uses a **continous 3-day activity data with 1-min intervals. We accpet CSV or smart watch data!!** 
            * We have a provided a sample test data in the github repository generated using SMOTE, which can be used to test or can be refrenced and generate more entries for further testing.
            
            GitHub link: https://github.com/DChops/dlw-dashboard 
                 """)
col1, col2, col3 = st.columns([1,6,1])

with col1:
    st.write("")

with col2:
    st.image("fav.png",width=600)

with col3:
    st.write("")

df=pd.read_csv("Test Data.csv",delimiter='\t')

uploaded_file=st.sidebar.file_uploader("Upload a CSV file of your ACTIVITY DATA",type='csv',help='Need a Time Series data with respective amount of activity')


st.sidebar.markdown("####  ")

if(st.sidebar.button("Click to connect your bluetooth smart watches")):
    st.sidebar.text("""
    Sorry! This service is currently
    under-development
     """)
#n = st.sidebar.slider(" ", min_value=100, max_value=10000, value=100)

# import time
# my_bar = st.progress(0)
# for percent_complete in range(10):
#     time.sleep(0.1)
#     my_bar.progress(percent_complete*10 + 10)
# # prediction


if uploaded_file is not None:
    col1, col2 = st.columns(2)
    with col1:
            st.markdown("### **Dataframe**")
            st.markdown('#')
            df=pd.read_csv(uploaded_file,delimiter='\t')
            st.dataframe(df,400,400)
    with col2:
        st.markdown("### **Visualize your activity**")
        interval = st.slider(
        "Choose your interval:",
        max_value=len(df),
        value=(0, 100))
        st.write("Interval --> ", interval)
        st.area_chart(df['activity'][interval[0]:interval[1]])
else:
    st.info("Please Upload your daily activity data for analysis and predictions!!This data displayed is preloaded")
    col1, col2 = st.columns(2)
    with col1:
            st.markdown("### **Dataframe**")
            st.markdown('#')
            st.dataframe(df,400,400)
    with col2:
        st.markdown("### **Visualize your activity**")
        interval = st.slider(
        "Choose your interval:",
        max_value=len(df),
        value=(0, 100))
        st.write("Interval --> ", interval)
        st.area_chart(df['activity'][interval[0]:interval[1]])
    
with st.spinner('Loading the transform and prediction Models...'):

    # tranform model
    transform_model=pickle.load(open('rocket.pkl', 'rb'))

    # classififcation model
    loaded_model = pickle.load(open('classifier.pkl', 'rb'))

    time.sleep(1)

st.success('Done!')

x=1
#depressed=loaded_model.predict(x)
# if(depressed):
#     k=1
# else:
#     k=0


    #st.markdown("## Have A Nice Day !!")
# st.sidebar.markdown("#### S (Threshold) ")
# s = st.sidebar.slider(" ", min_value=1, max_value=100, value=5)

    
# col2.markdown("Worst Case : " + str(max(result)))
# #if(col2.checkbox('Click to see list with worst complexity')):
# with col2.expander('Click to see list with worst complexity '):
#     st.write(data_copy[result.index(max(result))])
# st.markdown(
#     '### Keeping N same as provided and runing simulation for variable S(1-100)')

# s_result=variable_s_hybridsorting(n)
# x=list(range(1,17))
# x.extend([20,30,40,50,60,70,80,90,100])
# chart_data = pd.DataFrame(
#     s_result,
#     columns=["Key comparisons"])
# chart_data.set_index(pd.Index(x),inplace=True)
# #st.dataframe(chart_data)
# st.line_chart(chart_data)
feedback=st.text_area('Feedback')
if (st.button('Submit')):
    st.write('Thank You! For your valuable feedback ☺️')
