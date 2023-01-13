import pandas as pd

# open files
f1 = pd.read_csv('/Users/shuoyang/Desktop/invalid_salary_dataset - invalid_salary_dataset.csv')
f2 = pd.read_csv('/Users/shuoyang/Desktop/valid_salary_dataset - valid_salary_dataset.csv')
file = [f1,f2]
train = pd.concat(file)

# output combined file
train.to_csv("/Users/shuoyang/Desktop/combined_file" + ".csv", index=True, sep=',')

