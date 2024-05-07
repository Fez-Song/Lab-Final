def calculate_factorial(num):
    factorial = 1
    if num < 0:
        print("Sorry, there is no factorial for negative numbers")
    elif num == 0:
        print("the factorial of 0 is 1")
    else:
        for i in range(1, num + 1):
            factorial = factorial * i
        print(f"the factorial of {num} is {factorial}")


number = int(input("Enter a number: "))
print(calculate_factorial(number))

print("the factorial of each number from 1 to 5:")
for num in range(1, 6):
    print(calculate_factorial(num))