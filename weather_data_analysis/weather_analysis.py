from weather_reader import FileReader
from analyzer import WeatherAnalyzer

sitka_weather = FileReader('/Users/ja1473/pythonic-data-analysis/weather_data/sitka_weather_07-2021_simple.csv')

sitka_weather._index_reader()

analysis = WeatherAnalyzer('/Users/ja1473/pythonic-data-analysis/weather_data/sitka_weather_07-2021_simple.csv')
analysis._high_temp_extraction()