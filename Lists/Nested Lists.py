# Nested Lists
# Nested Lists
"""
In Python, lists are a super useful data structure. They can hold multiple items that can be accessed via index and they can store a mix of data types. For example:

list = ['a', 'b', 'c', 1, 2, 3]

Another benefit is that lists can nest other lists!

A nested list is a list of lists. Yep, you read that right! It's called a nested list because one of the items is another list. For example:

list = ['a', 'b', 'c', [1, 2, 3]]

To access the value of a nested list, we use extra square brackets to select for the list:

print(list[3][1])

First, we select the fourth index (or [3]) of list, which holds the nested list. Then, we add a second pair of brackets to select the second index (or [1]) of the nested list. Put it together, and you have [3][1]!

So when will we ever use this? Nested lists come up a bunch in data structures & algorithms, interview questions, data science problems, and even some edge cases. For example, suppose some students are double majoring and retaking a test:

student1 = ['Jerry', ['CompSci', 'Math'], 2026]
student2 = ['Ellie', ['InfoSci', 'Game Design'], 2024]
student3 = ['Daniel', 'CompSci', 2028]

test_scores1 = [[760, 760, 780], 32]
test_scores2 = [745, 32]
test_scores3 = [720, [31, 33]]

# Matrix
If we create a list of items, and every item is a nested list of the same size, we get what is called a matrix or 2D list (2-dimensional list).

This is where nested lists become really handy:

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

This could also be formatted as:

matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12]]

Or even:

matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10, 11, 12]
]

Imagine you are building a Tic-Tac-Toe game and you want to have a board layout:

board = [
  ['x', ' ', ' '],
  [' ', 'x', ' '],
  ['o', 'x', 'o']
]

Each item in the board list is a list of three items. This data is stored like how a table would organize its data into rows and columns. The inner lists are the rows while their items are the columns:

board[0][0] board[0][1] board[0][2]
board[1][0] board[1][1] board[1][2]
board[2][0] board[2][1] board[2][2]
For example:

row = 2
column = 1

print(board[row][column])
# Output: x

To go deeper on 2D lists, check out Python.org's Nested List Comprehensions.

Codédex
Made with  in Brooklyn, NY
"""
