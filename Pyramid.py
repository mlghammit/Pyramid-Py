def print_pyramid(rows):
    for i in range(1, rows + 1):
        #print spaces
        print(" " * (rows - i), end="")
        #print stars
        print("*" * (2 * i - 1))

num_rows = int(input("Enter the number of rows for the pyramid: "))
print_pyramid(num_rows)
