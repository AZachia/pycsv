# pycsv
a simple csv library for python

## Documentation

to upload a csv file: 
```python
from pycsv import csv
file = csv().load_file("file.csv", sep=";")
```
to load csv strings: 
```python
from pycsv import csv
file = csv().load_csv("Hello;World!", sep=";")
```
