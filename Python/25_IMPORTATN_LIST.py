'''  The name of the
# Index
List items are changeable, meaning we can update individual items within a list.

But before we do that, how can we access an individual item within a list? Well, this is where index comes in!

An index is an item's position in a list.

Python is 0-indexed, meaning that the indices starts at 0:

vowels = ['a', 'e', 'i', 'o', 'u']
# Index:   0    1    2    3    4

The item at index 0 is 'a'.
The item at index 1 is 'e'.
The item at index 2 is 'i'.
The item at index 3 is 'o'.
The item at index 4 is 'u'.

To output each of the items, we can use the name[index] syntax:

print(vowels[0])     # Output: a
print(vowels[1])     # Output: e
print(vowels[2])     # Output: i
print(vowels[3])     # Output: o
print(vowels[4])     # Output: u

# Negative Index
Another thing to note about index is that it can be positive or negative.

If the index is negative, it starts from -1 (which is the last item of a list) and it goes backwards from there.


vowels = ['a', 'e', 'i', 'o', 'u']
# Index:   0    1    2    3    4
# Index:  -5   -4   -3   -2   -1


# Slicing
Is there a way to get more than just one individual item? Yep! It's called slicing.

Slicing is where we can access certain parts of a sequence.

Instead of accessing an item using a single index like name[index], we can get multiple items by specifying where to start and where to end the range like name[start : end].

For example:

vowels = ['a', 'e', 'i', 'o', 'u']

print(vowels[0 : 3])
print(vowels[1 : 3])

# Output:
# ['a', 'e', 'i']
# ['e', 'i']

'''
'''
vowels = ['a', 'e', 'i', 'o', 'u']


print(vowels[2]) #solo un index positiv
print(vowels[-4]) #solo un index negative
print(vowels[1 : 3]) # slicing positive
print(vowels[-5: -3])#slicing negative
print(vowels[8])#slicing negative

'''
'''
stock1_prices = [2.52, 2.44, 2.32, 2.41, 2.51, 2.50, 2.44]
stock2_prices = [8.36, 8.31, 8.21, 8.21, 8.25, 8.11, 8.13]

print(len(stock1_prices))      # Output: 7 cantidad de index
print(max(stock1_prices))      # Output: 2.52 
print(min(stock2_prices))      # Output: 8.11 https://docs.python.org/3/library/functions.html


# List Methods
Besides built-in functions, Python has a bunch of built-in list methods that are very handy.

Here are some of them:

.append() method adds an item to the end of the list.
.insert() method adds an item to a specific index.
.remove() method removes an item from a list based on the value.
.pop() method removes the item at a particular index.
Let's use DNA sequences as an example for this! 🧬

dna = ['AUG', 'AUC', 'UCG']

dna.append('UAA')     # ['AUG', 'AUC', 'UCG', 'UAA']
dna.insert(2, 'GAU')  # ['AUG', 'AUC', 'GAU', 'UCG', 'UAA']
dna.remove('AUC')     # ['AUG', 'GAU', 'UCG', 'UAA']
dna.pop(0)            # ['GAU', 'UCG', 'UAA']

The difference between built-in functions and methods on a list is that methods use the dot notation syntax on the list variable we create. Built-in functions can be called by themselves, but methods are always attached to a list variable from which they are being called.

Another notable difference is that while not all the built-in functions are defined to work with lists, the list methods only work with lists.

Here are all 11 list methods to save in your notes:

List Method	Description
.append()	Add an item to the end of the list
.clear()	Remove all items from the list
.copy()	Return a shallow copy of the list
.count()	Return the number of times the value appears in the list
.extend()	Appends another list to the current list by extending it
.index()	Returns the index of a value inside the list
.insert()	Insert an item at a specified position in the list
.pop()	Remove an item from a specified position in the list
.remove()	Remove an item from the list based on the value of the item
.reverse()	Reverses the list in place
.sort()	Sorts the list in place


'''






