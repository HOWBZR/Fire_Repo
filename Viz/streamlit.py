from html.entities import html5
import pickle
import streamlit as st
import numpy as np
import pandas as pd

st.title('How dangerous are these conditions?')

with open('../Code/Models/rfmodel.pkl', 'rb') as pickle_in:
    model = pickle.load(pickle_in)

with open('../Code/Models/columns_list.pkl', 'rb') as pickle_in:
    columns = pickle.load(pickle_in)





df_list = columns
form_list = [[]]
list_diff = []

with st.form('prediction_form'):
    state = st.text_input('State', max_chars=2)
    county = st.text_input('County', max_chars=15)
    precipitation = st.text_input('Precipitation', max_chars=6)
    population = st.text_input('Population', max_chars=10)
    temp = st.text_input('Temperature', max_chars=4)
    lat = st.text_input('lat', max_chars=15)
    long = st.text_input('long', max_chars=15)
    year = st.text_input('year', max_chars = 4)
    month = st.text_input('month', max_chars=10)
    area = st.text_input('area', max_chars = 20)
    

    submitted = st.form_submit_button("Submit")
    if submitted:
        form_list[0].append(state.lower())
        form_list[0].append(county.lower())
        form_list[0].append(precipitation)
        form_list[0].append(population)
        form_list[0].append(temp)
        form_list[0].append(lat)
        form_list[0].append(long)
        form_list[0].append(year)
        form_list[0].append(month)
        form_list[0].append(area)
        

        df = pd.DataFrame(form_list, columns = ['state', 'origin_county','precipitation(in)', 'population', 'values', 'lattitude', 'longitude', 'year', 'month', 'area'])
        df = pd.get_dummies(df, columns = ['state', 'origin_county'])
        # with open('../Code/Models/columns_list2.pkl', 'wb') as pickle_out:
        #     columns2 = pickle.dump(df.columns, pickle_out)
        # df[('state_'+state).lower()] = 1
        # df[('origin_county_'+county).lower()] = 1
        # for i in df_list:
        #     if i.lower() not in df.columns:
        #         df[i.lower()] = 0
        
        df = df.reindex(columns=columns).fillna(0)


        # for col in df.columns:
        #     if col not in df_list:
        #         list_diff.append(col)
        print('Hello')
        st.write(model.predict(df))
        st.write(df)
        


