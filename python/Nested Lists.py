if __name__ == '__main__':
    students = []
    scores = []
    ans=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
        scores.append(score)
    m = min(scores)
    min_score = min(i for i in scores if i>m)
    for i in students:
        if i[1]==min_score:
            ans.append(i[0])
    ans.sort()
    print(ans)
        
