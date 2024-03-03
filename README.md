# pycsv
a simple csv library for python

## Installation
Copy the pycsv file in your project directory and import it with:
```python
from pycsv import csv
```

## Documentation

 - Upload a csv file: 
    ```python
    from pycsv import csv
    file = csv().load_file("file.csv", sep=";")
    ```
 - Load csv strings: 
    ```python
    from pycsv import csv
    table = csv().load_csv("Hello ;World!", sep=";")
    ```

 - Load python lists:
    ```python
    from pycsv import csv
    table = csv().load_table([["Hello", "world"]])
    ```

 - Save the table to a file:
      ```python
      from pycsv import csv
      table = csv().load_table([["Hello", "world"]])
      table.save("file.csv")
      ```
 - Get the table as a list:
      ```python
      from pycsv import csv
      file = csv().load_file("file.csv")
      print(list(file))
      ```
-  Get the table as a string:
      ```python  
      from pycsv import csv
      file = csv().load_file("file.csv")
      print(str(file))
      ```

 - Copy the table:
      ```python
      from pycsv import csv
      table = csv().load_file("file.csv")
      table2 = table.copy()
      ```

- Get the table size:
   ```python
   from pycsv import csv
   table = csv().load_csv("Hello ;World!", sep=";")
   print(table.num_lines())
   print(table.num_columns())
   ```