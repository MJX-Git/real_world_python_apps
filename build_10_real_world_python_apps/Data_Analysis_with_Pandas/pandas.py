#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 17:25:40 2020

@author: mjx
"""

import pandas

df1 = pandas.DataFrame([[2,4,6],[10,20,30]])

df2 = pandas.DataFrame([[2,4,6],[10,20,30]], columns=['Price','Age','Value'])

df3 = pandas.DataFrame([[2,4,6],[10,20,30]], columns=['Price','Age','Value'], index=['first','second'])

df4 = pandas.DataFrame([{'Name':'John'},{'Name':'Jack'}])

df5 = pandas.DataFrame([{'Name':'John', 'Surname':'Johns'},{'Name':'Jack'}])

print(df2.mean())

print(df2.mean().mean())

print(df2.Price)

print(df2.Price.mean())

print(df2.Price.max())