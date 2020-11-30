import random
import csv
import pickle
from collections import defaultdict
from Explanation_Models.ExpLOD import ExpLOD
from Explanation_Models.ExpLOD_KGE import ExpLOD_KGE

if __name__ == '__main__':
    with open('Eval_Samples/users_for_test.pickle', 'rb') as file:
        users_for_test = pickle.load(file)

    recommenders = ['cbf', 'svd', 'hybrid']
    patterns = ['basic', 'broader']
    nb_recs = [1, 2, 3, 4, 5]

    # ExpLOD
    with open('results_explod.csv', 'a') as result_file:
        fieldnames = ['algo', 'pattern', 'nb_rec', 'Exp_prec']
        writer = csv.DictWriter(result_file, fieldnames=fieldnames)
        writer.writeheader()

        for user, input_dict in users_for_test.items():
            # print(user)
            row_dict = {}
            for recommender in recommenders:
                for pattern in patterns:
                    for nb_rec in nb_recs:
                        exp_lod = ExpLOD(recommender=recommender,
                                         exp_pattern=pattern,
                                         input_dict=input_dict,
                                         nb_rec=nb_rec
                                         )
                        nb_explainable_items = len(exp_lod.exp_generator().keys())
                        ep = nb_explainable_items / nb_rec
                        row_dict['algo'] = recommender
                        row_dict['pattern'] = pattern
                        row_dict['nb_rec'] = nb_rec
                        row_dict['Exp_prec'] = ep
                        writer.writerow(row_dict)


    # ExpLOD_KGE
    with open('results_expLOD_KGE.csv', 'a') as result_file:
        fieldnames = ['algo', 'nb_rec', 'PEM', 'PEM+CEM']
        writer = csv.DictWriter(result_file, fieldnames=fieldnames)
        writer.writeheader()

        for user, input_dict in users_for_test.items():
            # print(user)
            row_dict = {}
            for recommender in recommenders:
                for nb_rec in nb_recs:
                    exp_kge = ExpLOD_KGE(recommender=recommender,
                                     input_dict=input_dict,
                                     nb_rec=nb_rec
                                     )
                    pattern_dict = exp_kge.exp_generator()
                    nb_explainable_items = len(pattern_dict.keys())
                    ep_hybrid = nb_explainable_items / nb_rec
                    ep_simple = len([key for key in pattern_dict.keys() if 'http' in key]) / nb_rec
                    row_dict['algo'] = recommender
                    row_dict['nb_rec'] = nb_rec
                    row_dict['PEM'] = ep_simple
                    row_dict['PEM_CEM'] = ep_hybrid
                    writer.writerow(row_dict)
