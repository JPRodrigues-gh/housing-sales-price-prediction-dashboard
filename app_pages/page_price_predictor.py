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
    ver = 'v2'
    path = f"outputs/ml_pipeline/predict_saleprice/{ver}"

    price_pipe = load_pkl_file(f"{path}/best_regressor_pipeline.pkl")
    price_features = (pd.read_csv(f"{path}/X_train.csv")
                      .columns
                      .to_list()
                      )
    feature_importance = list(pd.read_csv(f"{path}/feature_importance.csv")['Feature'])

    st.write("### Sale Price Prediction Interface")
    st.info(
        f"* The client is interested in predicting the house sales price"
        f" for her 4 inherited houses, and any other house in Ames, Iowa."
        )
    st.write("---")

    st.write("### Inherited houses price prediction")
    st.info(
        f"* Below are the details of the inherited "
        f"houses and their respective price predictions."
        )
    total_price = predict_inherited_house_price(price_pipe, price_features)
    total_price = "%.2f" % total_price
    st.info(
        f"The sum total sale price for all your "
        f"properties is \u20AC{total_price}"
        )
    st.write("---")

    # Generate Live Data
    check_var = False
    if check_var:
        check_variables_for_UI(price_features)

    st.write("### Houses Price Predictor")
    st.info(
        f"* Enter the values for the property for "
        f"which you require a **price prediction**."
        )
    X_live = DrawInputsWidgets()

    # predict on live data
    if st.button("Run Predictive Analysis"):
        price_prediction = predict_sale_price(X_live,
                                              price_features,
                                              price_pipe)
        # logic to display the sale price
        statement = (
            f"The predicted selling price for this house "
            f"is \u20AC{price_prediction}"
            )

        st.info(statement)


