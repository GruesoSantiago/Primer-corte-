#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Program: odd_even.py
# Description: This module separates a list of integers into two lists (odd, even)
# Author: Diego Fernando Marin
n = int(input("Digite el numero N:"))
m = int(input("Digite el numero M:"))
suma = 0 
p=0
if n > m:
	print("N debe ser mayor que M")
else: 
	for x in range(n,m+1):
		suma+= x**2 + 2*6
	print (suma)