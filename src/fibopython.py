def fibonacci_up_to(limit):  # generates the fibonacci sequence up to the limit
    fibonacci = [0, 1]
    for i in range(2, limit + 1):
        fibonacci.insert(i, fibonacci[-1] + fibonacci[-2])
        if fibonacci[i] > limit:
            del fibonacci[i]
            return fibonacci


def fibonacci_classic(numbers):  # generate the fibonacci sequence with x numbers
    fibonacci = [0, 1]
    for _ in range(2, numbers):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci


def fibonacci_ranged(start, stop):
    sequence = []
    fibonacci = fibonacci_up_to(stop)
    if start not in fibonacci_up_to(stop):
        valid_start = fibonacci[-1]
        print(
            f"{start} is not a valid fibonacci sequence number. Starting from {valid_start}"
        )
        for i in range(fibonacci.index(valid_start), len(fibonacci)):
            sequence.append(fibonacci[i])
    else:
        for i in range(fibonacci.index(start), len(fibonacci)):
            sequence.append(fibonacci[i])
    return sequence


print(f"Fibonacci Up To: {fibonacci_up_to(35)}")
print(f"Fibonacci Classic: {fibonacci_classic(15)}")
print(f"Fibonacci Ranged: {fibonacci_ranged(8,30)}")
