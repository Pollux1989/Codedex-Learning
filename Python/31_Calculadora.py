print("#####--------Calculator--------#####")
'''
# Return Value
We learned that functions can take in inputs, but did you know that functions can also have outputs? In fact, every Python function has an output!

The return keyword is used to terminate a function and output a value:

def function_name():
  # The code inside
  return value

When we don't add it, Python will implicitly return the default value, None, as the return value.

When we do want to be explicit:

def add(x, y):
  answer = x + y
  return answer

So a return keyword is added, plus the variable we want to output.

Now when we call the function, there will be an output that we can play with:

total = add(4.99, 9.99)   # total is 14.98

This means that we can actually print out a function call! 💡

print(add(3, 4))          # Same thing as print(7)
print(add(1, 5))          # Same thing as print(6)
print(add(5, 3))          # Same thing as print(8)

Here, the add() function is returning a value and that returned value is an argument for the print() function.

The output would be:

7
6
8

Note: When a return statement is reached, Python will stop the execution of the current function, sending a value out to where the function was called.

# Print vs. Return
Now you might wonder, why are we returning values instead of printing them?

Well, print() functions can be anywhere in the program — inside or outside of a function, whereas return is the output of a function; you don't need to print out whatever you are returning.

As a rule of thumb:

Use return in a function when you want to send value(s) from one point in the code to another.
Use print() in a function when you want to display some text to the user.
Instructions


'''
def suma(a,b):
    return a + b

def resta(a,b):
    return a - b

def multiplicacion (a, b):
    return a * b

def division (a,b) :
    return a / b

def exponente (a,b):
    return a ** b

print(suma(3,5))
print(resta(3, 5))
print(multiplicacion(7, 2))
print(division(4, 8))
print(exponente(9, 3))









"""
def calculator():
    print("Welcome to the Calculator!")
    print("Type 'Close' to exit")

    while True:
        operation = input ("Enter Operation (➕ ➖ ✖️  ➗) or 'close' to exit: ").strip()

        if operation.lower() == 'close':
            print("Thanks for using the Calculator, Goodbye! 👋")
            break
        if operation not in ['+', '-', '*', '/']:
            print('Invalid Operation. Please try again.')
            continue
        try:
            num1 = float(input('Enter first number: '))
            num2 = float(input('Enter second number: '))

            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 == 0:
                    print('Error: Division by Zero! 😂')
                    continue
                result = num1 / num2
            print(f"The result of {num1} {operation} {num2} = {result}")    
        
        except ValueError:
            print("Invalid input, Please Enter Numeric Values!!!")
calculator()                    

"""



