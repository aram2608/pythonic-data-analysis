from die import Die
import plotly.express as px
import plotly.io as pio
pio.renderers.default = 'browser' # Use this to open a browser window
# pio.renderers.default = 'notebook' use this to plot in a Jupyter notebook

die_1 = Die()
die_2 = Die(10)

results = []
for rolls in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

frequencies = []
max_results = die_1.num_sides + die_2.num_sides # Sum of the largest values on both die
poss_results = range(1, max_results+1) # We need to include +1 to include every possible value
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

title = "Results of Rolling Two D6 1,000 Times" # chart title
labels = {'x': 'Results', 'y': 'Frequency of Results'} # Dictionary with x and y labels
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Customixation
fig.update_layout(xaxis_dtick=1)
fig.show()