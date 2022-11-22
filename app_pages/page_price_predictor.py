'''
This file's contents were taken from the
 Churnometer Walkthrough Project 2 and customised for
 this project
'''
import streamlit as st
import pandas as pd
from src.file_management import load_clean_data, load_pkl_file
from src.predictive_analysis_ui import predict_sale_price


def page_price_predictor_body():

    # load predict sale price files
    ver = 'v1'
    path = 'outputs/ml_pipeline/predict_saleprice'

    price_pipe = load_pkl_file(f"{path}/{ver}/best_regressor_pipeline.pkl")
    price_features = (pd.read_csv(f"{path}/{ver}/X_train.csv")
                      .columns
                      .to_list()
                      )

    st.write("### Sale Price Prediction Interface")
    st.info(
        f"* The client is interested in predicting the house sales price"
        f" for her 4 inherited houses, and any other house in Ames, Iowa."
        )
    st.write("---")

    # Generate Live Data
    # check_variables_for_UI(price_features)
    X_live = DrawInputsWidgets()

    # predict on live data
    if st.button("Run Predictive Analysis"):
        price_prediction = predict_sale_price(X_live,
                                              price_features,
                                              price_pipe)


def check_variables_for_UI(price_features):
    import itertools

    # The widgets inputs are the features used
    #  in all pipelines (tenure, churn, cluster)
    # We combine them only with unique values
    combined_features = set(
        list(
            itertools.chain(price_features)
            )
        )
    st.write(f"* There are {len(combined_features)} features "
             f"for the UI: \n\n {combined_features}")


