# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 22:09:30 2021
@author: DELL
""" 
cot=int(input(" :"))
matrix = []
print("nhap so  :")
for i in range(1):
    a=[]
    for j in range(cot):
        a.append(int(input()))
    matrix.append(a)
for i in range (1):
    for j in range(cot):
        print(matrix[i][j], end = "")