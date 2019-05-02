#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
totalNumberOfSwaps = 0
for j in range(n):
    numberOfSwaps = 0
    for i in range(n-1):
        if a[i]>a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
            numberOfSwaps += 1
    totalNumberOfSwaps += numberOfSwaps

    if numberOfSwaps == 0:
        break
print("Array is sorted in {} swaps. ".format(totalNumberOfSwaps))
print("First Element: {}".format(a[0]))
print("Last Element: {}".format(a[-1]))