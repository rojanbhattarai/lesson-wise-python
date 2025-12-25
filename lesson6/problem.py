total = 0
n = int(input("How many numbers do you want to input? "))

numbers = []

for i in range(n):
    number = int(input("Enter the number: "))
    numbers.append(number)
    total = total + number   # add directly

print("Sum:", total)

