# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 13:28:51 2023

@author: felip
"""
##Aplicando o elbow method
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

wcss = []
for i in range(1,25):
    kmeans = KMeans(n_clusters = i, random_state = 0)
    kmeans.fit(previsores)
    wcss.append(kmeans.inertia_)
plt.plot(range(1,25), wcss)
plt.xlabel('Número de clusters')
plt.ylabel('WCSS')

