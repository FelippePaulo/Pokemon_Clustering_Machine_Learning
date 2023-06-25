# -*- coding: utf-8 -*-
"""
Created on 25 jun 11:50:41 2023

@author: Felippe
"""

############### Configuracao ###################
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering

################ Clusterização ####################

from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering
import numpy as np

hc = AgglomerativeClustering(n_clusters = 3, affinity = 'euclidean', linkage = 'ward')
previsoes = hc.fit_predict(previsores)

lista_clientes = np.column_stack((previsores,previsoes))
lista_clientes = lista_clientes[lista_clientes[:,12].argsort()]

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
variavel2 = 'type1'

plt.scatter(baseOriginal.loc[previsoes == 0, variavel1],baseOriginal.loc[previsoes == 0, variavel2],s=100,c='blue',label='Cluster 0')
plt.scatter(baseOriginal.loc[previsoes == 1, variavel1],baseOriginal.loc[previsoes == 1, variavel2],s=100,c='red',label='Cluster 1')
plt.scatter(baseOriginal.loc[previsoes == 2, variavel1],baseOriginal.loc[previsoes == 2, variavel2],s=100,c='orange',label='Cluster 2')
plt.scatter(baseOriginal.loc[previsoes == 3, variavel1],baseOriginal.loc[previsoes == 3, variavel2],s=100,c='green',label='Cluster 3')
plt.scatter(baseOriginal.loc[previsoes == 4, variavel1],baseOriginal.loc[previsoes == 4, variavel2],s=100,c='purple',label='Cluster 4')
plt.scatter(baseOriginal.loc[previsoes == 5, variavel1],baseOriginal.loc[previsoes == 5, variavel2],s=100,c='brown',label='Cluster 5')
plt.scatter(baseOriginal.loc[previsoes == 6, variavel1],baseOriginal.loc[previsoes == 6, variavel2],s=100,c='pink',label='Cluster 6')
plt.scatter(baseOriginal.loc[previsoes == 7, variavel1],baseOriginal.loc[previsoes == 7, variavel2],s=100,c='gray',label='Cluster 7')
plt.scatter(baseOriginal.loc[previsoes == 8, variavel1],baseOriginal.loc[previsoes == 8, variavel2],s=100,c='olive',label='Cluster 8')
plt.scatter(baseOriginal.loc[previsoes == 9, variavel1],baseOriginal.loc[previsoes == 9, variavel2],s=100,c='teal',label='Cluster 9')
plt.scatter(baseOriginal.loc[previsoes == 10, variavel1],baseOriginal.loc[previsoes == 10, variavel2],s=100,c='navy',label='Cluster 10')
plt.scatter(baseOriginal.loc[previsoes == 11, variavel1],baseOriginal.loc[previsoes == 11, variavel2],s=100,c='pink',label='Cluster 11')
plt.scatter(baseOriginal.loc[previsoes == 12, variavel1],baseOriginal.loc[previsoes == 12, variavel2],s=100,c='purple',label='Cluster 12')
plt.scatter(baseOriginal.loc[previsoes == 13, variavel1],baseOriginal.loc[previsoes == 13, variavel2],s=100,c='red',label='Cluster 13')
plt.scatter(baseOriginal.loc[previsoes == 14, variavel1],baseOriginal.loc[previsoes == 14, variavel2],s=100,c='orange',label='Cluster 14')
plt.scatter(baseOriginal.loc[previsoes == 15, variavel1],baseOriginal.loc[previsoes == 15, variavel2],s=100,c='green',label='Cluster 15')
plt.scatter(baseOriginal.loc[previsoes == 16, variavel1],baseOriginal.loc[previsoes == 16, variavel2],s=100,c='blue',label='Cluster 16')
plt.scatter(baseOriginal.loc[previsoes == 17, variavel1],baseOriginal.loc[previsoes == 17, variavel2],s=100,c='navy',label='Cluster 17')
plt.scatter(baseOriginal.loc[previsoes == 18, variavel1],baseOriginal.loc[previsoes == 18, variavel2],s=100,c='olive',label='Cluster 18')
plt.scatter(baseOriginal.loc[previsoes == 19, variavel1],baseOriginal.loc[previsoes == 19, variavel2],s=100,c='green',label='Cluster 19')
plt.scatter(baseOriginal.loc[previsoes == 20, variavel1],baseOriginal.loc[previsoes == 20, variavel2],s=100,c='blue',label='Cluster 20')

plt.xlabel(variavel1)
plt.ylabel(variavel2)



# # Criacao de variaveis para investigar padrao
# baseOriginal['BILL_TOTAL'] = baseOriginal['BILL_AMT1'] + baseOriginal['BILL_AMT2'] + baseOriginal['BILL_AMT3'] + baseOriginal['BILL_AMT4'] + baseOriginal['BILL_AMT5'] + baseOriginal['BILL_AMT6']
# baseOriginal['PAY_TOTAL'] = baseOriginal['PAY_AMT1'] + baseOriginal['PAY_AMT2'] + baseOriginal['PAY_AMT3'] + baseOriginal['PAY_AMT4'] + baseOriginal['PAY_AMT5'] + baseOriginal['PAY_AMT6']

# plt.scatter(baseOriginal.loc[previsoes == 1, 'BILL_TOTAL'],baseOriginal.loc[previsoes == 1, 'PAY_TOTAL'],s=100,c='orange',label='Cluster 1')
# plt.scatter(baseOriginal.loc[previsoes == 2, 'BILL_TOTAL'],baseOriginal.loc[previsoes == 2, 'PAY_TOTAL'],s=100,c='red',label='Cluster 2')
# plt.scatter(baseOriginal.loc[previsoes == 0, 'BILL_TOTAL'],baseOriginal.loc[previsoes == 0, 'PAY_TOTAL'],s=100,c='green',label='Cluster 0')
# plt.scatter(baseOriginal.loc[previsoes == 3, 'BILL_TOTAL'],baseOriginal.loc[previsoes == 3, 'PAY_TOTAL'],s=100,c='blue',label='Cluster 3')

# plt.xlabel('Fatura total')
# plt.ylabel('Pagamento total')

#################################################3

baseOriginal['Cluster'] = previsoes
total_por_grupo = baseOriginal.groupby('Cluster').count().rename(columns={'total': 'total'}).total