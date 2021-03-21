# Module: CSV

The CSV module allows us to interact with csv files in python.
> import csv
Note: csvfile refers to the object returned by the open function.

## Methods:
1) `csv.reader(csvfile, delimiter = ',')`: returns an iterable object that contains the fields in the csv file.

```py
import csv
with open('x.csv','r') as csvfile:
    csvcontent = csv.reader(csvfile, delimiter = ',')
    for row in csvcontent:
        print(row)
```

2) `csv.writer(csvfile, delimiter=",")`: returns a writer object to write to the csv file.
3) `writerObj.writerow(array)`: writes the array to the csv file.
4) `writerObj.writerows(array)`: writes an array of rows as seperate rows to the csv file.

```py
import csv
with open('x.csv','a') as csvfile:
    csvWriter = csv.writer(csvfile, delimiter=',')
    csvWriter.writerow([1,2,3,4])
    csvWriter.writerows([[5,6,7,8,],[9,10,11,12]])
	
"""
Final Content:
1,2,3,4
5,6,7,8
9,10,11,12
"""
```