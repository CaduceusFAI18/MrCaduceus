import pandas as pd


inputs_name  = ['demographic', 'examination', 'medications', 'diet', 'labs']

inputs_data = {}

for file_name in inputs_name:
    print(file_name)
    inputs_data[file_name] = pd.read_pickle('../data/preprocessed/removed_nan/' + file_name + '.pkl')
    print('shape: ', inputs_data[file_name].shape)
    print('n_unique_id: ', len(inputs_data[file_name]['SEQN'].unique()))


merged_data = inputs_data['demographic']

for name in inputs_name:
    if name != 'demographic':
        print('merged with ', name)
        merged_data = merged_data.merge(inputs_data[name], left_on='SEQN', right_on='SEQN', how = 'inner')
        print('shape: ', merged_data.shape)

print('merged_data shape: ', merged_data.shape)
pd.to_pickle(merged_data, '../data/preprocessed/merged/mergedX.pkl')
