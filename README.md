# Data Science Exercies
This repository contains many csv files, Python scripts, and Python functions that have been created in order to explore the field of Data Science and Statistics.

## CSV Files
The `billboard_hot_100_all_years.csv` file was taken from [Kaggle](https://www.kaggle.com/datasets/dhruvildave/billboard-the-hot-100-songs). This is a very large file. I created a simple script called `get_billboard_hot_100_annual_data.py` which extracts data from the aforementioned csv file and saves it into individual csv files according to the year.

## Predicting Hiring Decisions in Recruitment Data   
The recruitment data can be found as a CSV file over [here](./predicting_hiring_decisions_in_recruitment_data/recruitment_data.csv). This data set was taken from Kaggle. The data in its raw form provides insights into factors influencing hiring decisions. Each record represents a candidate with various attributes considered during the hiring process. The goal is to predict whether a candidate will be hired based on these attributes:   

**Age**   
Data Range: 20 to 50 years   
Data Type: Integer   

**Gender**   
Categories: Male (0) or Female (1)   
Data Type: Binary   

**Education Level**   
Categories:   
1: Bachelor's (Type 1)   
2: Bachelor's (Type 2)   
3: Master's   
4: PhD   
Data Type: Categorical   

**Years of Experience**   
Data Range: 0 to 15 years   
Data Type: Integer   

**Number of Companies Previously Worked At**    
Data Range: 1 to 5 companies   
Data Type: Integer   

**Distance From Company (km)**   
Data Range: 1 to 50 kilometers.   
Data Type: Float (continuous).   

**Interview Score**   
Data Range: 0 to 100   
Data Type: Integer   

**Technical Skill Score**   
Data Range: 0 to 100   
Data Type: Integer   

**Personality Score**   
Data Range: 0 to 100   
Data Type: Integer   

**Recruitment Strategy**   
1: Aggressive   
2: Moderate   
3: Conservative   
Data Type: Categorical   

**Hiring Decision (Target Variable)**   
0: Not hired   
1: Hired   
Data Type: Binary (Integer)   

**Dataset Information**   
Records: 1500   
Features: 10   
Target Variable: HiringDecision (Binary)   

This data set provides us with an opportunity to _play around_ with various statistical and machine learning models.