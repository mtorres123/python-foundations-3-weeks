from asyncio.windows_events import NULL
from email.errors import InvalidBase64CharactersDefect
from tkinter import EXCEPTION


n = 5
try:
    int(n)  # raises ValueError
    print('Success!')  # doesn't print
except ValueError as e:
    print("Fail!")  # prints
    print(e)  # captured exception


# print('Got here')

# int('1.5')  # Run fails with exit code 1
# print("Didn't get here")  # doesn't print

num = 'hello'
# inverse = None
try:
    inverse = 1 / num
except (ZeroDivisionError):
    # pass
    inverse = 'not defined'
    # print(f'Cannot divide by {num}')
# except TypeError:
#     inverse = 'not defined'
#     print(f'{num} is not a number')
except Exception as e:
    inverse = 'unknown'
    print(f'New exception: {repr(e)}')
else: # runs after "try" finishes without errors
    print('Success!')
finally: # runs after everything, even if error caught
    # good for handling files (e.g., always want to close a file)
    print(f'The inverse of {num} is {inverse}.')

# print(f'The inverse of {num} is {inverse}.')


def cubed(n):
    if not isinstance(n, (int,float)):
        raise ValueError(f'n must be a number, but got {repr(n)}')
    return n ** 3

cubed(5)