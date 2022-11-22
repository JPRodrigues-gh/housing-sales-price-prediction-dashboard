'''
This file and the contents thereof were taken from the 
 Churnometer Walkthrough Project 2 and customised for
 this project
'''
import streamlit as st

from app_pages.multi_page import MultiPage

# load pages scripts
from app_pages.page_summary import page_summary_body
from app_pages.page_sale_price_study import page_sale_price_study_body
# from app_pages.page_project_hypothesis import page_project_hypothesis_body
# from app_pages.page_predict_sale_price import page_predict_sale_price_body

app = MultiPage(app_name= "House Price Predictor") # Create an instance of the app 

# Add your app pages here using .add_page()
app.add_page("Quick Project Summary", page_summary_body)
app.add_page("House Sale Price Study", page_sale_price_study_body)
# app.add_page("Project Hypothesis and Validation", page_project_hypothesis_body)
# app.add_page("ML: House Sale Price Prediction", page_predict_sale_price_body)

app.run() # Run the  app