# n = int(input())
# for i in range(1,n):
#     for a in range(1,i):
#         if i %
count = 0
def PrimeNum(num):
    count = 0
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            continue
        else:
            count += 1
    return count

print(PrimeNum(3))