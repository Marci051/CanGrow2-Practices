n = int(input())
c = 0
if 1 <= n <= 10**6:
    for i in range(1,n+1):
        if n % i == 0:
            c += 1
print(c)