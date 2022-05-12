for num in range(100, 1000, 1):

    c = num // 100
    d = (num % 100) // 10
    u = num % 10

    if (num % 2 == 0):
        result = c + d + u
    else:
        result = c * d * u

    print(f"{num} - {result}")



