from weather_reader import FileReader

class WeatherAnalyzer(FileReader):
    """A class to analyze weather data from an input file."""

    def __init__(self, path):
        """Initialize weather analysis parameters."""
        super().__init__(path)
        self.path = path
        self.file_reader = FileReader(path)

    def _high_temp_extraction(self):
        """Extract high temps from a csv with weather data."""

        highs = []
        for row in self.file_reader.reader():
            self.file_reader._index_reader
            high = int(row[input()])