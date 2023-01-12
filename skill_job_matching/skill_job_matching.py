from transformers import BertTokenizer, BertForSequenceClassification
import torch
import numpy as np
from itertools import chain
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import random
import collections
import math


class SkillJobMatcher:
    '''

    input example: ['physical training', 'body shaping', 'nutrition knowledge']
    '''
    def __init__(self, input_skills, num_job_pred):

        self.tokenizer = BertTokenizer.from_pretrained('bert-base-uncased', do_lower_case=True)
        print("=== BERT base tokenizer loaded. ===")

        self.fine_tuned_model = BertForSequenceClassification.from_pretrained("./acc_models_0.51_0.49_warmup100_2e-5_666",
                                                                              num_labels=8)
        print("=== Fine-tuned model loaded. ===")

        self.sbert_model = SentenceTransformer('bert-base-nli-mean-tokens')
        print("=== Sentence BERT loaded. ===")

        self.job_df = pd.read_csv('./clean_dataset_1794.csv', index_col=0).reset_index(drop=True)
        print("=== Job dataset loaded. ===")

        self.job_emb = np.array(pd.read_csv('./job_emb.csv', header=None).to_numpy())
        print("=== Pre-calculated job skill embeddings loaded. ===")

        self.input_skills = input_skills
        self.weight_exp = 7
        self.num_job_pred = num_job_pred
        self.confidence = {}
        self.output_job_a = []
        self.output_job_b = []

    def weights(self):
        weights = []
        for i in range(len(self.input_skills[0].split(','))):
            weights.append(math.exp(self.weight_exp))
            self.weight_exp -= 0.6
        return weights

    def pred_category(self):
        encodings = self.tokenizer.encode_plus(
            self.input_skills[0],
            # None,
            add_special_tokens=True,
            max_length=512,  # Pad & truncate all sentences.
            pad_to_max_length=True,
            truncation=True,
            return_attention_mask=True,  # Construct attn. masks.
            return_tensors='pt',
        )

        # Define labels
        labels = ['Managers',
                  'Professionals',
                  'Service and sales workers',
                  'Plant and machine operators and assemblers',
                  'Craft and related trades workers',
                  'Technicians and associate professionals',
                  'Clerical support workers',
                  'Elementary occupations']

        self.fine_tuned_model.eval()

        # Evaluate fine-tuned model with input skill and output label index with the highest possibility
        with torch.no_grad():
            input_ids = encodings.input_ids
            attention_mask = encodings.attention_mask
            token_type_ids = encodings.token_type_ids
            output = self.fine_tuned_model(input_ids, attention_mask, token_type_ids)
            final_output = torch.sigmoid(output.logits).cpu().detach().numpy().tolist()
            # print(int(np.argmax(final_output, axis=1)))

        # Get output labels
        probabilities = list(chain.from_iterable(final_output))
        predictions = dict(zip(labels, probabilities))
        pred_label = max(predictions, key=predictions.get)

        return pred_label

    def method_a(self, shuffle):
        input_skills_split = self.input_skills[0].split(',')
        item_weight = self.weights()
        pred_label = self.pred_category()
        input_embeddings = self.sbert_model.encode(input_skills_split)  # (# of input skills, 768)
        jobs_idx = list(self.job_df[self.job_df['job category'] == pred_label].index)
        for idx in jobs_idx:
            cos_sum = 0
            for i_skill, skill in enumerate(input_embeddings):
                cos = cosine_similarity(skill.reshape(1, -1), self.job_emb[idx].reshape(1, -1)).reshape(-1, )
                cos_sum += cos * item_weight[i_skill]
            self.confidence[idx] = cos_sum

        sorted_confidence = sorted(self.confidence.items(), key=lambda x: x[1], reverse=True)

        for item in sorted_confidence[0:self.num_job_pred]:
            self.output_job_a.append(self.job_df['title'][item[0]])

        if shuffle:
            random.shuffle(self.output_job_a)

        return self.output_job_a

    def method_b(self, shuffle):
        input_skills_join = self.input_skills
        pred_label = self.pred_category()
        input_embeddings = self.sbert_model.encode(input_skills_join)
        idx = list(self.job_df[self.job_df['job category'] == pred_label].index)
        cos = cosine_similarity(input_embeddings.reshape(1, -1), self.job_emb[idx]).reshape(-1, )
        match_dict = collections.defaultdict(list)

        for key, value in zip(idx, cos):
            match_dict[key].append(value)

        sorted_match_dict = sorted(match_dict.items(), key=lambda x: x[1], reverse=True)

        for idx in sorted_match_dict[:self.num_job_pred]:
            self.output_job_b.append(self.job_df['title'][idx[0]])

        if shuffle:
            random.shuffle(self.output_job_b)
        return self.output_job_b


def main(user_input, num_job_output, proficiency=False, shuffle=False):
    if proficiency:
        output_list = SkillJobMatcher(user_input, num_job_output).method_a(shuffle)
    else:
        output_list = SkillJobMatcher(user_input, num_job_output).method_b(shuffle)

    return output_list


if __name__ == '__main__':
    user_input = ['c++, java, python']

    output_proficiency = main(user_input, 10, True)
    output_wo_proficiency = main(user_input, 10)

    print("Input skills, split with comma: \n", user_input, "\n")
    print("Result with proficiency order: \n", output_proficiency, "\n")
    print("Result without proficiency order: \n", output_wo_proficiency)

