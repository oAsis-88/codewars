def sum_two_smallest_numbers(numbers):
        return numbers.pop(numbers.index(min(numbers))) + numbers.pop(numbers.index(min(numbers)))


print(sum_two_smallest_numbers([5, 8, 12, 18, 22]))
