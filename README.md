# project-Indranuj10

project-Indranuj10 created by GitHub Classroom
# HOUSE PRICE PREDICTION

The project is on predicting house prices using Boston Housing database from UCI Machine Learning Repository. 
The database has 13 features and 1 label. The features are as follows:

1. CRIM:      per capita crime rate by town
2. ZN:        proportion of residential land zoned for lots over 
             25,000 sq.ft.
3. INDUS:     proportion of non-retail business acres per town
4. CHAS:      Charles River dummy variable (= 1 if tract bounds 
             river; 0 otherwise)
5. NOX:       nitric oxides concentration (parts per 10 million)
6. RM:        average number of rooms per dwelling
7. AGE:       proportion of owner-occupied units built prior to 1940
8. DIS:       weighted distances to five Boston employment centres
9. RAD:       index of accessibility to radial highways
10. TAX:      full-value property-tax rate per $10,000
11. PTRATIO:  pupil-teacher ratio by town
12. B:        1000(Bk - 0.63)^2 where Bk is the proportion of blacks 
             by town
13. LSTAT:    % lower status of the population
14. MEDV:     Median value of owner-occupied homes in $1000's 

Firstly, the data was split into training and testing. Then I used randomforest regressor on entire feature space to predict the desired
output using cross-validation. Here my loss function that I was using is RMSE(root mean squared error). Next I performed some feature 
exploration methods like getting correlation matrix, GLM LASSO, Random Forest ranking and Recussive feature elimination algorithms to 
see redundancy in feature space(entire analysis is there in the python notebook). Later I added one d=feature at a time with ramdon forest as 
a regressor and finally reduced the feature space from 13 to 9 features. 

The final list of features was:'LSTAT','DIS ','NOX','RM ','CRIM','AGE ','PTRATIO','B ','TAX'.

In this project I have used libraries like: numpy,pandas,matplotlib,sklearn.pickle,flask.

I built the app using Flask and deployed it in Heroku platform. 

**APP DOCUMENTATION AND HOW TO USE**

1] GO TO: https://housing-pred.herokuapp.com/predict

2] ENTER ALL THE **9** FIELDS AS STATED IN THE INPUT DIAGLOG BOX

3] SEE THE OUTPUT BELOW THE **PREDICT BUTTON**

SIGNIFICANCE OF THIS APP: This can be used by real-estate investors to predict prices of houses and then invest in those houses which are undervalued by the market and hence make great profits in future.

**VIDEO PRESENTATION LINK:**
