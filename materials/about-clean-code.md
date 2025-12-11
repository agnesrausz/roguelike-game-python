# About Clean Code

You have started to *write* code. This act implies that most probably somebody will *read* it later. The reader can be
your pair-programming partner, your teammate, your boss, any open source contributors, etc. Even if your code is read
only by the computer, you might have to build on it later so that you will be the reader. Even if you don't plan to read
it in the future, your incentive should be to write *clean code* which is not only pleasant to read but also simple to
build upon.

> *Programs are meant to be read by humans and only incidentally for computers to execute* — Donald Knuth

## Why do you need this?

For a novice programmer it is not always clear why clean coding got so much focus amongst seniors. It is understandable
since the advantages of clean code become more and more evident as the codebase becomes larger, the project duration
becomes longer, and the collaboration around the code becomes more intense.

So the main features of clean code:

- easier to understand

- easier to spot bugs

- easier to maintain

- easier to test

will get a growing importance as you advance in your career. In real life projects, knowing and following clean code
principles is a must-have. So it is in your best interest to start developing yourself in this aspect as early on as
possible.

## What is clean code??

Writing clean code means writing readable and sustainable code. A clean code version of implementing some functionality
is usually neither the shortest nor the fastest.

Some rules and advice

- Follow a consistent coding standard (see Python's PEP8: https://www.python.org/dev/peps/pep-0008/)
- Name things properly (long variable and function names are allowed), rename them as soon as you find a better name
- DRY (don't repeat yourself), write functions!
- SRP (single responsibility principle): each part (function) should do one and one thing only
- Write modular code: each part (function) should rely on parameters and return the results
- Avoid global variables
- Avoid too many levels of indentation (max. 3)
- Avoid too long functions (they should fit in a screen)
- Avoid unnecessary comments, write self-documenting code

A refactoring example: If you see return True after an if condition and return False in the else part, you can return
the condition itself.
It is even better if we follow the Single Responsibility Principle and outsource the details of the validation into
another function. At the same time we can make the conditional return even more compact.

The Zen of Python
Finally, read and contemplate about the Zen of Python, also known as PEP 20, the guiding principles for Python’s design.
An easter egg in the Python interpreter that typing import this prints this:

```
import this
```

```
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than right now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```
