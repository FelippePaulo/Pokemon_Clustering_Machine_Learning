# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 11:50:41 2020

@author: marco
"""

############### Configuracao ###################



################ Clusterização ####################

from sklearn.cluster import DBSCAN
import numpy as np

dbscan = DBSCAN(eps = 3.0, min_samples = 50)
previsoes = dbscan.fit_predict(previsores)

lista_pokemon = np.column_stack((previsores,previsoes))
lista_pokemon = lista_pokemon[lista_pokemon[:,12].argsort()]

############### Plotando grupos ####################
import matplotlib.pyplot as plt
############### Plotando grupos ####################

baseOriginal = pd.read_csv('pokemon.csv')
baseOriginal = baseOriginal[cols_previsores]

#substitui espaços vazios da variavel type2 por "nao possui"
baseOriginal['type2'] = baseOriginal['type2'].fillna('nao possui')
# Filtrando os Pokémon cujos nomes começam com "Gigantamax" 
baseOriginal = baseOriginal[~baseOriginal['name'].str.startswith('Gigantamax')]
# retirando o pokemon eternamax eternatus pos ter um valor muito discrepante
baseOriginal = baseOriginal.drop(baseOriginal[baseOriginal['name'] == 'Eternamax Eternatus'].index)
# Resetando o índice do dataframe
baseOriginal.reset_index(drop=True, inplace=True)

# Criacao de variaveis para investigar padrao
baseOriginal['typeconjunto'] = baseOriginal['type1']
# Verifica se a coluna 'type2' é diferente de 'nao possui'
# e concatena o valor de 'type2' com 'typeconjunto'
baseOriginal.loc[baseOriginal['type2'] != 'nao possui', 'typeconjunto'] += '+' + baseOriginal['type2']


variavel1 = 'total'
variavel2 = 'typeconjunto'

plt.scatter(baseOriginal.loc[previsoes == -1, variavel1],baseOriginal.loc[previsoes == -1, variavel2],s=100,c='yellow',label='Cluster -1')
plt.scatter(baseOriginal.loc[previsoes == 0, variavel1],baseOriginal.loc[previsoes == 0, variavel2],s=100,c='blue',label='Cluster 0')
plt.scatter(baseOriginal.loc[previsoes == 1, variavel1],baseOriginal.loc[previsoes == 1, variavel2],s=100,c='red',label='Cluster 1')
plt.scatter(baseOriginal.loc[previsoes == 2, variavel1],baseOriginal.loc[previsoes == 2, variavel2],s=100,c='orange',label='Cluster 2')
plt.scatter(baseOriginal.loc[previsoes == 3, variavel1],baseOriginal.loc[previsoes == 3, variavel2],s=100,c='green',label='Cluster 3')
plt.scatter(baseOriginal.loc[previsoes == 4, variavel1],baseOriginal.loc[previsoes == 4, variavel2],s=100,c='purple',label='Cluster 4')
plt.xlabel(variavel1)
plt.ylabel(variavel2)


# Criacao de variaveis para investigar padrao
# baseOriginal['BILL_TOTAL'] = baseOriginal['BILL_AMT1'] + baseOriginal['BILL_AMT2'] + baseOriginal['BILL_AMT3'] + baseOriginal['BILL_AMT4'] + baseOriginal['BILL_AMT5'] + baseOriginal['BILL_AMT6']
# baseOriginal['PAY_TOTAL'] = baseOriginal['PAY_AMT1'] + baseOriginal['PAY_AMT2'] + baseOriginal['PAY_AMT3'] + baseOriginal['PAY_AMT4'] + baseOriginal['PAY_AMT5'] + baseOriginal['PAY_AMT6']

# plt.scatter(baseOriginal.loc[previsoes == -1, 'BILL_TOTAL'],baseOriginal.loc[previsoes == -1, 'PAY_TOTAL'],s=100,c='green',label='Cluster 3')
# plt.scatter(baseOriginal.loc[previsoes == 1, 'BILL_TOTAL'],baseOriginal.loc[previsoes == 1, 'PAY_TOTAL'],s=100,c='blue',label='Cluster 1')
# plt.scatter(baseOriginal.loc[previsoes == 0, 'BILL_TOTAL'],baseOriginal.loc[previsoes == 0, 'PAY_TOTAL'],s=100,c='orange',label='Cluster 0')
# plt.scatter(baseOriginal.loc[previsoes == 2, 'BILL_TOTAL'],baseOriginal.loc[previsoes == 2, 'PAY_TOTAL'],s=100,c='red',label='Cluster 2')

# plt.xlabel('Fatura total')
# plt.ylabel('Pagamento total')

#################################################3

baseOriginal['Cluster'] = previsoes
total_por_grupo = baseOriginal.groupby('Cluster').count().rename(columns={'total': 'total'}).total
