## 25. Reading List
"""
Let's start a book club by making a
list of tech startup books! 📚

"""

books = ['Zero to One', 'The Lean Startup', 'The Mom Test','Make It Stick', 'Life in Code']

books.append ('Zero to One') 
##Output = ['Zero to One', 'The Lean Startup', 'The Mom Test', 'Make It Stick', 'Life in Code', 'Zero to One']
books.remove ('The Lean Startup')
books.pop (0)
##Output = ['The Mom Test', 'Make It Stick', 'Life in Code', 'Zero to One']
print(books)

