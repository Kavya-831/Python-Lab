def find_duplicates(lst):
    duplicates = []
    seen = []

    for item in lst:
        if item in seen:
            if item not in duplicates:
                duplicates.append(item)
        else:
            seen.append(item)
    
    return duplicates


my_list = [4, 2, 7, 4, 3, 2, 8, 7, 9]
duplicates = find_duplicates(my_list)

if duplicates:
    print("Duplicate values:", duplicates)
else:
    print("No duplicates found.")
