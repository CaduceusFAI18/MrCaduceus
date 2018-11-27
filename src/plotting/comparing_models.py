import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import RidgeClassifierCV
from sklearn import preprocessing

import warnings
warnings.filterwarnings('ignore')

x = pd.read_pickle('../../data/preprocessed/merged/mergedX.pkl')
### Load Y and merge with X
y = pd.read_csv('../../data/preprocessed/merged/Y.csv')
y = y.merge(x, how='right', on='SEQN').drop(columns=[column for column in list(x) if column != 'SEQN'])
y = y.drop(columns=['Unnamed: 0'])
y = y.applymap(lambda x: int(x))

###
diseases = list(y.columns.values)
diseases.remove('SEQN')
count = {}
for disease in diseases:
    count[disease] = y[disease].sum()
sorted_count = sorted(count.items(), key=lambda kv: kv[1], reverse=True)

other_disease = sorted_count[7:]
other_disease_count = sum([count[1] for count in other_disease])

common_diseases = sorted_count[:7]
common_disease_name = [cd[0] for cd in common_diseases]
y_most_common = y.loc[:, common_disease_name]


###
sensitive_variables = ['RIAGENDR', 'RIDAGEYR', 'RIDRETH1', 'RIDRETH3', 'DMQMILIZ', 'DMQADFC', 'DMDBORN4', 'DMDCITZN',
                       'DMDEDUC3', 'DMDEDUC2', 'DMDMARTL', 'RIDEXPRG', 'SIALANG', 'SIAINTRP', 'FIALANG', 'FIAINTRP',
                       'MIALANG', 'MIAINTRP', 'AIALANGA', 'DMDHRGND', 'DMDHRBR4', 'INDHHIN2', 'INDFMIN2', 'INDFMPIR']
age_and_gender_col_id = ['RIAGENDR', 'RIDAGEYR']

def encoding_string_labels(df):
    label_encoders = {}
    string_columns = df.select_dtypes(include=['object'])
    for column in string_columns:
        label_encoders[column] = preprocessing.LabelEncoder().fit(string_columns[column])
        df[column] = label_encoders[column].transform(string_columns[column])
    return df, label_encoders

x_encoded, x_encoding_labels = encoding_string_labels(x)

def compare_rf_model(data, labels, sensitive_vars):
    data_cleaned = data.drop(columns=sensitive_vars)
    scores = {}
    scores_cleaned = {}
    n_estimators = [5]
    max_depths = [50,75, 100]
    for n_estimator in n_estimators:
        for max_depth in max_depths:
            rfc = RandomForestClassifier(n_estimators=n_estimator, max_depth=max_depth, random_state=0, n_jobs=-1)
            scores[str(n_estimator) + ' ' + str(max_depth)] = cross_val_score(rfc, data[data.columns[1:]].as_matrix(),
                                                                              labels[labels.columns[1:]].as_matrix(),
                                                                              cv=5, scoring='f1_samples')
            scores_cleaned[str(n_estimator) + ' ' + str(max_depth)] = cross_val_score(rfc, data_cleaned[data_cleaned.columns[1:]].as_matrix(),
                                                                              labels[labels.columns[1:]].as_matrix(),
                                                                              cv=5, scoring='f1_samples')
    return scores, scores_cleaned

def compare_knn_model(data, labels, sensitive_vars):
    n_neighbors = [5]
    data_cleaned = data.drop(columns=sensitive_vars)
    scores = {}
    scores_cleaned = {}
    for n_neighbor in n_neighbors:
        knn = KNeighborsClassifier(n_neighbors=n_neighbor, n_jobs=-1)
        scores[n_neighbor] = cross_val_score(knn, data[data.columns[1:]].as_matrix(),
                                                 labels[labels.columns[1:]].as_matrix(), cv=10, scoring='f1_samples')
        scores_cleaned[n_neighbor] = cross_val_score(knn, data_cleaned[data_cleaned.columns[1:]].as_matrix(),
                                             labels[labels.columns[1:]].as_matrix(), cv=10, scoring='f1_samples')
    return scores, scores_cleaned


def compare_separate_classifier(data, labels, sensitive_vars):
    data_cleaned = data.drop(columns=sensitive_vars)
    scores = {}
    scores_cleaned = {}
    n_estimators = [5]
    max_depths = [50,75, 100]
    for n_estimator in n_estimators:
        for max_depth in max_depths:
            rfc = RandomForestClassifier(n_estimators=n_estimator, max_depth=max_depth, random_state=0, n_jobs=-1)
            scores[str(n_estimator) + ' ' + str(max_depth)] = cross_val_score(rfc, data[data.columns[1:]].as_matrix(),
                                                                              labels[labels.columns[1:]].as_matrix(),
                                                                              cv=5, scoring='f1_samples')
            scores_cleaned[str(n_estimator) + ' ' + str(max_depth)] = cross_val_score(rfc, data_cleaned[data_cleaned.columns[1:]].as_matrix(),
                                                                              labels[labels.columns[1:]].as_matrix(),
                                                                              cv=5, scoring='f1_samples')
    return scores, scores_cleaned

def max_scores(scores):
    scores_sorted = sorted(list(scores.values()), key=lambda folds_score: folds_score.mean())
    return scores_sorted[0].mean(), scores_sorted[0].std() * 2


# scores_rf, scores_rf_cleaned = compare_rf_model(x, y, age_and_gender_col_id)
# scores_knn, scores_knn_cleaned = compare_knn_model(x, y, age_and_gender_col_id)
#
# performance, error = zip(*[max_scores(scores_rf), max_scores(scores_rf_cleaned), max_scores(scores_knn), max_scores(scores_knn_cleaned)])
# model = ['RF', 'RF no age and gender', 'KNN', 'KNN no age and gender']
# colors = ['b', 'b', 'r', 'r']
# plt.rcParams.update({'font.size': 16})
# plt.xlabel('Model')
# plt.ylabel('F1 score')
# plt.errorbar(model, performance, error, linestyle='None', marker='^')
# plt.title('Models\' performance')
# plt.plot()
# plt.show()


scores_rf, scores_rf_cleaned = compare_rf_model(x, y, sensitive_variables)
scores_knn, scores_knn_cleaned = compare_knn_model(x, y, sensitive_variables)

performance, error = zip(*[max_scores(scores_rf), max_scores(scores_rf_cleaned), max_scores(scores_knn), max_scores(scores_knn_cleaned)])
model = ['RF', 'RF no law protected variables', 'KNN', 'KNN no law protected variables']
plt.rcParams.update({'font.size': 16})
plt.xlabel('Model')
plt.ylabel('F1 score')
plt.errorbar(model, performance, error, linestyle='None', marker='^')
plt.title('Models\' performance')
plt.plot()
plt.show()