def reverse_traverse_with_index(lst):
    length = len(lst)
    for i in range(length - 1, -1, -1):
        print(f"Index {i}: {lst[i]}")


original_list = ['red', 'green', 'white', 'black']
print("Original list:", original_list)
print("Traverse the said list in reverse order with original indexes:")
reverse_traverse_with_index(original_list)
