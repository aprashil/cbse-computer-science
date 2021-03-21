# List Comprehension

> What is list comprehension?
> List comprehension is a shorter syntax for creating a list from another list.

Syntax: `newlist = [expression for item in iterable if condition == True]`
    
For Example:
```py
numbers = [1,2,3,4,5,6,7,8,9,10]
even = []
for i in numbers:
    if i%2 == 0:
        even.append(i)

print(even) #[2, 4, 6, 8, 10]
```
is the same as
```py
numbers = [1,2,3,4,5,6,7,8,9,10]
even = [i for i in numbers if i%2 == 0]
print(even) #[2, 4, 6, 8, 10]
```
and if you wanted a list that had multiplied the resultant elements by 2,
```py
even = [i*2 for i in numbers if i%2 == 0]
print(even) #[4, 8, 12, 16, 20]
```

