num1 = int(input("adad aval ra vared konid: "))
num2 = int(input("adad dovom ra vared konid: "))

max = num1

if num2 > max:
    max = num2
else:
    max = num1

print(max)

# البته اگر بخوایم مقیاس پذیری مسئله رو در نظر بگیریم باید به صورت زیر باشه:

count = int(input("chand ta adad darid? "))
i = 0
numbers = []
while i <= count-1:
    number = int(input())
    numbers.append(number)
    i += 1

max_number = numbers[0]     
for num in numbers:
    if num > max_number:
        max_number = num

print(f"bozorgtarin adad: {max_number}")