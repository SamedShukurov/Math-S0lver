#30  
from math import *
#29
#faktorial
def f(n):
    if n<0:
        return abs(n)
    if n==0 or n==1:
        return 1
    else:
        return n*f(n-1)
def faktorial():
    n=int(input("ədəd daxil edin: "))   
    f(n)


