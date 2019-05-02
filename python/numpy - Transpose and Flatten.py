import numpy
mat=[]
n,m = map(int,input().split())
[mat.append(list(map(int,input().split()))) for i in range(n)]
arr = numpy.array(mat)
print(arr.transpose())
print(arr.flatten())