## Dataset Content
* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/housing-prices-data).
  * We created a fictitious user story where predictive analytics can be applied in a real project in the workplace. 
* The dataset has almost 1.5 thousand rows and represents housing records from Ames, Iowa;
  * The dataset contains house profiles (Floor Area, Basement, Garage, Kitchen, Lot, Porch, Wood Deck, Year Built, etc), for houses built between 1872 and 2010, and their respective sale price.

|Variable|Meaning|Units|
|:----|:----|:----|
|1stFlrSF|First Floor square feet|334 - 4692|
|2ndFlrSF|Second floor square feet|0 - 2065|
|BedroomAbvGr|Bedrooms above grade (does NOT include basement bedrooms)|0 - 8|
|BsmtExposure|Refers to walkout or garden level walls|Gd: Good Exposure; Av: Average Exposure; Mn: Mimimum Exposure; No: No Exposure; None: No Basement|
|BsmtFinType1|Rating of basement finished area|GLQ: Good Living Quarters; ALQ: Average Living Quarters; BLQ: Below Average Living Quarters; Rec: Average Rec Room; LwQ: Low Quality; Unf: Unfinshed; None: No Basement|
|BsmtFinSF1|Type 1 finished square feet|0 - 5644|
|BsmtUnfSF|Unfinished square feet of basement area|0 - 2336|
|TotalBsmtSF|Total square feet of basement area|0 - 6110|
|GarageArea|Size of garage in square feet|0 - 1418|
|GarageFinish|Interior finish of the garage|Fin: Finished; RFn: Rough Finished; Unf: Unfinished; None: No Garage|
|GarageYrBlt|Year garage was built|1900 - 2010|
|GrLivArea|Above grade (ground) living area square feet|334 - 5642|
|KitchenQual|Kitchen quality|Ex: Excellent; Gd: Good; TA: Typical/Average; Fa: Fair; Po: Poor|
|LotArea| Lot size in square feet|1300 - 215245|
|LotFrontage| Linear feet of street connected to property|21 - 313|
|MasVnrArea|Masonry veneer area in square feet|0 - 1600|
|EnclosedPorch|Enclosed porch area in square feet|0 - 286|
|OpenPorchSF|Open porch area in square feet|0 - 547|
|OverallCond|Rates the overall condition of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|OverallQual|Rates the overall material and finish of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|WoodDeckSF|Wood deck area in square feet|0 - 736|
|YearBuilt|Original construction date|1872 - 2010|
|YearRemodAdd|Remodel date (same as construction date if no remodeling or additions)|1950 - 2010|
|SalePrice|Sale Price|34900 - 755000|


## Business Requirements
As a good friend, you are requested by your friend, who has received an inheritance from a deceased great-grandfather located in Ames, Iowa, to  help in maximizing the sales price for the inherited properties.

Although your friend has an excellent understanding of property prices in her own state and residential area, she fears that basing her estimates for property worth on her current knowledge might lead to inaccurate appraisals. What makes a house desirable and valuable where she comes from might not be the same in Ames, Iowa. She found a public dataset with house prices for Ames, Iowa, and will provide you with that


## Hypothesis and how to validate?
  * Hypothesis for the housing sale prices:
    * An evaluation of sales prices of other houses in the area based on attributes similar to attributes of each of the clients 4 inherited houses should provide a prediction of sales price for each house respectively.
    * The correlation analysis shows that the sizes of the ground floor living area, the first floor, the basement and the garage, play a key role in determining house price. In addition, the year the house was built and the overall quality of materials used and the finishes in the house also play a significant role in determining house price.


## Rationale to map the business requirements to the Data Visualizations and ML tasks
* List the business requirements and a rationale to map them to the Data Visualizations and ML tasks

* Business Requirement 1 - Data Visualisation and Correlation Study
  * As a client I want to inspect the data related to the house records, so that I can discover how the house attributes correlate with the sale price
  * As a client I want to conduct a correlation study (Pearson and Spearman) to better understand how the variables are correlated to Sale Price, so that I can discover how the house attributes correlate with the sale price
    * Correlation and/or PPS studies may be performed to investigate the most relevant variables correlated to the sale price.
  * As a client I want to plot the main variables against Sale Price to visualise insights, so that I can discover how the house attributes correlate with the sale price
    * Visualize these variables against the sale price and summarize the insights.

* Business Requirement 2
  * As a client I want to predict the sale price for a given house.
    * Build an ML Model, so that the client can predict the house sale prices for her 4 inherited houses, and any other house in Ames, Iowa.
  * Deliver an ML system that is capable of reliably predicting the summed sales price of the 4 inherited houses.
  * Use either conventional ML or Neural Networks to map the relationships between the features and the target.
  * Consider changing the ML task from Regression to Classification if you find a valid rationale for that.
  * If conventional ML is used for modelling, with packages like scikit-learn for example, conduct an extensive hyperparameter optimization for a given algorithm. 
    * Refer back to the Scikit-learn lesson, Unit Notebook 6: Cross-Validation Search Part 2.
      * At the end of the notebook, is a list of hyperparameter options and values to start with, for the family of algorithms covered in the course.

## ML Business Case

### Business Case Assessment

1. What are the business requirements?
   Business Requirement 1:
   * The client is interested in discovering how house attributes correlate with sale prices.
   * Therefore, the client expects data visualizations of the correlated variables against the sale price.
   Business Requirement 2:
   * The client is interested in predicting the house sale prices of her 4 inherited houses, and any other house in Ames, Iowa.
