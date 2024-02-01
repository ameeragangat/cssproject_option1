#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 15:17:33 2024

@author: ameeragangat
"""

import pandas as pd

df = pd.read_csv('movie_dataset.csv')

print(df.info())

"""<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1000 entries, 0 to 999
Data columns (total 12 columns):
 #   Column              Non-Null Count  Dtype  
---  ------              --------------  -----  
 0   Rank                1000 non-null   int64  
 1   Title               1000 non-null   object 
 2   Genre               1000 non-null   object 
 3   Description         1000 non-null   object 
 4   Director            1000 non-null   object 
 5   Actors              1000 non-null   object 
 6   Year                1000 non-null   int64  
 7   Runtime (Minutes)   1000 non-null   int64  
 8   Rating              1000 non-null   float64
 9   Votes               1000 non-null   int64  
 10  Revenue (Millions)  872 non-null    float64
 11  Metascore           936 non-null    float64
dtypes: float64(3), int64(4), object(5)
memory usage: 93.9+ KB
"""

# Rename columns by replacing spaces with underscores
df.columns = df.columns.str.replace(' ', '_')

# Fill nan cells with a 0
df.fillna(0, inplace=True)
#%% QUESTION 1
highest_rated_movie = df.loc[df['Rating'].idxmax(), 'Title']
#%% QUESTION 2
avg_revenue = df['Revenue_(Millions)'].sum()/len(df)
#%% QUESTION 3
start_year = 2015
end_year = 2017

filtered_df = df[(df['Year'] >= start_year) & (df['Year'] <= end_year)]
avg_revenue = filtered_df['Revenue_(Millions)'].sum()/len(filtered_df)
#%% QUESTION 4
movies_2016 = df[df['Year'] == 2016]

movies_released_2016 = len(movies_2016)
#%% QUESTION 5 & 7
movies_nolan = df[df['Director'] == "Christopher Nolan"]

median_rating_nolan_movies = movies_nolan['Rating'].median()

movies_nolan_len = len(movies_nolan)
#%% QUESTION 6
movies_rating = df[df['Rating'] >= 8.0]

movies_rating_len = len(movies_rating)
#%% QUESTION 8
average_rating_by_year = df.groupby('Year')['Rating'].mean()

year_highest_average_rating = average_rating_by_year.idxmax()
#%% QUESTION 9
movies_2006 = df[df['Year'] == 2006]
movies_2016 = df[df['Year'] == 2016]

num_movies_2006 = len(movies_2006)
num_movies_2016 = len(movies_2016)

percentage_increase = ((num_movies_2016 - num_movies_2006) / num_movies_2006) * 100
#%% QUESTION 10
df['Actors'] = df['Actors'].str.split(', ')

most_common_actor = pd.Series(df['Actors'].sum()).mode()[0]
#%% QUESTION 11
genres_lists = df['Genre'].str.split(', ')

unique_genres = set(', '.join(genres_list) for genres_list in genres_lists)

num_unique_genres = len(unique_genres)
#%% QUESTION 12
corr_matrix = df.corr()















