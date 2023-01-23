# import packages
import pandas as pd
from collections import Counter
import itertools


# function to calculate skill popularity
def skill_pop(PATH):
    cats = ['Professionals', 'Technicians and associate professionals', 'Clerical support workers', 'Service and sales workers',
           'Skilled agricultural, forestry and fishery workers', 'Craft and related trades workers', 'Plant and machine operators and assemblers', 'Elementary occupations']
    df = pd.read_csv(PATH)
    most_10s = []
    for cat in cats:
        cat_matching_skills = []
        for index, item in enumerate(df['job category']):
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
        most_10s.append(most_10)
#     counts_10 = []
#     labels_10 = []
#     for item in most_10:
#         counts_10.append(item[1])
#         labels_10.append(item[0])

    return most_10s
if __name__ == "__main__":
    PATH = '/Users/shuoyang/Desktop/BERT/combined_file.csv'
    res = skill_pop(PATH)
    print(res)