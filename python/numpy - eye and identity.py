#submission code: (just because there is a bug in test case)

import numpy
print(str(numpy.eye(*map(int,input().split()))).replace('1',' 1').replace('0',' 0'))


#expected code:
# import numpy
# N, M = map(int, input().split())
# print (numpy.eye(N, M, k = 0))

