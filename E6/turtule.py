def canConvert(number):
    if len(number) % 2 == 0:
        if number.count('0') % 2 == 1:
            return 'You can!'
        else:
            return "You can't :("
    else:
        if number.count('0') % 2 == 0:
            return 'You can!'
        else:
            return "You can't :("

n = input('enter the number made by 0s and 1s: \n')
result = canConvert(n)
print(f"Result: {result}")
