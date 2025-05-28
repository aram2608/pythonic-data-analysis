from pathlib import Path
import csv

class FileReader:
    """A class to manage the reading of files."""

    def __init__(self, path):
        """Inititalize parameters for reading in files."""
        self.path = Path(path)

    def _read_lines(self):
        """Read the file and extract lines."""
        path = self.path
        lines = path.read_text(encoding='utf-8').splitlines() # Extracts all the lines in the file

        reader = csv.reader(lines) # Creates a reader object, parses each line in a file and stores values in a list
        header_row = next(reader) # Next function returns the next line in a file starting at the beginning
        self.reader = reader
        self.header_row = header_row
    
    def _index_reader(self):
        """A function to print the headers of a csv and their corresponding index."""
        self._read_lines()

        for index, column_header in enumerate(self.header_row): # Enumerate returns both the index and value of each item in a list
            print(index, column_header)