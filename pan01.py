#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
# http://nbviewer.jupyter.org/urls/bitbucket.org/hrojas/learn-pandas/raw/master/lessons/01%20-%20Lesson.ipynb
import matplotlib.pyplot as plt
import pandas as pd #this is how I usually import pandas
import sys #only needed to determine Python version number
import matplotlib #only needed to determine Matplotlib version number


names = ['Bob','Jessica','Mary','John','Mel']
births = [968, 155, 77, 578, 973]

names = ['Bob','Jessica','Mary','John','Mel']
births = [968, 155, 77, 578, 973]

BabyDataSet = list(zip(names,births))
print BabyDataSet

df = pd.DataFrame(data = BabyDataSet, columns=['Names', 'Births'])
print df


df.to_csv('births1880.csv',index=False,header=False)
Location = r'/home/santosg/python/births1880.csv'
df = pd.read_csv(Location)

print df

