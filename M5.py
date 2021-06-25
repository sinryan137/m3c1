# Import the matplotlib.pyplot submodule and name it plt
import matplotlib.pyplot as plt

# Create a Figure and an Axes with plt.subplots
fig, ax = plt.subplots()

# Call the show function to show the result
plt.show()

# Import the matplotlib.pyplot submodule and name it plt
import matplotlib.pyplot as plt

# Create a Figure and an Axes with plt.subplots
fig, ax = plt.subplots()

import pandas as pd
seattle_weather=pd.read_csv("seattle_weather.csv")
austin_weather=pd.read_csv("austin_weather.csv")

# Plot MLY-PRCP-NORMAL from seattle_weather against the MONTH
ax.plot(seattle_weather["DATE"], seattle_weather["MLY-PRCP-NORMAL"])

# Plot MLY-PRCP-NORMAL from austin_weather against MONTH
ax.plot(austin_weather["DATE"], austin_weather["MLY-PRCP-NORMAL"])

# Call the show function
plt.show()

# Plot Seattle data, setting data appearance
ax.plot(seattle_weather["DATE"], seattle_weather["MLY-PRCP-NORMAL"], color=("b"), marker=("o"), linestyle=("--"))

# Plot Austin data, setting data appearance
ax.plot(austin_weather["DATE"], austin_weather["MLY-PRCP-NORMAL"], color=("r"), marker=("v"), linestyle=("--"))

# Call show to display the resulting plot
plt.show()

ax.plot(seattle_weather["DATE"], seattle_weather["MLY-PRCP-NORMAL"])
ax.plot(austin_weather["DATE"], austin_weather["MLY-PRCP-NORMAL"])

# Customize the x-axis label
ax.set_xlabel("Time (months)")

# Customize the y-axis label
ax.set_ylabel("Precipitation (inches)")

# Add the title
ax.set_title("Weather patterns in Austin and Seattle")

# Display the figure
plt.show()

# Create a Figure and an array of subplots with 2 rows and 2 columns
fig, ax = plt.subplots(2, 2)

# Addressing the top left Axes as index 0, 0, plot month and Seattle precipitation
ax[0, 0].plot(seattle_weather["DATE"], seattle_weather["MLY-PRCP-NORMAL"])

# In the top right (index 0,1), plot month and Seattle temperatures
ax[0, 1].plot(seattle_weather["DATE"], seattle_weather["MLY-TAVG-NORMAL"])

# In the bottom left (1, 0) plot month and Austin precipitations
ax[1, 0].plot(austin_weather["DATE"], austin_weather["MLY-PRCP-NORMAL"])

# In the bottom right (1, 1) plot month and Austin temperatures
ax[1, 1].plot(austin_weather["DATE"], austin_weather["MLY-TAVG-NORMAL"])
plt.show()

# Create a figure and an array of axes: 2 rows, 1 column with shared y axis
fig, ax = plt.subplots(2, 1, sharey=True)

# Plot Seattle precipitation data in the top axes
ax[0].plot(seattle_weather["DATE"], seattle_weather["MLY-PRCP-NORMAL"], color = "b")
ax[0].plot(seattle_weather["DATE"], seattle_weather["MLY-PRCP-25PCTL"], color = "b", linestyle = "--")
ax[0].plot(seattle_weather["DATE"], seattle_weather["MLY-PRCP-75PCTL"], color = "b", linestyle = "--")

# Plot Austin precipitation data in the bottom axes
ax[1].plot(austin_weather["DATE"], austin_weather["MLY-PRCP-NORMAL"], color = "r")
ax[1].plot(austin_weather["DATE"], austin_weather["MLY-PRCP-25PCTL"], color = "r", linestyle = "--")
ax[1].plot(austin_weather["DATE"], austin_weather["MLY-PRCP-75PCTL"], color = "r", linestyle = "--")

plt.show()

# Import pandas as pd
import pandas as pd

# Read the data from file using read_csv
climate_change = pd.read_csv("climate_change.csv", parse_dates=["date"], index_col=["date"])

import matplotlib.pyplot as plt
fig, ax = plt.subplots()

# Add the time-series for "relative_temp" to the plot
ax.plot(climate_change.index, climate_change["relative_temp"])

# Set the x-axis label
ax.set_xlabel("Time")

# Set the y-axis label
ax.set_ylabel("Relative temperature (Celsuis)")

# Show the figure
plt.show()

import matplotlib.pyplot as plt
fig, ax = plt.subplots()

# Add the time-series for "relative_temp" to the plot
ax.plot(climate_change.index, climate_change["relative_temp"])

# Set the x-axis label
ax.set_xlabel("Time")

# Set the y-axis label
ax.set_ylabel('Relative temperature (Celsius)')

# Show the figure
plt.show()

import matplotlib.pyplot as plt

# Use plt.subplots to create fig and ax
fig, ax = plt.subplots()


# Create variable seventies with data from "1970-01-01" to "1979-12-31"
seventies = climate_change["1970-01-01":"1979-12-31"]

# Add the time-series for "co2" data from seventies to the plot
ax.plot(seventies.index, seventies["co2"])
ax.set_xlabel("Index")
ax.set_ylabel("co2")

# Show the figure
plt.show()

import matplotlib.pyplot as plt

# Initalize a Figure and Axes
fig, ax = plt.subplots()

# Plot the CO2 variable in blue
ax.plot(climate_change.index, climate_change["co2"], color="blue")

# Create a twin Axes that shares the x-axis
ax2 = ax.twinx()

# Plot the relative temperature in red
ax2.plot(climate_change.index, climate_change["relative_temp"], color="red")

plt.show()

# Define a function called plot_timeseries
def plot_timeseries(axes, x, y, color, xlabel, ylabel):

  # Plot the inputs x,y in the provided color
  axes.plot(x, y, color=color)

  # Set the x-axis label
  axes.set_xlabel(xlabel)

  # Set the y-axis label
  axes.set_ylabel(ylabel, color=color)

  # Set the colors tick params for y-axis
  axes.tick_params('y', colors=color)

  fig, ax = plt.subplots()

  # Plot the CO2 levels time-series in blue
  plot_timeseries(ax, climate_change.index, climate_change["co2"], "blue", "Time (years)", "CO2 levels")

  # Create a twin Axes object that shares the x-axis
  ax2 = ax.twinx()

  # Plot the relative temperature data in red
  plot_timeseries(ax, climate_change.index, climate_change["relative_temp"], "red", "Time (years)",
                  "Relative temperature (Celsius)")

  plt.show()

  fig, ax = plt.subplots()

  # Plot the relative temperature data
  ax.plot(climate_change.index, climate_change['relative_temp'])

  # Annotate the date at which temperatures exceeded 1 degree
  ax.annotate(">1 degree", xy=[pd.Timestamp("2015-10-16"), 1])

  plt.show()

  fig, ax = plt.subplots()

  # Plot the CO2 levels time-series in blue
  plot_timeseries(ax, climate_change.index, climate_change["co2"], 'blue', "Time (years)", "Co2 levels")

  # Create an Axes object that shares the x-axis
  ax2 = ax.twinx()

  # Plot the relative temperature data in red
  plot_timeseries(ax, climate_change.index, climate_change["relative_temp"], 'red', "Time (years)",
                  "Relative temp (Celsius)")

  # Annotate point with relative temperature >1 degree
  ax2.annotate(">1 degree", xy=(pd.Timestamp("2008-10-06"), 1), xytext=(pd.Timestamp("2008-10-06"), -0.2),
               arrowprops={"arrowstyle": "->", "color": "gray"})

  plt.show()




