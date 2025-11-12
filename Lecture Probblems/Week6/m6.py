def fourbonacci(n):
    # Start with the first 4 values given in the problem
    numbers = [1, 4, 7, 8]

    # If n is 1–4, just return it directly
    if n <= 4:
        return numbers[n-1]


    for i in range(4, n):

        # F(N) = 4*F(N-4) + 3*F(N-3) + 2*F(N-2) + F(N-1)
        next_value = 4 * numbers[i-4] + 3 * numbers[i-3] + 2 * numbers[i-2] + numbers[i-1]
        numbers.append(next_value)

    # Return the nth
    return numbers[n-1]


def odd_squares(n):
    count = 0         # how many odd square
    num = 1
    while count < n:  # keep going until we have n numbers
        square = num * num
        print(square) # print the square
        count += 1    # one more odd square printed
        num += 2      # move to the next odd number (




def diamond(height):
    middle = (height // 2) + 1

    # this loop does the top half of the diamond  and middle
    for i in range(1, middle + 1):
        limit = (2 * i) - 1
        # how many spaces to put in front so it looks centered
        spaces = middle - i
        # print the spaces first
        print(" " * spaces, end="")
        for j in range(1, limit + 1):
            print(j, end="")
        # go to the next line when this row is done
        print()

    # bottom half of the diamond
    for i in range(middle - 1, 0, -1):
        limit = (2 * i) - 1
        spaces = middle - i
        print(" " * spaces, end="")
        for j in range(1, limit + 1):
            print(j, end="")
        print()

