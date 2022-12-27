import pandas as pd

data = pd.read_csv('signals.csv', sep=';', index_col=False)
data = data.set_index(['Signal'])
print('HEAD\n', data.head(), '\n')
print('TAIL\n', data.tail(), '\n')
print('THIRD LINE\n', data.iloc[2], '\n')
temp = data['Description']
print('DESCRIPTION\n', temp, '\n')
temp.to_csv('sliced_py.csv', sep=';')

