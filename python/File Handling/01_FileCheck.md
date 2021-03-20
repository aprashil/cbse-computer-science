# Checking file existance in python.

You can check for the existance of a file before attempting to perform actions
so that incase the file doesnt exist, the program isn't halted.

You can do this in two different ways.

1)
```py
import os
if os.path.isfile('data.txt'):
    {funcionality}
else:
    {alert user that file doesnt exist}
```

2)
```py
try:
    {functionality}
except FileNotFoundError:
    {alert user that file doesnt exist}
```