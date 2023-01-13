import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
import numpy as np


class SkillOntologyMatcher:

    def __init__(self, input_skill):
        self.input_skill = input_skill
        self.esco = pd.read_csv('./esco.csv')
        print("=== esco loaded. ===")
        self.df_esco = pd.read_csv('./df_esco.csv')
        print("=== df_esco loaded. ===")
        self.esco_emb = pd.read_csv('./esco_emb.csv', header=None).to_numpy()
        print("=== esco_emb loaded. ===")
        self.model = SentenceTransformer('bert-base-nli-mean-tokens')
        self.output = {}  # key: skill, value: ontology

    def predict_ontology(self):
        input_split = self.input_skill[0].split(',')
        input_df = pd.DataFrame(self.input_skill[0].split(','))
        split_embeddings = self.model.encode(input_split)

        for idx, skill in enumerate(split_embeddings):
            matched = np.argmax(cosine_similarity(skill.reshape(1, -1), self.esco_emb))
            input_df.loc[idx, 'Level 3 Ontology'] = self.df_esco['skill'][matched]

        for idx, ont in enumerate(input_df['Level 3 Ontology']):
            ontology_tree = self.esco[self.esco['Level 3 preferred term'] == ont].values
            input_df.loc[idx, 'Level 2 Ontology'] = ontology_tree[0, 5]
            input_df.loc[idx, 'Level 1 Ontology'] = ontology_tree[0, 3]
            input_df.rename(columns={0: 'skills'})

        return input_df


if __name__ == '__main__':
    input_sk = ['c++, java, python']
    ontologyMatcher = SkillOntologyMatcher(input_sk).predict_ontology()
    for i, row in ontologyMatcher.iterrows():
        input_split = input_sk[0].split(',')
        print("Skill: ", input_split[i])
        print("Level 1 Ontology: ", row['Level 1 Ontology'], '\n')
        print("Level 2 Ontology: ", row['Level 2 Ontology'], '\n')
        print("Level 3 Ontology: ", row['Level 3 Ontology'], '\n')
