# import packages
import pandas as pd
from collections import Counter
import itertools


# function to calculate skill popularity
def skill_pop(job_titles, PATH):
    df = pd.read_csv(PATH)
    matching_skills = []
    for index, item in enumerate(job_titles):
        for title in df['title']:
            if item == title:
                matching_skills.append(df['skills'][index])
    # skill splitting
    skills = []
    for description in matching_skills:
        skill_list = description.split(', ')
        skills.append(skill_list)
    # list flattening
    flat_list = list(itertools.chain(*skills))

    # implement Counter: return counts and labels
    count = Counter(flat_list)
    most_10 = count.most_common(5)
    # counts_10 = []
    # labels_10 = []
    # for item in most_10:
    #     counts_10.append(item[1])
    #     labels_10.append(item[0])

    return most_10

if __name__ == "__main__":
    job_titles = ['Project Engineer', 'HR Coordinator', 'Program Manager I', 'VP Sr Technology Recruiter', 'Data Engineer', 'Machine Adjuster Trainee']
    PATH = '/Users/shuoyang/Desktop/BERT/combined_file.csv'
    res = skill_pop(job_titles, PATH)
    print(res)