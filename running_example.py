import random
import csv
import pickle
from collections import defaultdict

import sys
print(sys.path)

from Explanation_Models.ExpLOD import ExpLOD
from Explanation_Models.ExpLOD_KGE import ExpLOD_KGE

if __name__ == '__main__':

    # To run the example, you need to define:
    # - the input_dict, which is the user input (profile), keys are item IDs (see movies.csv in the Dataset folder), values are ratings (of a 1 to 10 scale)
    # - the recommender system used (recommender), which has to be one of the followings ('cbf', 'svd', 'hybrid')
    # - the explanation pattern used for the ExpLOD model (pattern), which has to be one of the two options ('basic', 'broader'), and
    # - the number of recommended items (nb_recs)


    # A running example
    input_dict = {'0319262': '10', '0454876': '10', '0120616':'8'}
    recommender = 'cbf'
    pattern = 'basic'
    nb_recs = 2

    # ExpLOD model
    exp_lod = ExpLOD(recommender=recommender,
                     exp_pattern=pattern,
                     input_dict=input_dict,
                     nb_rec=nb_recs
                     )
    print(exp_lod.exp_generator())


    # ExpLOD_KGE
    exp_kge = ExpLOD_KGE(recommender=recommender,
                     input_dict=input_dict,
                     nb_rec=nb_recs
                     )
    pattern_dict = exp_kge.exp_generator()
    print(pattern_dict)
