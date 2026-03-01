def total_sum(*numbers):
    total = 0
    for num in numbers:
        total += num
    print("Sum:", total)

total_sum(10, 20, 30)