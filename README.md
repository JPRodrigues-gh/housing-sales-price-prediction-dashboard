## Dataset Content
* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/housing-prices-data). We created then a fictitious user story where predictive analytics can be applied in a real project in the workplace. 
* The dataset has almost 1.5 thousand rows and represents housing records from Ames, Iowa; indicating house profile (Floor Area, Basement, Garage, Kitchen, Lot, Porch, Wood Deck, Year Built) and its respective sale price for houses built between 1872 and 2010.

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

* 1 - The client is interested in discovering how the house attributes correlate with the sale price.
  * Therefore, the client expects data visualizations of the correlated variables against the sale price to show that.
* 2 - The client is interested in predicting the house sales price from her 4 inherited houses, and any other house in Ames, Iowa.


### Project Considerations
* A list your variables for the data-cleaning and feature-engineering steps. You may download the template in this [link](https://docs.google.com/spreadsheets/d/1pucuXPJM3UIaj6vb08NVanujpv0EcHol/edit#gid=733070095). 
* This file will not be assessed and it will not be as part of your final grade; it is just an auxiliary file you can use in your workflow. 
* In this file, you should list the names of the variables.


## Hypothesis and how to validate?
* List here your project hypothesis(es) and how you envision to validate it (them)
* In science, a hypothesis is an educated guess to explain something.
  * It must be testable in such a way that you could prove it false using a statistical test.
* In statistics, the goal is to see if observations are related.
  * Your hypothesis, in this case, is that two observations are equal. This is called the null hypothesis.  
  * A statistical test will either reject this null hypothesis or fail to reject it.
  * If the test rejects the null hypothesis then you assume there is a difference between your observations.
* In machine learning, a hypothesis is a model that approximates a function that maps the inputs to the outputs.
  * This is essentially the same as the conventional definition in that you are proposing that your inputs will give a particular prediction.
  * This model or hypothesis is then validated and tested in a very similar manner to a scientific or statistical hypothesis.  
  * If the model fails testing then you need to reframe your hypothesis in the light of this.
* So, let’s see how we will use a hypothesis in the course. A simple business problem might be:  
  * The webpage ‘contact us’ form is too long so prospective customers don’t finish it.   
  * The hypothesis is: 
    * By reducing the form inputs from 20 to 10 we will see an increase completed forms.
    * In this case it can be evaluated by a/b testing the 2 forms to see which form is completed by more people.  
    * This is a simple statistical data analysis where no change is the null hypothesis and
    * if there is a statistically significant increase in numbers with the new form then reject the null hypothesis. 
  * However, a more complex business problem like forecasting when a tool in a factory needs maintenance might well be answered by data collected by tool performance sensors and data on how worn out replaced components were.  
    * Your hypothesis might be that maintenance is required when a component is 90% worn out. 
    * To evaluate and test this hypothesis may require a Machine learning solution. 
    * In this case, a model trained on the data to predict exactly when is the best time to maintain a tool, would be how to evaluate and test the hypothesis.
  
  * Hypothesis for the housing prices:
    * An evaluation of sales prices of other houses in the area based on attributes similar to attributes of each of the clients 4 inherited houses should provide a prediction of sales price for each house respectively.
    * The correlation analysis shows that the sizes of the ground floor living area, the first floor, the basement and the garage, play a key role in determining house price. In addition, the year the house was built and the overall quality of materials used and the finishes in the house also play a significant role in determining house price.


## Rationale to map the business requirements to the Data Visualizations and ML tasks
* List your business requirements and a rationale to map them to the Data Visualizations and ML tasks
* Business Requirement 1 - Data Visualisation and Correlation Study
  * As a client I want to inspect the data related to the house records, so that I can discover how the house attributes correlate with the sale price
  * As a client I want to conduct a correlation study (Pearson and Spearman) to better understand how the variables are correlated to Sale Price, so that I can discover how the house attributes correlate with the sale price
    * You may perform a correlation and/or PPS study to investigate the most relevant variables correlated to the sale price.
  * As a client I want to plot the main variables against Sale Price to visualise insights, so that I can discover how the house attributes correlate with the  sale price
    * You have to visualize these variables against the sale price, so you can summarize the insights.
* Business Requirement 2
  * As a client I want to predict the sale price for a given house.
    * We want to build an ML Model, so that the client can predict the house sale prices from her 4 inherited houses, and any other house in Ames, Iowa.
  * You may deliver an ML system that is capable of reliably predicting the summed sales price of the 4 inherited houses.
  * You may use either conventional ML or Neural Networks to map the relationships between the features and the target.
  * You may consider changing the ML task from Regression to Classification if you find a valid rationale for that.
  * In case you are modelling using conventional ML, with packages like scikit-learn for example, you may conduct an extensive hyperparameter optimization for a given algorithm. 
    * You can refer back to the Scikit-learn lesson, Unit Notebook 6: Cross-Validation Search Part 2.
    *   At the end of the notebook, you will find a list of hyperparameter options and values to start with, for the family of algorithms we covered in the course.

## ML Business Case
* In the previous bullet, you potentially visualized a ML task to answer a business requirement. You should frame the business case using the method we covered in the course

### Business Case Assessment
You have already conducted a business case assessment, so you can also use that information to build your project README file.

1. What are the business requirements?
  * The client is interested in discovering how house attributes correlate with sale prices. Therefore, the client expects data visualizations of the correlated variables against the sale price.
  * The client is interested in predicting the house sale prices from her 4 inherited houses, and any other house in Ames, Iowa.
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
* List all dashboard pages and its content, either block of information or widgets, like: buttons, checkbox, image, or any other item that your dashboard library supports.
* Eventually, during the project development, you may revisit your dashboard plan to update a give feature (for example, in the beginning of the project you were confident you would use a given plot to display an insight but eventually you needed to use another plot type)

### Dashboard Expectations
The dashboard should contain:

* A project summary page, showing the project dataset summary and the client's requirements.
* A page listing your findings related to which features have the strongest correlation to the house sale price.
* A page displaying the 4 houses' attributes and their respective predicted sale price.
  * It should display a message informing the summed predicted price for all 4 inherited houses.
  * Add interactive input widgets that allow a user to provide real-time house data to predict the sale price.
* A page indicating your project hypothesis(es) and how you validated it across the project.
* A technical page displaying your model performance. If you deployed an ML pipeline, you have to display your pipeline steps.

### Page 1: Quick project summary
* Quick project summary
	* Project Terms & Jargon
	* Describe Project Dataset
	* State Business Requirements

### Page 2: Customer Base Churn Study
* Before the analysis, we knew we wanted this page to answer business requirement 1, but we couldn't know in advance which plots would need to be displayed.
* After data analysis, we agreed with stakeholders that the page will: 
	* State business requirement 1
	* Checkbox: data inspection on customer base (display the number of rows and columns in the data, and display the first ten rows of the data)
	* Display the most correlated variables to churn and the conclusions
	* Checkbox: Individual plots showing the churn levels for each correlated variable 
	* Checkbox: Parallel plot using Churn and correlated variables 

### Page 3: Prospect Churnometer
* State business requirement 2
* Set of widgets inputs, which relates to the prospect profile. Each set of inputs is related to a given ML task to predict prospect Churn, Tenure and Cluster.
* "Run predictive analysis" button that serves the prospect data to our ML pipelines, and predicts if the prospect will churn or not, if so, when. It also shows to which cluster the prospect belongs and the cluster's profile. For the churn and tenure predictions, the page will inform the associated probability for churning and for tenure level.

### Page 4: Project Hypothesis and Validation
* Before the analysis, we knew we wanted this page to describe each project hypothesis, the conclusions, and how we validated each. After the data analysis, we can report that:
* 1 - We suspect customers are churning with low tenure levels
	* Correct. The correlation study at Churned Customer Study supports that.
* 2 -  A customer survey showed our customers appreciate fibre Optic.
	* A churned user typically has Fiber Optic, as demonstrated by a Churned Customer Study. The insight will be taken to the survey team for further discussions and investigations.

### Page 5: Predict Property Sale Price
* Considerations and conclusions after the pipeline is trained
* Present ML pipeline steps
* Feature importance
* Pipeline performance

## Unfixed Bugs
* You will need to mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a big variable to consider, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.

## Fixed Bugs
* In data_collection.ipynb after unzipping the Kaggle dataset download I moved the csv dataset files to the raw directory.
  * As a result this notebook would not run hands free when attempting to access the dataset csv using pandas read.
  * Instead of adding a mv file command I decided to just stick to using the path to which the file unzipped. 

## Deployment
### Heroku

* The App live link is: https://YOUR_APP_NAME.herokuapp.com/ 
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

### Guidelines
- In this section you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism. 
- You can break the credits section up into Content and Media, depending on what you have included in your project. 

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
- A big thanks to Code Institutes' Fernando Doreto, Yoni Lavi, Niel Mc Ewen, Matt Rudge, Gyan Shashwat for the LMS material.
- Precious Ijege my project mentor
