# Python IO

Every program needs to communicate with the "outer world". For simple programs, this usually means communication through
the console or by using files.

Let's explore both in a nutshell.

## Writing to the Console

Since `Hello, World!` you know that `print()` is the built-in function in Python that allows you to write messages to
the console.

### Multiple Arguments

Let's see some additional features of this function:

- You can write multiple values at once by providing multiple arguments separated by comma(s), eg.:

```python
print('apple', 'orange')
```

    >>> apple orange

This will write arguments next to each other, separated by a space character (default value).

- You can print various types; they all will be converted to strings.

```python
print(5, 'big', False, 'apples')
```

    >>> 5 big False apples

#### Non-Default Separators and Endings

If you'd like to separate your items by something other than a space, use the `sep` keyword argument.

You can print the items with no separator

```python
print(7, 'up', sep='')
```

    >>> 7up

separate them in a more structured way

```python
print('O', 'X', 'O', sep=' | ')
```

    >>> O | X | O

or print them on separate lines by specifying the newline character as the separator: `sep='\ n'`.

#### Endings

Another keyword argument, `end`, sets what will be written after all items have been printed. By default, `end='\ n'` is
set, which is why subsequent print statements write on new lines. You can set `end=''` to leave the cursor at the end of
the line.

Alternatively, you can use it to specify an arbitrary last item:

```python
print('Are', 'there', 'any', 'questions', end='?\ n')
```

    >>> Are there any questions?

Another interesting example of using the `print()` function with the `end` keyword argument is while printing inside a
loop:

```python
for i in range(5):
    print(i, end=' ')
```

    >>> 0 1 2 3 4 

## Getting User Input

The main tool for getting textual input from the user in the console is the built-in function `input()`. It may have a
string argument that will be displayed as a prompt on the screen.

The function returns the input string after the user presses enter. The return value is always a string, and the newline
character won't be part of it.

```python
user_says = input("What's on your mind today? ")
```

### Converting Types

A common case is needing a non-string input from the user, such as a numeric value. In this case, you need to convert
the input result into the expected type.

```python
num_string = input('Please give me a number: ')
number = int(num_string)
```

This might raise an error if `num_string` is not a proper numeric form. The usual way to handle this is to catch the
error and ask the user to repeat the input:

```python
def play_with_numbers():
    while True:
        try:
            num_string = input('Please give me a number! ')
            number = int(num_string)
            break
        except ValueError:
            print("That's not a valid number. Please try again.")
    print(f'Hey, I know a greater number, {number + 1}. I won!!')
```

If there are unknown parts in this snippet, don't worry. We'll discuss `loops` and `error/exception` handling elsewhere.

## Working with Files

### Reading from Files

Without diving into details, this is how you should access the contents of a text file called `file_name` line by line:

```
with open('file_name') as f:
    for line in f:
        print(line, end='')  # or process the line here
```

If the file is not huge, you can load the contents into memory (a variable) at once. If you need lines, use the
`.readlines()` method and access the lines as a regular list:

```
with open('file_name') as f:
    lines = f.readlines()
# process the lines list here
```

Be aware that in both cases the newline (`\ n`) characters are included in the line strings.

If you are not interested in lines, use the `.read()` method to load everything into one string:

```
with open('file_name') as f:
    content = f.read()
# process the content string here
```

### Writing to Files

To write a string to a file, you need to open it in "write-mode" (use the 'w' argument in open), and use the write()
method (within a with/open block):

```
with open('file_name', 'w') as f:
    f.write('This will be written to the file.')
```

The file will be created or overwritten. If you need more refined operations like appending or partial overwriting, see
the documentation below.

## Resources

- [Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
