from html.entities import html5
from PIL import Image
image = Image.open('./Dstats_table.png')
weather_image = Image.open('./temp_example.png')
import pickle
import streamlit as st
import numpy as np
import pandas as pd
import xgboost as xgb # model version '1.6.0'


# to run write in terminal streamlit run streamlit.py

model10_pickled = xgb.XGBClassifier()
model10_pickled.load_model("./model10.json")


st.title('How dangerous are these conditions?')

#with open('../Code/Models/rfmodel.pkl', 'rb') as pickle_in:
    #model = pickle.load(pickle_in)

with open('../Code/Models/columns_list.pkl', 'rb') as pickle_in:
    columns = pickle.load(pickle_in)





df_list = columns
form_list = [[]]
list_diff = []

with st.form('prediction_form'):
    state = st.text_input('State(abbreviations i.e. CA)', max_chars=2)
    #county = st.text_input('County', max_chars=15)
    precipitation = st.text_input('Precipitation (inches)', max_chars = 6) # fifth importance ranking
    #population = st.text_input('Population', max_chars=10)
    temp = st.text_input('Avergae Temperature (Fahrenheit)', max_chars = 4) # fourth imporance ranking
    st.write('''For Monthly Temperature Average feel free to use this (use search bar for specific location) [link](https://www.timeanddate.com/weather/usa/los-angeles/climate)  \n \
                Refer to Image below: ''')
    col1, col2, col3, col4,col5,col6, col7, col8, col9,col10= st.columns(10)
    with col2:
        st.image(weather_image, caption='''Sample Temperature Image of Los Angeles, CA (Use 'Mean Temp' Value)''',
                            width=600, use_column_width=None)



    lat = st.text_input('lat', max_chars = 15) # first importance ranking
    long = st.text_input('long', max_chars = 15) # second importance ranking
    year = st.text_input('year', max_chars = 4) #
    month = st.text_input('month', max_chars = 10) # third importance ranking
    st.write('''For Drought INDEX values below use this [link](https://droughtmonitor.unl.edu/)  \n \
     Directions: ''')
    st.write('''- Click on the region then on state of interest''')
    st.write('''- Scroll down to tables and edit drop down to show "Categorical Percent Area" ''')
    st.write('''- "Last Week" Values''')
    st.image(image, caption='''Sample Table Image (Use 'Last Week' Values)''', width=None, use_column_width=None)





    d0 = st.text_input('D0 Index (weekly)', max_chars = 8)
    d1 = st.text_input('D1 Index (weekly)',max_chars = 8)
    d2 = st.text_input('D2 Index (weekly)', max_chars = 8)
    d3 = st.text_input('D3 Index (weekly)',max_chars = 8)
    d4 = st.text_input('D4 Index (weekly)',max_chars = 8)
    submitted = st.form_submit_button("Submit")
    if submitted:
        form_list[0].append(1)
        #form_list[0].append(county.lower())
        form_list[0].append(float(precipitation))

        form_list[0].append(float(temp))
        form_list[0].append(float(lat))
        form_list[0].append(float(long))
        form_list[0].append(float(year))
        form_list[0].append(float(month))
        form_list[0].append(float(d0))
        form_list[0].append(float(d1))
        form_list[0].append(float(d2))
        form_list[0].append(float(d3))
        form_list[0].append(float(d4))
        # calculated with USDM stats ref: https://droughtmonitor.unl.edu/About/AbouttheData/DSCI.aspx
        form_list[0].append(float( (d0*1)+(d1*2)+(d2*3)+(d3*4)+(d4*5) ))

        df = pd.DataFrame(form_list, columns = ['state_'+state.upper(),'precipitation(in)', 'values', 'longitude', 'lattitude', 'year', 'month', 'd0','d1','d2','d3','d4','DSCI_summed'])
        #df = pd.get_dummies(columns=['state'],data=df)
        df = df.reindex(columns=columns).fillna(0)


        # for col in df.columns:
        #     if col not in df_list:
        #         list_diff.append(col)
        #print('Hello')
        preds = model10_pickled.predict(df)
        st.write('PREDICTING FIRE CLASS OF',str(preds[0]))
        #st.write(df)
