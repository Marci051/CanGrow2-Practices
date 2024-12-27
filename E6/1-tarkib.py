def fact(a):
    sum = 1
    for z in range(1,a+1):
        sum *= z
    return sum    
    
def C(n,r):
    return (fact(n))/(fact(r)*fact(n-r))

m = int(input())
n = int(input())

if n > 0 and n <= 20 and m > 0 and m <= 20:
    if n <= m:
        print(int(C(m,n)))