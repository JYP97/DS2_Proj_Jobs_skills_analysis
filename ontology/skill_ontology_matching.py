import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
import numpy as np

class SkillOntologyMatcher:
    def __int__(self, input_skill):
        self.input_skill = input_skill
        self.esco = pd.read_csv('./esco.csv')
        print("=== esco loaded. ===")
        self.df_esco = pd.read_csv('./df_esco.csv', header=None).to_numpy()
        print("=== df_esco loaded. ===")
        self.esco_emb = pd.read_csv('./esco_emb', header=None).to_numpy()
        print("=== esco_emb loaded. ===")
        self.model = SentenceTransformer('bert-base-nli-mean-tokens')
        self.output = {} # key: skill, value: ontology

    def predict_level3_ontology(self):
        input_split = self.input_skill[0].split(',')
        input_df = pd.DataFrame(self.input_skill[0].split(','))
        split_embeddings = self.model.encode(input_split)

        for idx,skill in enumerate(split_embeddings):
            matched = np.argmax(cosine_similarity(skill, self.esco_emb))
            input_df.loc[idx, 'Level 3 Ontology'] = self.df_esco['skill'][matched]

        # for idx, ont in enumerate(input_df['Level 3 Ontology']):
        #     ontology_tree =





if __name__ == '__main__':


