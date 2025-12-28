def avg():
    total = 0
    for i in range(4):
        num = int(input("Enter your number: "))
        total = total + num

    print("Sum =", total)
    print("Average =", total / 4)

avg()
