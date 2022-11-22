'''
The contents of this file were taken from the
 Churnometer Walkthrough Project 2 and customised for
 this project
'''
import streamlit as st
import pandas as pd
import joblib


@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def load_housing_price_data():
    df = pd.read_csv("inputs/datasets/raw/house-price-20211124T154130Z-001/house-price/house_prices_records.csv")
    return df


def load_pkl_file(file_path):
    return joblib.load(filename=file_path)
