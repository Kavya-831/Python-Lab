def print_pyramid(n):
    for i in range(1, n + 1):
       
        for j in range(n - i):
            print(" ", end="")
        
        
        for k in range(2 * i - 1):
            print("*", end="")
        
        
        print()


n = int(input("Enter the number of rows: "))
print_pyramid(n)
