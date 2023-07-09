# SyntaxError
print("Hello, World!"

# TypeError
num1 = 10
num2 = '20'
sum = num1 + num2
print(sum)

# IndexError
numbers = [1, 2, 3]
print(numbers[3])

# ValueError
number = int('abc')
print(number)

# ZeroDivisionError
result = 10 / 0
print(result)

# FileNotFoundError
file = open('nonexistent_file.txt', 'r')


#user defined exception
class MyException(Exception):
    pass
def divide_numbers(a, b):
    if b == 0:
        raise MyException("Cannot divide by zero!")
    return a / b
try:
    result = divide_numbers(10, 0)
    print("Result:", result)
except MyException as e:
    print("Exception:", e)


#try except and finally block
def divide_numbers(a, b):
    try:
        result = a / b
        print("Result:", result)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    finally:
        print("Finally block executed.")
# Example 1: Division with non-zero denominator
divide_numbers(10, 2)
# Example 2: Division by zero
divide_numbers(10, 0)


#default except block
def divide_numbers(a, b):
    try:
        result = a / b
        print("Result:", result)
    except ValueError:
        print("Error: Invalid input!")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    except:
        print("Error: An exception occurred!")
# Example 1: Division with non-zero denominator
divide_numbers(10, 2)
# Example 2: Division by zero
divide_numbers(10, 0)
# Example 3: Invalid input
divide_numbers(10, 'abc')


#Multiple exceptions in single except block
def divide_numbers(a, b):
    try:
        result = a / b
        print("Result:", result)
    except (ValueError, ZeroDivisionError):
        print("Error: Invalid input or division by zero!")
    except:
        print("Error: An exception occurred!")
# Example 1: Division with non-zero denominator
divide_numbers(10, 2)
# Example 2: Division by zero
divide_numbers(10, 0)
# Example 3: Invalid input
divide_numbers(10, 'abc')
