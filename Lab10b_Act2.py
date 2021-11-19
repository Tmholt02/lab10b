# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Thomas Holt
# Section:      464
# Assignment:   Lab10b_Act2
# Date:         11/19/2021

# import dependencies
import numpy as np
import matplotlib.pyplot as plt


def main():

    # Read basic data from file
    file_id = open("CLLWeatherData-1.csv", 'r')
    lines = file_id.readlines()[1:]
    file_id.close()

    # 2D array of plots
    plots = plt.subplots(2, 2)[1]

    # Locate and plot each wind speed and temp
    winds = []
    precips = []
    temps = []
    tempsMax = []
    tempsMin = []
    for line in lines:
        line = line.split(',')
        winds.append(float(line[1]))
        temps.append(float(line[3]))

    ######################################################################################

    # Create twin axis
    ax_temp = plots[0][0]
    ax_wind = ax_temp.twinx()

    wind_line = ax_wind.plot(winds, label="Wind avg, mph", color='blue')
    ax_wind.set_ylabel("Average Wind Speed (mph)", color='blue')

    temp_line = ax_temp.plot(temps, label="Temp avg, F", color='red')
    ax_temp.set_ylabel("Average Temperature (F)", color='red')

    # Prepare the legend by taking each line and each label in lists
    functions = temp_line + wind_line
    labels = [function.get_label() for function in functions]
    ax_wind.legend(functions, labels, loc=1)

    # Title and display
    plt.title("Temperature vs Wind Speed")
    plt.show()


if __name__ == "__main__":
    main()

