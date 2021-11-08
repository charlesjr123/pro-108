import csv
import pandas as pandas
import plotly.figure_factory as pfp

df=pandas.read_csv('data.csv')
print(df)


fig=pfp.create_distplot([df['Sr.No(numbers)'].toList()],["number"],show_hist=False)
fig.show()