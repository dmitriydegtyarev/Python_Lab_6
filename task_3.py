def fibonacci_numbers(limit):
    """Створює множину чисел Фібоначчі до `limit`."""
    fib = {0, 1}
    a, b = 0, 1
    while b <= limit:
        fib.add(b)
        a, b = b, a + b
    return fib

numbers = set(range(1, 51))

# Знаходимо числа Фібоначчі в множині
fib_numbers = numbers & fibonacci_numbers(50)

sorted_fib_list = sorted(fib_numbers)

print("Числа Фібоначчі:", sorted_fib_list)
print("Кількість чисел у послідовності:", len(fib_numbers))