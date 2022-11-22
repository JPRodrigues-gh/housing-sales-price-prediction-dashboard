'''
This file's contents were taken from the
 Churnometer Walkthrough Project 2 and customised for
 this project
'''
import streamlit as st


def predict_sale_price(X_live, features, pipeline):

    # from live data, subset features related to this pipeline
    X_live_sale_price = X_live.filter(features)

    # predict
    sale_price_prediction = pipeline.predict(X_live_sale_price)

    # create logic to display the results

    statement = (
        f"* The predicted selling price for this house "
        f"is {sale_price_prediction.round(2)}"
        )

    st.write(statement)
