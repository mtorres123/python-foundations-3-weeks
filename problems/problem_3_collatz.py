"""
Collatz sequence:
    - Starting at a number, n
    - If n is even, divide it by 2
    - If n is odd, multiply it by 3 and add 1
    - Repeat the process until you reach 1

Print the Collatz sequence for each number from 1 to 100.
"""


# Todo: determine next number in sequence
def next_num(n):
    # pass
    if n % 2 == 0:
        return(int(n/2))
    else:
        return(int(n**3+1))


# Todo: print the Collatz sequence for a given number
def collatz(num):
    # pass
    col_seq = [num]
    while num != 1:
        num = next_num(num)
        col_seq.append(num)
    print(col_seq)


# Todo: print the Collatz sequence for each number from 1 - 100
# n = range(1,101)
for n in range(1,5):
    collatz(n)