def predict_inherited_house_price(price_pipe, price_features):
    inherited = load_clean_data("inherited")
    row_count = len(inherited)
    inherited.index = range(1, row_count+1)
    total_price = 0
    for x in range(row_count):
        X_live = inherited.iloc[[x]]
        st.write(X_live)
        price_prediction = predict_sale_price(X_live,
                                              price_features,
                                              price_pipe)
        price_prediction = "%.2f" % price_prediction
        statement = (
            f"* The predicted selling price for house "
            f"{x+1} is \u20AC{price_prediction}"
            )
        total_price += float(price_prediction)
        st.write(statement)
        
    return total_price

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
    df = load_clean_data("clean")
    percentageMin, percentageMax = 0.4, 2.0

    # we create input widgets for all features
    col1, col2 = st.beta_columns(2)
    col3, col4 = st.beta_columns(2)
    # col4, col5, col6 = st.beta_columns(3)
    # col7, col8, col9 = st.beta_columns(3)
    # col10, col11, col12, = st.beta_columns(3)
    # col13, col14, col15, = st.beta_columns(3)
    # col16, col17, col18 = st.beta_columns(3)
    # col19, col20, col21 = st.beta_columns(3)

    # We are using these features to feed the ML pipeline
    # - values copied from check_variables_for_UI() result
    # '1stFlrSF', 'GarageArea', 'GrLivArea', 'YearBuilt'
    #  'LotArea', 'BsmtUnfSF', 'KitchenQual', 'BsmtFinSF1',
    #  'GarageYrBlt', 'TotalBsmtSF', '2ndFlrSF', 'MasVnrArea',
    #  'OverallQual', 'OverallCond', 'LotFrontage', 'GarageFinish',
    #  'BedroomAbvGr', 'BsmtFinType1', 'OpenPorchSF',
    #  'BsmtExposure', 'YearRemodAdd'

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
        feature = "GrLivArea"
        st_widget = st.number_input(
            label=feature,
            min_value=df[feature].min()*percentageMin,
            max_value=df[feature].max()*percentageMax,
            value=df[feature].median()
            )
        X_live[feature] = st_widget

    with col3:
        feature = "GarageArea"
        st_widget = st.number_input(
            label=feature,
            min_value=df[feature].min()*percentageMin,
            max_value=df[feature].max()*percentageMax,
            value=df[feature].median()
            )
        X_live[feature] = st_widget

    with col4:
        feature = "YearBuilt"
        st_widget = st.number_input(
            label=feature,
            min_value=df[feature].min()*percentageMin,
            max_value=df[feature].max()*percentageMax,
            value=df[feature].median()
            )
        X_live[feature] = st_widget

    # with col5:
    #     feature = "OverallQual"
    #     st_widget = st.number_input(
    #         label=feature,
    #         min_value=df[feature].min()*percentageMin,
    #         max_value=df[feature].max()*percentageMax,
    #         value=df[feature].median()
    #         )
    #     X_live[feature] = st_widget

    # with col6:
    #     feature = "2ndFlrSF"
    #     st_widget = st.number_input(
    #         label=feature,
    #         min_value=df[feature].min()*percentageMin,
    #         max_value=df[feature].max()*percentageMax,
    #         value=df[feature].median()
    #         )
    #     X_live[feature] = st_widget

    # with col7:
    #     feature = "BedroomAbvGr"
    #     st_widget = st.number_input(
    #         label=feature,
    #         min_value=df[feature].min()*percentageMin,
    #         max_value=df[feature].max()*percentageMax,
    #         value=df[feature].median()
    #         )
    #     X_live[feature] = st_widget

    # with col8:
    #     feature = "KitchenQual"
    #     st_widget = st.selectbox(
    #         label=feature,
    #         options=df[feature].unique()
    #         )
    #     X_live[feature] = st_widget

    # with col9:
    #     feature = "BsmtExposure"
    #     st_widget = st.selectbox(
    #         label=feature,
    #         options=df[feature].unique()
    #         )
    #     X_live[feature] = st_widget

    # with col10:
    #     feature = "BsmtFinType1"
    #     st_widget = st.selectbox(
    #         label=feature,
    #         options=df[feature].unique()
    #         )
    #     X_live[feature] = st_widget

    # with col11:
    #     feature = "BsmtFinSF1"
    #     st_widget = st.number_input(
    #         label=feature,
    #         min_value=df[feature].min()*percentageMin,
    #         max_value=df[feature].max()*percentageMax,
    #         value=df[feature].median()
    #         )
    #     X_live[feature] = st_widget

    # with col12:
    #     feature = "BsmtUnfSF"
    #     st_widget = st.number_input(
    #         label=feature,
    #         min_value=df[feature].min()*percentageMin,
    #         max_value=df[feature].max()*percentageMax,
    #         value=df[feature].median()
    #         )
    #     X_live[feature] = st_widget

    # with col13:
    #     feature = "TotalBsmtSF"
    #     st_widget = st.number_input(
    #         label=feature,
    #         min_value=df[feature].min()*percentageMin,
    #         max_value=df[feature].max()*percentageMax,
    #         value=df[feature].median()
    #         )
    #     X_live[feature] = st_widget

    # with col14:
    #     feature = "GarageFinish"
    #     st_widget = st.selectbox(
    #         label=feature,
    #         options=df[feature].unique()
    #         )
    #     X_live[feature] = st_widget

    # with col15:
    #     feature = "GarageYrBlt"
    #     st_widget = st.number_input(
    #         label=feature,
    #         min_value=df[feature].min()*percentageMin,
    #         max_value=df[feature].max()*percentageMax,
    #         value=df[feature].median()
    #         )
    #     X_live[feature] = st_widget

    # with col16:
    #     feature = "MasVnrArea"
    #     st_widget = st.number_input(
    #         label=feature,
    #         min_value=df[feature].min()*percentageMin,
    #         max_value=df[feature].max()*percentageMax,
    #         value=df[feature].median()
    #         )
    #     X_live[feature] = st_widget

    # with col17:
    #     feature = "OpenPorchSF"
    #     st_widget = st.number_input(
    #         label=feature,
    #         min_value=df[feature].min()*percentageMin,
    #         max_value=df[feature].max()*percentageMax,
    #         value=df[feature].median()
    #         )
    #     X_live[feature] = st_widget

    # with col18:
    #     feature = "LotArea"
    #     st_widget = st.number_input(
    #         label=feature,
    #         min_value=df[feature].min()*percentageMin,
    #         max_value=df[feature].max()*percentageMax,
    #         value=df[feature].median()
    #         )
    #     X_live[feature] = st_widget

    # with col19:
    #     feature = "LotFrontage"
    #     st_widget = st.number_input(
    #         label=feature,
    #         min_value=df[feature].min()*percentageMin,
    #         max_value=df[feature].max()*percentageMax,
    #         value=df[feature].median()
    #         )
    #     X_live[feature] = st_widget

    # with col20:
    #     feature = "OverallCond"
    #     st_widget = st.number_input(
    #         label=feature,
    #         min_value=df[feature].min()*percentageMin,
    #         max_value=df[feature].max()*percentageMax,
    #         value=df[feature].median()
    #         )
    #     X_live[feature] = st_widget

    # with col21:
    #     feature = "YearRemodAdd"
    #     st_widget = st.number_input(
    #         label=feature,
    #         min_value=df[feature].min()*percentageMin,
    #         max_value=df[feature].max()*percentageMax,
    #         value=df[feature].median()
    #         )
    #     X_live[feature] = st_widget

    st.write(X_live)

    return X_live
