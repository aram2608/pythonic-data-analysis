from die import Die
import plotly.express as px
import plotly.io as pio
pio.renderers.default = 'browser' # Use this to open a browser window
# pio.renderers.default = 'notebook' use this to plot in a Jupyter notebook

die = Die()

results = []
for rolls in range(1000):
    result = die.roll()
    results.append(result)

frequencies = []
poss_results = range(1, die.num_sides+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

title = "Results of Rolling One D6 1,000 Times" # chart title
labels = {'x': 'Results', 'y': 'Frequency of Results'} # Dictionary with x and y labels
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.show()
