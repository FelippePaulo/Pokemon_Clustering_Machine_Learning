# -*- coding: utf-8 -*-
"""
Created on 25 jun 11:50:41 2020

@author: Felippe
"""

############### Configuracao ###################

##Aplicando o elbow method
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


################ Clusterização ####################

from sklearn.cluster import KMeans
import numpy as np

kmeans = KMeans(n_clusters = 3, random_state = 0)
previsoes = kmeans.fit_predict(previsores)

lista_pokemons = np.column_stack((previsores,previsoes))
lista_pokemons = lista_pokemons[lista_pokemons[:,10].argsort()]

############### Plotando grupos com k = 4 ####################

baseOriginal = pd.read_csv('Pokemon.csv')
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

plt.scatter(baseOriginal.loc[previsoes == 0, variavel1],baseOriginal.loc[previsoes == 0, variavel2],s=50,c='blue',label='Cluster 0')
plt.scatter(baseOriginal.loc[previsoes == 1, variavel1],baseOriginal.loc[previsoes == 1, variavel2],s=50,c='red',label='Cluster 1')
plt.scatter(baseOriginal.loc[previsoes == 2, variavel1],baseOriginal.loc[previsoes == 2, variavel2],s=50,c='orange',label='Cluster 2')
plt.scatter(baseOriginal.loc[previsoes == 3, variavel1],baseOriginal.loc[previsoes == 3, variavel2],s=50,c='green',label='Cluster 3')
plt.xlabel(variavel1)
plt.ylabel(variavel2)



############### Plotando grupos com k = 8 ####################

# plt.scatter(baseOriginal.loc[previsoes == 0, 'total'],baseOriginal.loc[previsoes == 0, 'type1'],s=50,c='blue',label='Cluster 0')
# plt.scatter(baseOriginal.loc[previsoes == 1, 'total'],baseOriginal.loc[previsoes == 1, 'type1'],s=50,c='red',label='Cluster 1')
# plt.scatter(baseOriginal.loc[previsoes == 2, 'total'],baseOriginal.loc[previsoes == 2, 'type1'],s=50,c='orange',label='Cluster 2')
# plt.scatter(baseOriginal.loc[previsoes == 3, 'total'],baseOriginal.loc[previsoes == 3, 'type1'],s=50,c='green',label='Cluster 3')
# plt.scatter(baseOriginal.loc[previsoes == 4, 'total'],baseOriginal.loc[previsoes == 4, 'type1'],s=50,c='purple',label='Cluster 4')
# plt.scatter(baseOriginal.loc[previsoes == 5, 'total'],baseOriginal.loc[previsoes == 5, 'type1'],s=50,c='yellow',label='Cluster 5')
# plt.scatter(baseOriginal.loc[previsoes == 6, 'total'],baseOriginal.loc[previsoes == 6, 'type1'],s=50,c='brown',label='Cluster 6')
# plt.scatter(baseOriginal.loc[previsoes == 7, 'total'],baseOriginal.loc[previsoes == 7, 'type1'],s=50,c='black',label='Cluster 7')
# plt.xlabel('total')
# plt.ylabel('tipo 1')



# Criacao de variaveis para investigar padrao
# baseOriginal['BILL_TOTAL'] = baseOriginal['BILL_AMT1'] + baseOriginal['BILL_AMT2'] + baseOriginal['BILL_AMT3'] + baseOriginal['BILL_AMT4'] + baseOriginal['BILL_AMT5'] + baseOriginal['BILL_AMT6']
# baseOriginal['PAY_TOTAL'] = baseOriginal['PAY_AMT1'] + baseOriginal['PAY_AMT2'] + baseOriginal['PAY_AMT3'] + baseOriginal['PAY_AMT4'] + baseOriginal['PAY_AMT5'] + baseOriginal['PAY_AMT6']

# plt.scatter(baseOriginal.loc[previsoes == 2, 'BILL_TOTAL'],baseOriginal.loc[previsoes == 2, 'PAY_TOTAL'],s=50,c='orange',label='Cluster 2')
# plt.scatter(baseOriginal.loc[previsoes == 0, 'BILL_TOTAL'],baseOriginal.loc[previsoes == 0, 'PAY_TOTAL'],s=50,c='blue',label='Cluster 0')
# plt.scatter(baseOriginal.loc[previsoes == 3, 'BILL_TOTAL'],baseOriginal.loc[previsoes == 3, 'PAY_TOTAL'],s=50,c='green',label='Cluster 3')
# plt.scatter(baseOriginal.loc[previsoes == 1, 'BILL_TOTAL'],baseOriginal.loc[previsoes == 1, 'PAY_TOTAL'],s=50,c='red',label='Cluster 1')

# plt.xlabel('Fatura total')
# plt.ylabel('Pagamento total')

#################################################3

baseOriginal['Cluster'] = previsoes
total_por_grupo = baseOriginal.groupby('Cluster').count().rename(columns={'total': 'total'}).total

