import pandas as pd 
from pandas_datareader import DataReader
from datetime import date
import time
import matplotlib.pyplot as plt

print()
print(('*'*8+' '*8+'Economic data from the Federal Reserve'+' '*8+'*'*8).center(142))
print()

series_code = 'GOLDAMGBD228NLBM'

# Set start and end dates
start = date(1968,1,1)
end = date(2016,12,31)

# Set the ticker
#ticker = 'AAPL'

# Set the data source
data_source = 'fred'  #federal reserve economic data

# Import the stock prices
gold_price = DataReader(series_code, data_source, start)

# Display and inspect the result
print(gold_price.head())
print()
gold_price.info()

# Plot the price of gold
gold_price.plot(title = 'Gold Price')

# Show the plot
plt.show(block=False)
plt.pause(3)
plt.close()

print()
print(('*'*8+' '*8+'Compare labor market participation and unemployment rates'+' '*8+'*'*8).center(142))
print()

# Set the start date
start = date(1950,1,1)

# Define the series codes
series = ['UNRATE', 'CIVPART']

# Import the data
econ_data = DataReader(series,'fred',start=start)

# Assign new column labels
econ_data.columns = ['Unemployment Rate','Participation Rate']

# Plot econ_data
econ_data.plot(title = 'Labor Market', subplots = True)

# Show the plot
plt.show(block=False)
plt.pause(3)
plt.close()




print('\n'*50)