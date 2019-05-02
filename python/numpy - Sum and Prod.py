import numpy
n,m = map(int,input().split())
mat = []
[mat.append(list(map(int,input().split()))) for i in range(n)]
mat = numpy.array(mat)
print(numpy.prod(numpy.sum(mat,axis=0)))
