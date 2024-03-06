"""
# ---------- Pycsv ----------

## A simple csv module for python by @AZachia

website & documentation: [github.com/AZachia/pycsv](https://github.com/AZachia/pycsv)

With this module you can:
- Create a new csv table
- Load a csv table from a string
- Load a csv table from a file
- Save a csv table to a file
- Sort a csv table
- Get the number of lines and colones
- Format the csv table
- Show the csv table in a pretty way
- Get the csv table as a string
- Copy the csv table
- Get a line of the csv table
- Get the length of the csv table
- Iterate through the csv table
- And more...

Example:
```python
from pycsv import csv
file = csv().load_file("file.csv", sep=";")
print(list(file))
```

"""

try:
    import color
except:
    color = None


class csv:
    """
    A simple CSV (Comma-Separated Values) utility class.

    Attributes:
        table (list[list]): The CSV table data.
        sep (str): The separator character used in the CSV file.
    """

    def __init__(self, table: list[list] = [[]], sep=";") -> None:
        """
        The constructor for the CSV class.

        Parameters:
            - table (list[list]): The initial table data. Defaults to an empty list of lists.
            - sep (str): The separator used in the CSV file. Defaults to ";".

        Returns:
            None
        """
        self.table = table
        self.sep = sep

    def new(self, lines:int, columns:int, fill:str=" "):
        """Create a new table with the specified number of lines and columns.

        Args:
            lines (int): The number of lines in the table.
            columns (int): The number of columns in the table.
            fill (str, optional): The value to fill the table cells with. Defaults to " ".

        Returns:
            pycsv: The updated pycsv object with the new table.
        """
        self.table = [[fill for column in range(columns)] for line in range(lines)]
        return self

    def load_table(self, table: list[list]):
            """
            Load a table into the PyCSV object.

            Args:
                table (list[list]): The table to load.

            Returns:
                PyCSV: The PyCSV object itself.
            """
            self.table = table
            return self

    def load_csv(self, text: str, sep:str=";"):
        self.table = []
        for line in text.split("\n"):
            if line != "\n":
                self.table.append(line.split(self.sep))
        return self

    def load_file(self, path:str, sep: str = ';'):
        self.table = []
        with open(path, "r", encoding="utf-8") as file:
            for line in file.readlines():
                if line != "":
                    self.table.append(line.replace("\n", "").split(sep))
        file.close()
        return self

    def save(self, path:str, encoding="utf-8"):
        with open(path, "w", encoding=encoding) as file:
            file.write(self.__str__())
        file.close()

    def sort(self):
        for line in self.table:
            try:
                line = line.sort()
            except:
                pass
        return self

    def num_lines(self) -> int:
        return len(self.table)

    def num_columns(self) -> int:
        columns = 0
        for line in self.table:
            columns = max([columns, len(line)])
        return columns

    def format(self):
        for line in self.table:
            for index, item in enumerate(line):
                try:
                    line[index] = eval(str(item))
                except Exception as e:
                    line[index] = str(item)
        return self

    def show(self, *args, **kwargs):
        if color:
            color.table(tab=self.table, *args, **kwargs)
        else:
            print(str(self))

    def text(self) -> str:
        return str(self)

    def copy(self) -> "csv":
        copy = csv()
        copy.table = self.table
        copy.sep = self.sep
        return copy

     def toSQL(self, tablename: str, columns:list | tuple = None, startindex:int = 1, types: str | list = "auto") -> str:
        sql = ""
        if not columns:
            columns = list(self)[0]
        for row in list(self)[startindex:]:
            values = []
            for column, item in enumerate(row):
                item = str(item)
                if types == "auto":
                    if item.isdecimal():
                        values.append(item)
                    else:
                        values.append(f'"{item}"')
                else:
                    if types[column] in (int, float):
                        values.append(item)
                    else:
                        values.append(f'"{item}"')

            line = f"""INSERT INTO {tablename} ({', '.join(columns)}) VALUES ({', '.join(values)})"""
            sql += line + ";\n"
        return sql

    def __str__(self) -> str:
        text = ""
        for index, line in enumerate(self.table):
            text += self.sep.join(str(item) for item in line)+'\n'
        return text

    def __getitem__(self, item):
        return self.table[item]

    def __len__(self):
        return len(self.table)
    
    def __iter__(self):
        return iter(self.table)