def DrawInputsWidgets():

    # load dataset
    df = load_clean_data()
    percentageMin, percentageMax = 0.4, 2.0

    # we create input widgets only for 6 features
    col1, col2, col3, col4 = st.beta_columns(4)
    col5, col6, col7, col8 = st.beta_columns(4)
    col9, col10, col11, col12 = st.beta_columns(4)
    col13, col14, col15 = st.beta_columns(3)
    col16, col17, col18 = st.beta_columns(3)
    col19, col20, col21 = st.beta_columns(3)

    # We are using these features to feed the ML pipeline
    # - values copied from check_variables_for_UI() result
    # {'LotArea', 'GrLivArea', 'BsmtUnfSF', 'KitchenQual', 'BsmtFinSF1',
    #  'GarageYrBlt', 'GarageArea', 'TotalBsmtSF', '2ndFlrSF', 'MasVnrArea',
    #  'OverallQual', '1stFlrSF', 'OverallCond', 'LotFrontage', 'GarageFinish',
    #  'BedroomAbvGr', 'BsmtFinType1', 'OpenPorchSF', 'YearBuilt',
    #  'BsmtExposure', 'YearRemodAdd'}

    # create an empty DataFrame, which will be the live data
    X_live = pd.DataFrame([], index=[0])

    # from here on we draw the widget based on the variable
    # type (numerical or categorical) and set initial values
    with col1:
        feature = "1stFlrSF"
        st_widget = st.number_input(
            label=feature,
            min_value=df[feature].min()*percentageMin,
            max_value=df[feature].max()*percentageMax,
            value=df[feature].median()
            )
    X_live[feature] = st_widget

    with col2:
        feature = "2ndFlrSF"
        st_widget = st.number_input(
            label=feature,
            min_value=df[feature].min()*percentageMin,
            max_value=df[feature].max()*percentageMax,
            value=df[feature].median()
            )
    X_live[feature] = st_widget

    with col3:
        feature = "BedroomAbvGr"
        st_widget = st.number_input(
            label=feature,
            min_value=df[feature].min()*percentageMin,
            max_value=df[feature].max()*percentageMax,
            value=df[feature].median()
            )
    X_live[feature] = st_widget

    with col4:
        feature = "GrLivArea"
        st_widget = st.number_input(
            label=feature,
            min_value=df[feature].min()*percentageMin,
            max_value=df[feature].max()*percentageMax,
            value=df[feature].median()
            )
    X_live[feature] = st_widget

    with col5:
        feature = "KitchenQual"
        st_widget = st.selectbox(
            label=feature,
            options=df[feature].unique()
            )
    X_live[feature] = st_widget

    with col6:
        feature = "BsmtExposure"
        st_widget = st.selectbox(
            label=feature,
            options=df[feature].unique()
            )
    X_live[feature] = st_widget

    with col7:
        feature = "BsmtFinType1"
        st_widget = st.selectbox(
            label=feature,
            options=df[feature].unique()
            )
    X_live[feature] = st_widget

    with col8:
        feature = "BsmtFinSF1"
        st_widget = st.number_input(
            label=feature,
            min_value=df[feature].min()*percentageMin,
            max_value=df[feature].max()*percentageMax,
            value=df[feature].median()
            )
    X_live[feature] = st_widget

    with col9:
        feature = "BsmtUnfSF"
        st_widget = st.number_input(
            label=feature,
            min_value=df[feature].min()*percentageMin,
            max_value=df[feature].max()*percentageMax,
            value=df[feature].median()
            )
    X_live[feature] = st_widget

    with col10:
        feature = "TotalBsmtSF"
        st_widget = st.number_input(
            label=feature,
            min_value=df[feature].min()*percentageMin,
            max_value=df[feature].max()*percentageMax,
            value=df[feature].median()
            )
    X_live[feature] = st_widget

    with col11:
        feature = "GarageArea"
        st_widget = st.number_input(
            label=feature,
            min_value=df[feature].min()*percentageMin,
            max_value=df[feature].max()*percentageMax,
            value=df[feature].median()
            )
    X_live[feature] = st_widget

    with col12:
        feature = "GarageFinish"
        st_widget = st.selectbox(
            label=feature,
            options=df[feature].unique()
            )
    X_live[feature] = st_widget

    with col13:
        feature = "GarageYrBlt"
        st_widget = st.number_input(
            label=feature,
            min_value=df[feature].min()*percentageMin,
            max_value=df[feature].max()*percentageMax,
            value=df[feature].median()
            )
    X_live[feature] = st_widget

    with col14:
        feature = "MasVnrArea"
        st_widget = st.number_input(
            label=feature,
            min_value=df[feature].min()*percentageMin,
            max_value=df[feature].max()*percentageMax,
            value=df[feature].median()
            )
    X_live[feature] = st_widget

    with col15:
        feature = "OpenPorchSF"
        st_widget = st.number_input(
            label=feature,
            min_value=df[feature].min()*percentageMin,
            max_value=df[feature].max()*percentageMax,
            value=df[feature].median()
            )
    X_live[feature] = st_widget

    with col16:
        feature = "LotArea"
        st_widget = st.number_input(
            label=feature,
            min_value=df[feature].min()*percentageMin,
            max_value=df[feature].max()*percentageMax,
            value=df[feature].median()
            )
    X_live[feature] = st_widget

    with col17:
        feature = "LotFrontage"
        st_widget = st.number_input(
            label=feature,
            min_value=df[feature].min()*percentageMin,
            max_value=df[feature].max()*percentageMax,
            value=df[feature].median()
            )
    X_live[feature] = st_widget

    with col18:
        feature = "OverallCond"
        st_widget = st.number_input(
            label=feature,
            min_value=df[feature].min()*percentageMin,
            max_value=df[feature].max()*percentageMax,
            value=df[feature].median()
            )
    X_live[feature] = st_widget

    with col19:
        feature = "OverallQual"
        st_widget = st.number_input(
            label=feature,
            min_value=df[feature].min()*percentageMin,
            max_value=df[feature].max()*percentageMax,
            value=df[feature].median()
            )
    X_live[feature] = st_widget

    with col20:
        feature = "YearBuilt"
        st_widget = st.number_input(
            label=feature,
            min_value=df[feature].min()*percentageMin,
            max_value=df[feature].max()*percentageMax,
            value=df[feature].median()
            )
    X_live[feature] = st_widget

    with col21:
        feature = "YearRemodAdd"
        st_widget = st.number_input(
            label=feature,
            min_value=df[feature].min()*percentageMin,
            max_value=df[feature].max()*percentageMax,
            value=df[feature].median()
            )
    X_live[feature] = st_widget

    st.write(X_live)

    return X_live
