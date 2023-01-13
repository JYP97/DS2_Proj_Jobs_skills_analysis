# import packages
import pandas as pd
from collections import Counter
import itertools


# function to calculate skill popularity
def skill_pop(cat, PATH):
    df = pd.read_csv(PATH)
    cat_matching_skills = []
    for index, item in enumerate(df['job_category']):
        if item == cat:
            cat_matching_skills.append(df['skills'][index])
    # skill splitting
    skills = []
    for description in cat_matching_skills:
        skill_list = description.split(', ')
        skills.append(skill_list)
    # list flattening
    flat_list = list(itertools.chain(*skills))

    # implement Counter: return counts and labels
    count = Counter(flat_list)
    most_10 = count.most_common(10)
    counts_10 = []
    labels_10 = []
    for item in most_10:
        counts_10.append(item[1])
        labels_10.append(item[0])
    return labels_10
