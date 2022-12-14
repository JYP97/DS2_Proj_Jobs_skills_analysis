# Data Preprocessing

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# Feature Scaling
from sklearn.preprocessing import StandardScaler
# Splitting the dataset into Training Set and Test set
from sklearn.cross_validation import train_test_split

# Importing the dataset
dataset = pd.read_csv('dataset_jobskills.csv')
X =  # Independent Variables
y =   # Dependent Variables

X_train,X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=0)
