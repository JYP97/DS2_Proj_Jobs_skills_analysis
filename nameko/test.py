from nameko_http import api
import json
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
from skill_job_matching import SkillJobMatcher


class NamekoService:
    name = 'yyds'

    @api('POST', '/skill', cors_enabled=True)
    def skill(self, req):
        ''' input data has been decoded as 'request', please assign the output data to 'resp' '''

        request_str = req.data.decode('utf-8', errors='ignore')
        request = eval(request_str)['request']

        ''' check request data '''
        # print('print: == skill ==')
        # print(request)
        # print(type(request))
        # print('print: ----')

        ''' [your code] '''

        ''' test resp data '''
        resp = 's1,s2,s3,s4,s5,s6,s7,s8,s9,10'
        dict = {'request': request, 'response': resp}
        print(dict)

        return json.dumps({'response': resp})

    @api('POST', '/job', cors_enabled=True)
    def job(self, req):
        ''' input data has been decoded as 'request', please assign the output data to 'resp' '''

        request_str = req.data.decode('utf-8', errors='ignore')
        request = eval(request_str)['request']

        ''' check request data '''
        # print('print: == job ==')
        # print(request)
        # print(type(request))
        # print('print: ----')

        ''' [your code] '''

        if request['proficiency']:
            resp = SkillJobMatcher(request['user_input'], request['num_job_output']).method_a(['shuffle'])
        else:
            resp = SkillJobMatcher(request['user_input'], request['num_job_output']).method_b(['shuffle'])
        ''' test resp data '''
        # resp = 'j1,j2,j3,j4,j5'
        dict = {'request': request, 'response': resp}
        print(dict)

        return json.dumps({'response': resp})