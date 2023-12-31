import pandas as pd
arquivo = pd.read_csv('alimento.csv')
print(f'arquivo.info():\n {arquivo.info()}')
print()
print(f'arquivo.head():\n {arquivo.head()}')
print()
print(f'arquivo.tail():\n {arquivo.tail()}')
print()
print(f'arquivo.columns:\n {arquivo.columns}')
print()
print(f'arquivo.shape:\n {arquivo.shape}')
print()
print(f'arquivo.describe():\n {arquivo.describe()}')
print()
print(f'arquivo.sort_values(by="produto"):\n {arquivo.sort_values(by="produto")}')
print()
print(f'arquivo["produto"].value_counts():\n {arquivo["produto"].value_counts()}')
print()
print(f'arquivo.sort_values(by="region"):\n {arquivo.sort_values(by="regiao")}')