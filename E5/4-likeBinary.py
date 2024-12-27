n = int(input())
i = 1
sum = 0
if n >= 1 and n <= 2**14:
    while i < n:
        if n%i == 0:
            sum += i
            i = i + 1
        else:
            i = i + 1
    if sum > 0 and (sum & (sum - 1)) == 0:
        print("1")
    else:
        print("0")


else:
    print('enter a number between 1 and 16384')



