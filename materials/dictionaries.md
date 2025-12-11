# dictionaries

In [1]:

```python
# Initialization from literal
prices = {'apple': 20, 'orange': 30}
prices
```

Out[1]:

```
{'apple': 20, 'orange': 30}
```

In [2]:

```python
# Adding new keys and updating values of existing keys
prices['banana'] = 27
prices['apple'] = 19
prices
```

Out[2]:

```
{'apple': 19, 'orange': 30, 'banana': 27}
```

## Dictionary views

Dictionary methods `keys`, `values`, and `items` are called *dictionary views*. With the help of views we can iterate
through the contents of a dictionary:

In [3]:

```python
# To iterate through the keys
for product in prices.keys():
    print(product)
```

Out[3]:

```
apple
orange
banana
```

In [4]:

```python
# To iterate through the values
for price in prices.values():
    print(price)
```

Out[4]:

```
19
30
27
```

In [5]:

```python
# To iterate through the key-value pairs as tuples
for item in prices.items():
    print(item)
```

Out[5]:

```
('apple', 19)
('orange', 30)
('banana', 27)
```

In [6]:

```python
# We usually "unpack" the item tuples right in the `for` statement
for product, price in prices.items():
    print(f'The price of {product} is {price}.')
```

Out[6]:

```
The price of apple is 19.
The price of orange is 30.
The price of banana is 27.
```

A dictionary is iterable itself; by default it iterates through the keys:

In [7]:

```python
# To iterate through the keys you don't even need to use the `keys` view
for product in prices:
    print(product)
```

Out[7]:

```
apple
orange
banana
```

## Checking for keys

As usually, the `in` operator can be used for membership checking. In case of dictionaries it looks for keys:

In [8]:

```python
new_product = 'pear'
new_price = 25
if new_product not in prices:
    prices[new_product] = new_price
else:
    print(f'We already have {new_product}, thank you!')
prices
```

Out[8]:

```
{'apple': 19, 'orange': 30, 'banana': 27, 'pear': 25}
```

## Keys must be immutable

In [9]:

```python
# These are all valid keys
dic = {12: 'twelve', 'thirty': 30.0, True: "true", (21, 22): 'tuple'}
dic
```

Out[9]:

```
{12: 'twelve', 'thirty': 30.0, True: 'true', (21, 22): 'tuple'}
```

But if you try to add a key of mutable type (like a list) you'll get an error:

In [10]:

```python
wannabe_key = [1, 2, 3]
dic[wannabe_key] = 'some value'
```

Out[10]:

```
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-9-6b61de5ffb9f> in <module>
      1 wannabe_key = [1, 2, 3]
----> 2 dic[wannabe_key] = 'some value'

TypeError: unhashable type: 'list'
```

The "unhashable" is a closely related concept to immutability, it basically means the same.

## Dictionary methods

There are a few useful methods available on dictionaries. For example, trying to retrieve a value by a non-existing key
leads to an error:

In [11]:

```python
prices['coconut']
```

Out[11]:

```
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
<ipython-input-10-d8a2960e3e58> in <module>
----> 1 prices['coconut']

KeyError: 'coconut'
```

To aviod this, use the `get` method which returns `None` in this case:

In [12]:

```python
print(prices.get('coconut'))
```

Out[12]:

```
None
```

You can also define a specific default value instead of `None`:

In [13]:

```python
prices.get('coconut', 0)
```

Out[13]:

```
0
```

A related method is `setdefault` which returns the existing value if the given key is already in the dictionary,
otherwise adds a new key-value pair with the second argument as the value:

In [14]:

```python
prices.setdefault('apple', 4)
```

Out[14]:

```
19
```

In [15]:

```python
prices
```

Out[15]:

```
{'apple': 19, 'orange': 30, 'banana': 27, 'pear': 25}
```

In [16]:

```python
prices.setdefault('ananas', 4)
```

Out[16]:

```
4
```

In [17]:

```python
prices
```

Out[18]:

```
{'apple': 19, 'orange': 30, 'banana': 27, 'pear': 25, 'ananas': 4}
```

© Codecool 2019
