# -*- coding: utf-8 -*-

from random import random
import numpy as np
from time import time
from pyspark import SparkContext,SparkConf
from operator import add
import math

conf = SparkConf().setAppName("pi_estimator")\
        .setMaster("local")
sc = SparkContext(conf=conf)

def is_point_inside_unit_circle(p):
    x = random()
    y = random()
    return 1 if x*x+y*y<1 else 0

def pi_estimator_spark(n):
    t = time()
    count = sc.parallelize(range(0, n))\
            .map(is_point_inside_unit_circle)\
            .reduce(add)
    pi = count/n*4
    t_tot = np.round(time()-t,2)
    return pi,t_tot

def pi_estimator_numpy(n):
    t = time()
    n_in = 0
    for i in range (n):
        pt = is_point_inside_unit_circle(0)
        if pt == 1 :
            n_in += 1
    pi = 4*n_in/n  
    t_tot = np.round(time()-t,2)
    return pi,t_tot


n = 100000

(pi_spark,t_spark) = pi_estimator_spark(n)
ecart_spark = np.abs(np.round(100-(pi_spark/math.pi)*100,2))
(pi_np,t_np) = pi_estimator_numpy(n)
ecart_np = np.abs(np.round(100-(pi_np/math.pi)*100,2))

print("")
print("")
print("")
print("  Nombre de points : ",n)
print("")
print("  Spark : ")
print("  Approximation de pi avec spark : ",pi_spark)
print("  Temps de calcul estime avec spark : ",t_spark)
print("  Ecart entre pi et le pi estime avec spark : ",ecart_spark,"%")
print("")
print("  Numpy : ")
print("  Approximation de pi avec numpy : ",pi_np)
print("  Temps de calcul estime avec numpy : ",t_np)
print("  Ecart entre pi et le pi estime avec numpy : ",ecart_np,"%")
print("")
print("")
print("")

sc.stop()
