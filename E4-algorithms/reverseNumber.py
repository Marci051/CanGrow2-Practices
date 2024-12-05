number = int(input("Yek adad vared konid: "))

reversed_number = 0

while number > 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number = number // 10

print(f"Maqloob adad: {reversed_number}")