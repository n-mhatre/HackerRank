# Enter your code here. Read input from STDIN. Print output to STDOUT
# take m,n
n,m = map(int,input().split())
#get array and store in dictionary format with count to
# save time and space for further computation
d = {}
for i in map(int,input().split()):
    if i in d:
        d[i] += 1
    else:
        d[i] = 1 


# get like and dislike array
like = set(map(int,input().split()))
dislike = set(map(int,input().split()))

result = 0
for i in d.keys():
    if i in like:
        result += d[i]
    elif i in dislike:
        result -= d[i]

print(result)
