import numpy
numpy.set_printoptions(sign=' ')
mat=[]
n,m = map(int,input().split())
[mat.append(list(map(int,input().split()))) for i in range(n)]
arr = numpy.array(mat)
print(numpy.mean(arr,axis = 1))
print(numpy.var(arr,axis = 0))
print(round((numpy.std(arr)), 11))