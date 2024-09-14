'''
Use variable arguments in Python
Completed
100 XP
5 minutes
In Python, you can use any number of arguments and keyword arguments without declaring each one of them.
This ability is useful when a function might get an unknown number of inputs.

Variable arguments
Arguments in functions are required. But when you're using variable arguments, 
the function allows any number of arguments (including 0) to be passed in.
The syntax for using variable arguments is prefixing a single asterisk (*) before the argument's name.

The following function prints the received arguments:

'''
def sequence_time(*args):
    total_minutes = sum(args)
    if total_minutes < 60:
        return f"Total time to launch is {total_minutes} minutes"
    else:
        return f"Total time to launch is {total_minutes/60} hours"
    
print (sequence_time(4, 14, 18))

print (sequence_time(4, 14, 48))

#Variable keyword arguments
#For a function to accept any number of keyword arguments, you use a similar syntax. 
#In this case, a double asterisk is required:

def variable_length(**kwargs):
    print(f'{len(kwargs)} Astronauts assigned for this mission: ')
    for title, name in kwargs.items():
        print(f'{title}: {name}')

print (variable_length (captain="Neil Armstrong", pilot="Buzz Aldrin", command_pilot="Michael Collins"))





