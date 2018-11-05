import pandas as pd

input_files_name  = ['X', 'Y']

input_data = {}

for file_name in input_files_name:
    print(file_name)
    input_data[file_name] = pd.read_csv('../data/preprocessed/' + file_name + '.csv')

n_nan = 0

for column in input_data['X']:
    n_nan + input_data['X'].isna().sum()

print(n_nan)