def f(n):
    return print(' '.join([''.join(['%s' %(i) for i in range(1,j+1)])+''.join(['%s' %(i) for i in range(j-1,0,-1)]) for j in range(1,int(n+1))]))
