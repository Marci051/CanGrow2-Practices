a = int(input())
b = int(input())
if a > 1 and b < 20:
    if b >= a: 
        print("Wrong order!")
    if (a - b)%2 != 0:
        print("Wrong difference!")
    else:
        for i in range(a):
            for j in range(a):
                if b <= i < a - b and b <= j < a - b:
                    print(" ", end="") 
                else:
                    print("*", end="")
            print() 
        
