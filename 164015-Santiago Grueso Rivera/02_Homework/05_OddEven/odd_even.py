#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Program: odd_even.py
# Description: Este programa ordena listas de numeros pares e impares
# Author: Santiago Grueso Rivera

def odd_even(numbers):
    
    
    numbers = list(numbers)
    
    print (numbers)
    
    
    lista_pares = []
    lista_impares = []

    
    jj = (len(numbers))

    for i in range(jj):
        if (int(numbers[i])) % 2 == 0:
            lista_pares.append(numbers[i])   
        else:
             lista_impares.append(numbers[i])      
        
    
    return lista_impares, lista_pares

def main():
    """ Main Program """
    numbers= ((input("enter a list of numbers (separated by spaces): ")).split())
    # TODO: convert the string "1 2 3 4 5" into a list [1, 2, 3, 4, 5]
    (odds, evens) = odd_even(numbers)
    print("{} = {} and {}".format(numbers, odds, evens))

if __name__ == "__main__":
    main()


