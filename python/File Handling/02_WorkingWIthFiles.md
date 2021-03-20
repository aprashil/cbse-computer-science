# Working with files in python.
You can open files in two different ways.
```py
f = open("data.txt", "r")
text = f.read()
print(text)
f.close()
```
OR
```py
with open("data.txt", "r") as f:
    text = f.read()
    print(text)
```

> Notice how in the second option we didn't have to close the file, because
after exiting the scope the file is automatically closed.