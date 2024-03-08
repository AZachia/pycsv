# pycsv
a simple csv library for python

<img src="https://skillicons.dev/icons?i=py&perline=12" />

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
   table = csv().load_csv("Hello ;World!"
   print(table.num_lines())
   print(table.num_columns())
   ```
- Print the table:
   ```python
   from pycsv import csv
   table = csv().load_csv("Hello ;World!\nHow ;are you?")
   table.show()
   ```
   output:
   ```┬────────╮
   │Hello │World!  │
   ├──────┼────────┤
   │How   │are you?│
   ╰──────┴────────╯
   ╭──────
   ```
   If you want to display the table by using the show() method, you need to install the [color](https://github.com/azachia/color) library.

 - Format rmthe table:
   ```python
   from pycsv import csv
   table = csv().load_csv("Hello;1;1.34")
   print(list(table))
   table.format()
   print(list(table))
   ```
      output:
   ``
   ["Hello", "1", "1.34"]
   ["Hello", 1, 1.34]
   ```
- Convert into SQL queries
   

   
