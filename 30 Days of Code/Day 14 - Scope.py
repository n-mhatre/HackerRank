class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0
#
       
    def computeDifference(self):
        for  i in range(0, (len(self.__elements))):
            for j in range(1, len(self.__elements)):
                val = abs(self.__elements[i] - self.__elements[j])
                if val>self.maximumDifference:
                    self.maximumDifference = val
        return self.maximumDifference

#

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()
print(d.maximumDifference)        