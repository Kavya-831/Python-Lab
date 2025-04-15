def print_report(name, grade):
    print(f"Student: {name}")
    print(f"Final Grade: {grade}")

def main():
    name = input("Enter student's name: ")
    grade = input("Enter student's grade (A-F): ")
    print_report(name, grade)

if __name__ == "__main__":
    main()
