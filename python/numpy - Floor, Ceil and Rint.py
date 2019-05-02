import numpy
numpy.set_printoptions(sign=' ')
arr = numpy.array((list(map(float,input().split()))), dtype=float)
print(numpy.floor(arr))
print(numpy.ceil(arr))
print(numpy.rint(arr))