Return = list(map(int, input().split(" ")))
expected = list(map(int, input().split(" ")))
fine = 0
# To handle case such as
# 9 6 2014
# 15 6 2015
if Return[2]<expected[2]:
    fine = 0
elif Return[2] == expected[2] :
    # To handle case such as
    # 25 3 2015
    # 15 6 2015
    if Return[1]<expected[1]:
        fine = 0
    elif  Return[1]==expected[1]:
        if Return[0]<=expected[0]:
            fine = 0
        else:
            fine = 15 * (Return[0] - expected[0])            
    else:
        fine = 500 * ( Return[1] - expected[1])
else:
    fine = 10000

print(fine)