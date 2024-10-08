
'''
String format in Python
Completed
100 XP
3 minutes
Besides transforming text and performing basic operations, such as matching and searching, it's essential to format the text when you're presenting information. The simplest way to present text information with Python is to use the print() function. You'll find it critical to get information in variables and other data structures into strings that print() can use.

In this unit, you'll learn several valid ways to include variable values in text by using Python.

Percent sign (%) formatting
The placeholder for the variable in the string is %s. After the string, use another % character followed by the variable name. The following example shows how to format by using the % character:

Python

Copy
mass_percentage = "1/6"
print("On the Moon, you would weigh about %s of your weight on Earth." % mass_percentage)
Output: On the Moon, you would weigh about 1/6 of your weight on Earth.

Using multiple values changes the syntax, because it requires parentheses to surround the variables that are passed in:

Python

Copy
print("""Both sides of the %s get the same amount of sunlight, but only one side is seen from %s because the %s rotates around its own axis when it orbits %s.""" % ("Moon", "Earth", "Moon", "Earth"))
Output: Both sides of the Moon get the same amount of sunlight, but only one side is seen from Earth because the Moon rotates around its own axis when it orbits Earth.

 Tip

Although this method is still a valid way to format strings, it can lead to errors and decreased clarity in code when you're dealing with multiple variables. Either of the other two formatting options described in this unit would be better suited to this purpose.

The format() method
The .format() method uses braces ({}) as placeholders within a string, and it uses variable assignment for replacing text.

Python

Copy
mass_percentage = "1/6"
print("On the Moon, you would weigh about {} of your weight on Earth.".format(mass_percentage))
Output: On the Moon, you would weigh about 1/6 of your weight on Earth.

You don't need to assign repeated variables multiple times, making it less verbose because fewer variables need to be assigned:

Python

Copy
mass_percentage = "1/6"
print("""You are lighter on the {0}, because on the {0} you would weigh about {1} of your weight on Earth.""".format("Moon", mass_percentage))
Output: You are lighter on the Moon, because on the Moon you would weigh about 1/6 of your weight on Earth.

Instead of empty braces, the substitution is to use numbers. The {0} means to use the first (index of zero) argument to .format(), which in this case is Moon. For simple repetition {0} works well, but it reduces readability. To improve readability, use keyword arguments in .format() and then reference the same arguments within braces:

Python

Copy
mass_percentage = "1/6"
print("""You are lighter on the {moon}, because on the {moon} you would weigh about {mass} of your weight on Earth.""".format(moon="Moon", mass=mass_percentage))
Output: You are lighter on the Moon, because on the Moon you would weigh about 1/6 of your weight on Earth.

About f-strings
As of Python version 3.6, it's possible to use f-strings. These strings look like templates and use the variable names from your code. Using f-strings in the preceding example would look like this:

Python

Copy
print(f"On the Moon, you would weigh about {mass_percentage} of your weight on Earth.")
Output: On the Moon, you would weigh about 1/6 of your weight on Earth.

The variables go within braces, and the string must use the f prefix.

Aside from f-strings being less verbose than any other formatting option, it's possible to use expressions within the braces. These expressions can be functions or direct operations. For example, if you want to represent the 1/6 value as a percentage with one decimal place, you can use the round() function directly:

Python

Copy
print(round(100/6, 1))
Output: 16.7

With f-strings, you don't need to assign a value to a variable beforehand:

Python

Copy
print(f"On the Moon, you would weigh about {round(100/6, 1)}% of your weight on Earth.")
Output: On the Moon, you would weigh about 16.7% of your weight on Earth.

Using an expression doesn't require a function call. Any of the string methods are valid as well. For example, the string could enforce a specific casing for creating a heading:

Python

Copy
subject = "interesting facts about the moon"
heading = f"{subject.title()}"
print(heading)
Output: Interesting Facts About The Moon

'''

mass_percentage = "1/6"
print("On the Moon, you would weigh about %s of your weight on Earth." % mass_percentage)

print("""Both sides of the %s get the same amount of sunlight, but only one side is seen from %s because the %s rotates around its own axis when it orbits %s."""
       % ("Moon", "Earth", "Moon", "Earth"))

print("On the Moon, you would weigh about {} of your weight on Earth.".format(mass_percentage))

print("""You are lighter on the {0}, because on the {0} you would weigh about {1} of your weight on Earth.""".format("Moon", mass_percentage))

print("""You are lighter on the {moon}, because on the {moon} you would weigh about {mass} of your weight on Earth.""".format(moon="Moon", mass=mass_percentage))

print(f"On the Moon, you would weigh about {mass_percentage} of your weight on Earth.")

print(f"On the Moon, you would weigh about {round(100/6, 1)}% of your weight on Earth.")


print (""" TOPIC has become an integral part of the rising debate in the present world. While proponents of the argument are in favour,
       the opponents are considerably against the relevance of TOPIC.
       From my perspective,TOPIC-KEYWORDS have more positive impacts than negatives around the globe. 
       To commence with, there is a plethora of arguments in favour of my belief.
       The most prominent one is that POSITIVIE OA.
       According to research conducted by the University of California, EXAMPLE1. Secondly, POSITIVE OA. 
       On the other hand, critics may argue that one of the most significant disadvantages of the TOPIC-KEYWORDS is that NEGATIVE OD. 
       As an illustration, a survey conducted in the United States revealed that EXAMPLE2. 
       To conclude, even when there are a lot of demerit points associated with the TOPIC, the advantages outweigh the drawbacks.
       Moreover, TOPIC has become a pivotal part of our lives. Therefore, efficient use of TOPIC should be promoted. However, its misuse should be condemned.""")

topic = input ("What is the Topic:  ")



