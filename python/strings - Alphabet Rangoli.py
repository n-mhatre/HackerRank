def print_rangoli(n):
    # your code goes here
    #print upper half trangle
    for i in range(1,n+1):
        part_printing(i)
    #print lower half trangle    
    for i in range(n-1,0,-1):
        part_printing(i)

def part_printing(i):
    s=""
    width = 4*n-3
    for j in range(i):
        s+= chr(96-j+n)
    s+=s[-2::-1]
    print("-".join(s).center(width,"-"))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)