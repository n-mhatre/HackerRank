from collections import Counter
input()
profit = 0
data = Counter( map(int,input().split()))
for _ in range(int(input())):
	size, price = map(int, input().split())
	if (data.get(size) != 0) and (size in data.keys()):
		data[size] -= 1
		profit += price

print(profit)