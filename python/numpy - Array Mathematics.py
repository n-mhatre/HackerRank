import numpy
n,m = map(int,input().split())
array_1 = []
array_2 = []
[array_1.append(list(map(int,input().split()))) for i in range(n)]
[array_2.append(list(map(int,input().split()))) for i in range(n)]
array_1 = numpy.array(array_1)
array_2 = numpy.array(array_2)
print(array_1 + array_2)
print(array_1 - array_2)
print(array_1 * array_2)
print(array_1 // array_2)
print(array_1 % array_2)
print(array_1 ** array_2)