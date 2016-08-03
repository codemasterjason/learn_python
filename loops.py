for i in range(0, 10):
    for j in range(0, 10):
        print(i, ' ', j)

x = 0
while x != 5:
    x = int(input("Guess a number: "))
    if x != 5:
        print("Incorrect number!\n")

print("Correct!")