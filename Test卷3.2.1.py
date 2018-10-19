from functools import reduce

def f(N,A,B):
    return print (reduce(lambda a,x:a+1 if x in A else a-1 if x in B else a,N,0))
