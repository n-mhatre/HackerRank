# Enter your code here. Read input from STDIN. print output to STDOUT
n,m=map(int,input().split())
m= 3*n
mid = (n+1)//2
for i in range(1,mid):
    print(((".|.")*(i*2-1)).center(m,"-"))
print("WELCOME".center(m,"-"))
for i in range(mid-1,0,-1):
    print(((".|.")*(i*2-1)).center(m,"-"))