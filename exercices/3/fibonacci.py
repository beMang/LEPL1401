def fibonacci(n):
    first_number = 0
    second_number = 1
    i = 0
    while i != n:  # Le dernier sera ce chiffre - 1
        i += 1
        first = second_number
        second = first_number + second_number
        first_number = first
        second_number = second

    return first_number
