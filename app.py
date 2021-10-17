
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
                 """)
col1, col2, col3 = st.columns([1,6,1])

with col1:
    st.write("")

with col2:
    st.image("fav.png",width=600)

with col3:
    st.write("")


uploaded_file=st.sidebar.file_uploader("Upload a CSV file of your ACTIVITY DATA",type='csv',help='Need a Time Series data with respective amount of activity')


st.sidebar.markdown("####  ")

if(st.sidebar.button("Click to connect your bluettoth smart watches")):
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
with st.spinner('Loading the transform and prediction Models...'):

    # tranform model
   # transform_model=pickle.load(open('rocket.pkl', 'rb'))

    # classififcation model
    #loaded_model = pickle.load(open('classifier.pkl', 'rb'))

    time.sleep(1)

st.success('Done!')

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
    st.info("Please Upload your daily activity data for analysis and predictions!!")
    

x=1
#depressed=loaded_model.predict(x)
# if(depressed):
#     k=1
# else:
#     k=0


    #st.markdown("## Have A Nice Day !!")
# st.sidebar.markdown("#### S (Threshold) ")
# s = st.sidebar.slider(" ", min_value=1, max_value=100, value=5)


# loading data
# data_load_state = st.text(
#     "Generating randomly generated list of size : " + str(n)+" .....")
# data = generaterandom(n)
# data_load_state.text('Generating....done!')
# # st.dataframe(data)

# st.info(""" 
#         Value of **N (list size):**
#         """
#         + str(n) +
#         """
        
#         Value of **S (Threshold):** 
#             """
#         + str(s))

# # st.write(pd.array(data.loc[1]))

# #---- perfrom sorting ------------#
# with st.expander('Click to see code for HybridSort'):
#     st.code("""
# def hybrid_sort(array, left_index, right_index,s):
#     # recursion ending statement
#     global compares
#     if right_index-left_index <= s:
#         hybridinsertion_sort(array,left_index,right_index)
#         return
    
#     # finding middle
#     middle = (left_index + right_index)//2
    
#     # recursive call 1
#     hybrid_sort(array, left_index, middle,s)
#     # recurive call 2
#     hybrid_sort(array, middle + 1, right_index,s)
    
#     # merging the returned arrays after recurrsion
#     merge(array, left_index, right_index, middle)
    
    
# def merge(array, left_index, right_index, middle):
    
#     global compares
#     # making copies of list
#     left_list=array[left_index:middle+1]
#     right_list=array[middle+1:right_index+1]
    
#     # intialising indexes
#     left_list_index=0
#     right_list_index=0
#     sorted_index=left_index
    
    
#     while(left_list_index<len(left_list) and right_list_index<len(right_list)):
        
#         # If left_list has the smaller element, put it in the sorted
#         # part and then move forward in left_copy
#         if left_list[left_list_index] <= right_list[right_list_index]:
#             array[sorted_index] = left_list[left_list_index]
#             left_list_index = left_list_index + 1
#             #comparison=comparison+1
#             compares=compares+1
#         # else put the right_list ement in sorted array
#         else:
#             array[sorted_index] = right_list[right_list_index]
#             right_list_index = right_list_index + 1
#             compares=compares+1
        
#         # increasing sorted index
#         sorted_index=sorted_index+1
        
#     # Wran out of elemnt in either one of the list
#     # so we will put the remaining elements and add them to the sorted list
#     while left_list_index < len(left_list):
#         array[sorted_index] = left_list[left_list_index]
#         left_list_index = left_list_index + 1
#         sorted_index = sorted_index + 1
    
#     while right_list_index < len(right_list):
#         array[sorted_index] = right_list[right_list_index]
#         right_list_index = right_list_index + 1
#         sorted_index = sorted_index + 1
        
    
# def hybridinsertion_sort(array,start,end):
#     global compares
#     for index in range(start, end+1):
#         curr = array[index]
#         curr_pos = index
        
#         while curr_pos > 0 and array[curr_pos - 1] > curr:
#             array[curr_pos] = array[curr_pos -1]
#             curr_pos = curr_pos - 1
#             compares=compares+1
#         array[curr_pos] = curr



#             """)

# st.markdown('### Running 1000 random list simulations for provided N and S value')

# import copy
# data_copy = copy.deepcopy(data)
# # result=perform_mergesorting(data_2)
# # st.table(result)
# # st.line_chart(result)

# # st.table(data)
# result = perform_hybridsorting(data,s)
# st.line_chart(result)
# # st.table(result)
# # st.table(result)
# st.balloons()

# col1, col2 = st.columns(2)
# col1.subheader('Average Key comparisons')
# col1.write("""
#          **The average key comparisons of all simulations ran :**
#          """)
# col1.write(Average(result))
# col2.subheader('Worst and best cases')
# col2.markdown("Best Case : " + str(min(result)))
# with col2.expander('Click to see list with best complexity '):
#     st.write(data_copy[result.index(min(result))])
    
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