2. Is there any business requirement that can be answered with conventional data analysis?
  * Yes, we can use conventional data analysis to investigate how house attributes are correlated with the sale prices.
3. Does the client need a dashboard or an API endpoint?
  * The client needs a dashboard
4. What does the client consider as a successful project outcome?
  * A study showing the most relevant variables correlated to sale price.
  * Also, a capability to predict the sale price for the 4 inherited houses, as well as any other house in Ames, Iowa.
5. Can you break down the project into Epics and User Stories?
  * Information gathering and data collection. (DataCollection.ipynb)
  * Data visualization, cleaning, and preparation. (SalePriceStudy.ipynb) (DataCleaning.ipynb)
  * Model training, optimization and validation. (FeatureEngineering.ipynb) (ModelingAndEvaluation-PredictSalesPrice.ipynb)
  * Dashboard planning, designing, and development.
  * Dashboard deployment and release.
6. Ethical or Privacy concerns?
  * No. The client found a public dataset.
7. Does the data suggest a particular model?
  * The data suggests a regressor where the target is the sale price.
8. What are the model's inputs and intended outputs?
  * The inputs are house attribute information and the output is the predicted sale price.
9. What are the criteria for the performance goal of the predictions?
  * We agreed with the client an R2 score of at least 0.75 on the train set as well as on the test set.
10. How will the client benefit?
  * The client will maximize the sales price for the inherited properties.


## Dashboard Design

### Dashboard Expectations
The dashboard should contain:

* A project summary page, showing the project dataset summary and the client's requirements.
* A page listing the findings related to which features that have the strongest correlation to the house sale price.
* A page displaying the 4 houses' attributes and their respective predicted sale price.
  * It should display a message informing the summed predicted price for all 4 inherited houses.
  * Add interactive input widgets that allow a user to provide real-time house data to predict the sale price.
* A page indicating your project hypothesis(es) and how you validated it across the project.
* A technical page displaying your model performance. If you deployed an ML pipeline, you have to display your pipeline steps.

### Page 1: Quick project summary
* Quick project summary
	* Describe Project Dataset
	* State Business Requirements
  * Dataset Content Guidelines

### Page 2: House Sale Price Study
* Before the analysis, we knew we wanted this page to answer business requirement 1, but we couldn't know in advance which plots would need to be displayed.
* After data analysis, we agreed with stakeholders that the page will: 
	* State business requirement 1
	* Checkbox: data inspection on housing sale dataset
    * display the number of rows and columns in the data, and display the first ten rows of the data
	* Display the variables that bear the storngest correlation to sale price and the conclusions
	* Checkbox: Individual plots showing how sale price correlates to each variable 

### Page 3: Price Predictor
* State business requirement 2
* List the details of the inherited houses and their respective price predictions.
* Display the sum total of all the predicted house sale prices.
* A Set of widget inputs, which relate to house sales dataset.
  * All the features are available to the client for capturing attributes of the house for which they require a price prediction.
* "Run predictive analysis" button that serves the house data, provided by the client, to the ML pipelines, and predicts the sale price for the house and displays the result to the client.

### Page 4: Project Hypothesis and Validation
* Before the analysis, we knew we wanted this page to describe each project hypothesis, the conclusions, and how we validated each.
* After the data analysis, we can report that:
* 1 - An evaluation of sales prices of other houses in the area based on attributes similar to attributes of each of the clients 4 inherited houses should provide a prediction of sales price for each house respectively.
* 2 - The correlation analysis shows that the sizes of the ground floor living area, the first floor, the basement and the garage, play a key role in determining house price. In addition, the year the house was built and the overall quality of materials used and the finishes in the house also play a significant role in determining house price.

### Page 5: ML: House Sale Price Prediction
* Considerations and conclusions after the pipeline is trained
* Present ML pipeline steps
* Feature importance: List the features and plot the best features
* Pipeline performance evaluation: Show model evaluation and plots

## Unfixed Bugs
* No known bugs

## Deployment
### Heroku

* The App live link is: https://house-sales-price-predictor.herokuapp.com/ 
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly in case all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.


## Main Data Analysis and Machine Learning Libraries
* Here you should list the libraries you used in the project and provide example(s) on how you used these libraries.
* For example, if we consider the Churnometer project you may have listed that Seaborn is used to display a bar plot on the customer-based churn study to visualize churn levels. All libraries used in your project are listed in your requirements.txt file.


## Credits 

### Content 

- I used "https://github.com/Code-Institute-Solutions/milestone-project-heritage-housing-issues" as a repository template for this project
- The data source for this project is located [here](https://www.kaggle.com/datasets/codeinstitute/housing-prices-data)

### Media

- The photos used on the home and sign up page are from This Open Source site
- The images used for the gallery page were taken from this other open source site

### References
- This project was written based on the guidelines provided in the Customer Churn walk through project, data collection lesson.
  - Most of the functions used in this project were taken directly from the notebooks from the Customer Churn walk through project.
- Functions from the ML Feature Engine lesson have also been used in this project
- https://stackoverflow.com/
- https://pandas.pydata.org/
- https://numpy.org/

## Acknowledgements (optional)
- A big thanks to Code Institute team.
- Precious Ijege my project mentor
