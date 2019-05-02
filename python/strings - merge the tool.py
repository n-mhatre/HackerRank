def merge_the_tools(s, k):
    # your code goes here
    for i in range(len(s)//k):
        t = ''
        for j in s[i * k : (i + 1) * k]:
            if j not in t:
                t+=j
        print(t)
    
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)