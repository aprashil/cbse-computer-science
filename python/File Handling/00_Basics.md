# Basics of File Handling

Files are external sources that store data.
Some file types: txt, csv

The main function used in python for file handling is the open function:
<strong>open("filename.ext","mode")</strong>

### Different file opening modes:

- r - read only, error if file doesnt exist, cursor at start of file
- w - write, creates file if it doesnt exist, cursor at start of file
- a - append, creates file if it doesnt exist, cursor at end of file

- r+ - same as r but also writes
- w+ - same as w but also reads
- a+ - same as a but  also reads

> For binary files, just add a 'b' after any mode:
eg. rb, wb+, ab, rb+
