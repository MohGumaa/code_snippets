def collatz(n):
    if n % 2 == 0:
        n =  n // 2
        return n
    else:
        n = 3 * n + 1
        return n


# collatz(8)

# Ask user for Number
number = int(input('Please Enter Number:\n'))

# Continue Unit remeinder is equal to zero
while number > 1:
    number = collatz(number)
    print(number)

