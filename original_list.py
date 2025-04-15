def split_list(original_list, first_part_length):
    if first_part_length < 0 or first_part_length > len(original_list):
        return None, None  
    
    first_part = []
    second_part = []

    for i in range(len(original_list)):
        if i < first_part_length:
            first_part.append(original_list[i])
        else:
            second_part.append(original_list[i])
    
    return first_part, second_part


original_list = [1, 1, 2, 3, 4, 4, 5, 1]
first_part_length = 3

first, second = split_list(original_list, first_part_length)
print("Original list:", original_list)
print("Length of the first part of the list:", first_part_length)
print("Splitted the said list into two parts:", (first, second))
