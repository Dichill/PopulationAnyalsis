import math
import matplotlib.pyplot as plt
import pandas as pd
import numpy

"""
Year  |   Population
2015      131,528
2020      148,012
"""

"""
Starting Population of 131,528 in 2015 and Ending Population of
148,012 in 2020

Formula Used
- P(t) = P(0) * e^(k * t)
"""

"""
Lists
    Change the years list to the years you want to graph & predict
"""
municipality = "Consolacion"
years = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032]

clean_population = []
population = [] # Years Length == Population Length
aagr = []

for x in years:
    """
    p = Starting Population
    pt = Ending Population
    starting_year = Starting Year of your population data
    ending_year = Ending Year of your population data
    """
    p = 131528
    pt = 148012
    starting_year = 2015
    ending_year = 2020
    k = ending_year - starting_year

    t = x - starting_year
    pt = pt/p

    pt = numpy.log(pt) / k
    k = pt

    pt = round(p * numpy.exp(k * t))

    population.append(pt)
    print("Year: {0} | Predicted Population: {1:,}".format(x, pt))

fig, ax = plt.subplots(figsize=(16,10), facecolor='white', dpi= 80)
bars = ax.bar(years, population, width=0.5, color='firebrick', alpha=0.7, tick_label=years)

for bars in ax.containers:
    ax.bar_label(bars, labels=[f'{x:,}' for x in bars.datavalues])

graphed_aagr = []
aagr.append("n/a")
for index, elem in enumerate(population):
    if (index+1 < len(population)):
        prev_el = int(population[index-1])
        curr_el = int(elem)
        next_el = int(population[index+1])

        graphed_aagr.append(round((next_el/curr_el - 1) * 100, 4))
        aagr.append("{0}%".format(round((next_el/curr_el - 1) * 100, 4)))

graphed_aagr.insert(0, 0)

for x in population:
    clean_population.append("{0:,}".format(x))

plt.xlabel('X - YEAR')
plt.ylabel('Y - POPULATION')
plt.title('{0} Exponential Growth'.format(municipality))

plt.savefig('{0} Exponential Growth.png'.format(municipality))

figure, aagrax = plt.subplots(figsize=(16,10), facecolor='white', dpi= 80)

plt.xlabel('X - YEAR')
plt.ylabel('Y - AVERAGE ANNUAL GROWTH RATE')
plt.title('{0} Average Annual Growth'.format(municipality))

aagrbar = aagrax.bar(years, graphed_aagr, tick_label = years,
        width = 0.8, color = "cornflowerblue", alpha = 0.7)

for bars in aagrax.containers:
    aagrax.bar_label(bars, labels=aagr)

plt.savefig('{0} Average Annual Growth Rate.png'.format(municipality))

col1 = "Year"
col2 = "Population"
col3 = "AAGR"
data = pd.DataFrame({col1:years,col2:clean_population,col3:aagr})
data.to_excel('{0}Population.xlsx'.format(municipality), sheet_name='{0} Population'.format(municipality), index=False)

plt.show()