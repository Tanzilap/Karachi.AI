# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 15:45:03 2023

@author: Administrator
"""
import pandas as pd
import streamlit as st

file = r'C:/Users/Administrator/Desktop/Python/Billionaire.csv'
df = pd.read_csv('Billionaire.csv')

df['NetWorth'] = df['NetWorth'].apply(lambda x : float(x.replace('$','').replace('B','')))

all_countries = sorted(df['Country'].unique())
col1,col2 = st.columns(2)
# Column 1
# display on streamlit
selected_country = col1.selectbox('Select your country',all_countries)
#Subset on selected country
subset_country = df[df['Country'] == selected_country]
# get unique sources from the selected country
sources = sorted(subset_country['Source'].unique())
#display multi select option on source 
selected_source = col1.multiselect('select source of income',sources)
# subset on selected source
subset_source = subset_country[subset_country['Source'].isin(selected_source)]
# Column 2
main_string = '{} - Billionaires'.format(selected_country)
col2.header(main_string)
col2.dataframe(subset_country)
col2.header('Source wise info')
col2.dataframe(subset_source)
