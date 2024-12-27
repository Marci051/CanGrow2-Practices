n = int(input())
average = 0
for i in range(n):
    score = int(input())
    if score >= 0 and score <= 20:
        average += score
    else:
        print('enter a number between 0 and 20.')

print(average, average/n)