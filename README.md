# First-Recurring-Character
First Recurring Character

Using List Comprehensions to find the first repeated character in a String.

```python
def first_recurring(given_string):
  ```  

```python
return[char for char in given_string if given_string.count(char) > 1][0]
```

```python
print(first_recurring("DBCABA"))
```
