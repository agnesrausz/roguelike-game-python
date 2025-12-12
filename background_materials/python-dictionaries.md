# Dictionaries

Dictionary is the built-in Python type implementing the abstract data type *mapping* (also known as *key-value store* or
associative array).

In these structures the elements cannot be accessed by an index but a general *key*. Keys can be numbers, strings,
tuples, and the value connected to a key is accessible by `dict_name[key]`.

Dictionaries can be created by `{}` or the `dict()` function. It is also possible to add initial content by writing
`{key1: value1, key2: value2}`.

## Keys are unique

The most important thing about dictionaries that its keys must be unique. If you add two values to the same key, the
second value will overwrite the first.

## Keys must be immutable

If keys changed they couldn't open the doors they were made for. Similarly, keys mustn't change in a key-value store.
You got an error (`TypeError: unhashable type`) if you try to add a key of mutable type (like a list) to a dictionary.

## Dictionaries are fast

A very important feature of maps (dictionaries) that they have a fast lookup mechanism, so values are retrieved quickly
even if the collection is huge. Think about "real" dictionaries: there the lexicographic (alphabetic) ordering of the
entries makes it possible to find a word pretty quickly even from 100000s of words. We'll dive into this topic deeper
when we'll discuss map implementations.

## Dictionary view objects

You can ask three different iterables from a dictionary:

- `dict.keys()` for the keys
- `dict.values()` for the values
- `dict.items()` for the key-value pairs.

## A dictionary itself is iterable

If you iterate through a dictionary, you'll be iterating through its keys. This means that writing `for key in dict` and
`for key in dict.keys()` are equivalent.

## Dictionary methods

There are many useful methods like `pop` or `setdefault`. See the documentation and try out all the features!

## Notebooks

- [Dictionaries](/background_materials/dictionaries.md)

## Further reading

- [Dictionary documentation](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)

