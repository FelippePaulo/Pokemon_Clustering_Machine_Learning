# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 14:41:29 2023

@author: felip
"""

############### Configuracao ###################
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage


dendrograma = dendrogram(linkage(previsores, method = 'ward'))
plt.title("Dendrograma")
plt.xlabel('Registros')
plt.ylabel('Distancia Euclidiana')