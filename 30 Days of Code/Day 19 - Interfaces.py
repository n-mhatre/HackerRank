class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    # Here i just want to go from 1 - n/2 element
    # so that i can reduce time complexity.
    def divisorSum(self, n):
        l = []
        # if single no. present then return 1
        if n==1:
            l.append(1)
            return 1

        # if more no. present consider n=6
        # than go through 1-3 only
        for i in range(1, ((n//2)+1) ):
            if n%i == 0:
                # To ensure no. is not in list
                if i not in l:
                    l.append(i)
                    # second no. not in list that add it in list
                    # in case n=4,  when i=4, n//i also 4
                    # To remove duplicate value we use this condition.
                    if n//i not in l:
                        l.append(n//i)
        return sum(l)

    """
    You can also use simple one:

    def divisorSum(self, n):
        result = 0
        for i in range(n):
            if n % i == 0:
                result += i
        return sum

    """

n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)               