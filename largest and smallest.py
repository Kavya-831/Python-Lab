def find_largest_and_smallest(numbers):
    if len(numbers) == 0:
        return None, None  

    largest = numbers[0]
    smallest = numbers[0]

    for num in numbers[1:]:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num

    return largest, smallest


my_list = [4, 12, -5, 23, 0, 9]
largest, smallest = find_largest_and_smallest(my_list)
print("Largest number:", largest)
print("Smallest number:", smallest)
