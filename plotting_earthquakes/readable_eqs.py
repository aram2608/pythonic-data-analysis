from pathlib import Path
import json

# Read data as a string and convert to Python object
path = Path('/Users/ja1473/pythonic-data-analysis/eq_data/eq_data_1_day_m1.geojson')
contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)

# Creates a more readable version of the data 
path = Path('/Users/ja1473/pythonic-data-analysis/eq_data/readable_eq_data.geojson')
readable_contents = json.dumps(all_eq_data, indent=4)
path.write_text(readable_contents)