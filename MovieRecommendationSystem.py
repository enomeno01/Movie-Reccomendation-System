#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 22:45:00 2023

@author: enesdemirpence
"""

import pandas as pd
from sklearn.metrics import pairwise_distances

movies = pd.read_csv("/Users/enesdemirpence/Downloads/ml-latest-small/movies.csv")
ratings = pd.read_csv("/Users/enesdemirpence/Downloads/ml-latest-small/ratings.csv")

df = pd.merge(movies, ratings, on="movieId")
df = df[["userId", "title", "rating"]]

pivot = df.pivot_table(index="title", columns="userId", values="rating", fill_value=0)

benzerlik_matrisi = pairwise_distances(pivot, metric="correlation")

indeksler = list(pivot.index)

film_adi = input("Benzerlik aramak istediğiniz film adını girin: ")
if film_adi in indeksler:
    film_indeks = indeksler.index(film_adi)
    benzer_indeksler = benzerlik_matrisi[film_indeks].argsort()[1:6]

    print(f"{film_adi} için benzer filmler:")
    for i in benzer_indeksler:
        print(indeksler[i])
else:
    print(f"{film_adi} adlı bir film bulunamadı.")
