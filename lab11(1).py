def group_names_by_first_letter(names):
    grouped = {}
    for name in names:
        first_letter = name[0].upper()  
        grouped.setdefault(first_letter, []).append(name)
    return grouped
names = ['Kavya', 'Heama', 'Divya', 'Priya', 'Keerthy', 'Vinod']
result = group_names_by_first_letter(names)
print(result)
