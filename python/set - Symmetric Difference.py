# Enter your code here. Read input from STDIN. Print output to STDOUT
input()
s1 = set(map(int, input().split(" ")))
input()
s2 = set(map(int, input().split(" ")))
ans = []
{ans.append(i) for i in s1-s2}
{ans.append(i) for i in s2-s1}
for i in sorted(ans):
    print(i,end="\n")