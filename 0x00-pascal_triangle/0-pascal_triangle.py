from math import factorial

# where n is the number of rows
def pascal_triangle(n):
    for i in range(n):
        # first loop for leading spaces
        for j in range(n - i + 1):
            print(end = " ")

        # second loop for row i elements
        for j in range(i + 1):
            # define factorial formula: nCr = n!/((n-r)!*r!)
            print(factorial(i)//(factorial(j)*factorial(i - j)), end = " ")

        # print each row in a new line
        print("\n")

# help(pascal_triangle)
# pascal_triangle(5)