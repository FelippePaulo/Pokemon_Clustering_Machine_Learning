# -*- coding: utf-8 -*-
"""
Created on jun 25 11:41:40 2023

@author: Felippe
"""

import pandas as pd


################ Pré processamento ###############

# Leitura dos dados
base = pd.read_csv('Pokemon.csv')
descricao = base.describe()

# Pocurando valores inconsistentes
# type2 e inconsistente. 

# Separando dados que serão usados
cols_previsores = ["number","name","type1","type2","total", "hp","attack","defense","sp_attack","sp_defense","speed","generation","legendary"] 
previsores = base[cols_previsores]

#substitui espaços vazios da variavel type2 por "nao possui"
previsores['type2'] = previsores['type2'].fillna('nao possui')

# Filtrando os Pokémon cujos nomes começam com "Gigantamax" 
previsores = previsores[~previsores['name'].str.startswith('Gigantamax')]
# retirando o pokemon eternamax eternatus pos ter um valor muito discrepante
previsores = previsores.drop(previsores[previsores['name'] == 'Eternamax Eternatus'].index)
# Resetando o índice do dataframe
previsores.reset_index(drop=True, inplace=True)

#retirando a coluna nome e numer pois sao apenas identificadores
previsores = previsores.drop(columns=['name'])
previsores = previsores.drop(columns=['number'])

# Transforma variaveis categóricas em numéricas
from sklearn.preprocessing import LabelEncoder
labelencoder_previsores = LabelEncoder()
#previsores.loc[:, 'name'] = labelencoder_previsores.fit_transform(previsores.loc[:, 'name'])
previsores.loc[:, 'type1'] = labelencoder_previsores.fit_transform(previsores.loc[:, 'type1'])
previsores.loc[:, 'type2'] = labelencoder_previsores.fit_transform(previsores.loc[:, 'type2'])
previsores.loc[:, 'legendary'] = labelencoder_previsores.fit_transform(previsores.loc[:, 'legendary'])

# Criando variáveis dummy para categoricas nominais
from sklearn.preprocessing import LabelBinarizer
labelbinarizer = LabelBinarizer()

#variaveis dummy

from sklearn.preprocessing import LabelBinarizer

# Variável type1
labelbinarizer = LabelBinarizer()
variaveis_dummy = labelbinarizer.fit_transform(previsores['type1'])
novas_variaveis_dummy = [f"type1_{classe}" for classe in labelbinarizer.classes_]
df_variaveis_dummy = pd.DataFrame(variaveis_dummy, columns=novas_variaveis_dummy)
#substituindo na base
previsores = pd.concat([previsores, df_variaveis_dummy], axis=1)
previsores = previsores.drop('type1', axis=1)

# Variável type2
labelbinarizer = LabelBinarizer()
variaveis_dummy = labelbinarizer.fit_transform(previsores['type2'])
novas_variaveis_dummy = [f"type2_{classe}" for classe in labelbinarizer.classes_]
df_variaveis_dummy = pd.DataFrame(variaveis_dummy, columns=novas_variaveis_dummy)
#substituindo na base
previsores = pd.concat([previsores, df_variaveis_dummy], axis=1)
previsores = previsores.drop('type2', axis=1)



# Padronização dos dados
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
previsores = scaler.fit_transform(previsores)