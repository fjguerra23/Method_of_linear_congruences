# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 14:57:49 2018

@author: Javier Guerra
"""

from random import randint
x=randint(0,9999999999)
m=2**32
a=22695477
c=1   
rng_value = (a*x + c) % m  #MLC method for random number
x=rng_value  #MLC random number memory that will use for the next gama
print(x)