'''
This file and the contents thereof were taken from the
 Churnometer Walkthrough Project 2 and customised for
 this project
'''
import streamlit as st


def page_project_hypothesis_body():

    st.success(
        f"### Project Hypothesis and Validation\n\n"
        f"* I assume an evaluation of sales prices of other houses, "
        f"in the area of Ames, Iowa, based on attributes similar to attributes"
        f" of each of the clients 4 inherited houses should provide a "
        f"prediction of sales price for each house respectively\n\n"

        f"* The correlation analysis shows that the sizes of the ground floor "
        f"living area, the first floor, the basement and the garage, play a "
        f"key role in determining house price.\n"
        f"* In addition, the year the house was built and the overall quality "
        f"of materials used and the finishes in the house also play a "
        f"significant role in determining house price.\n"
        f"The insight will be taken to the survey team for further "
        f"discussions and investigations."
    )
