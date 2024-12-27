n =  int(input())

def SuM(i):
    SuM = 0
    count = 0
    for j in range(1, i+1):
        if i%j == 0:
            SuM += j
            count += 1 
    return SuM, count 

sumOfAll = 0
totalCount = 0

for m in range(1,n+1):
    sumOf, count = SuM(m)
    sumOfAll += sumOf
    totalCount += count


print(totalCount)
print(sumOfAll)
