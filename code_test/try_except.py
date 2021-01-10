def divideZero(number):
    try:
        return 42/number
    except Exception as e:
        return e

print(divideZero(0))
