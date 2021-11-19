# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Thomas Holt
# Section:      464
# Assignment:   Lab10b_Act2
# Date:         11/19/2021

# import dependencies
from typing import List

import numpy as np
import matplotlib.pyplot as plt


def main():
    # Read basic data from file
    file_id = open("CLLWeatherData-1.csv", 'r')
    lines = file_id.readlines()[1:]
    file_id.close()

    # Divide the plot into two rows and two cols
    plt.subplots(2, 2)

    # Locate and plot each value within the spreadsheet
    winds: list[float] = []
    precips: list[float] = []
    temps: list[float] = []
    temps_max: list[float] = []
    temps_min: list[float] = []
    for line in lines:
        line = line.split(',')
        winds.append(float(line[1]))
        precips.append(float(line[2]))
        temps.append(float(line[3]))
        temps_max.append(float(line[4]))
        temps_min.append(float(line[5]))

    ######################################################################################

    # Create twin axis and set plt focus
    ax_temp = plt.subplot(2, 2, 1)
    plt.xlabel("Day")
    ax_wind = ax_temp.twinx()

    plt.title("Temperature vs Wind Speed")

    wind_line = ax_wind.plot(winds, label="Wind avg, mph", color='blue')
    ax_wind.set_ylabel("Average Wind Speed (mph)", color='blue')

    temp_line = ax_temp.plot(temps, label="Temp avg, F", color='red')
    ax_temp.set_ylabel("Average Temperature (F)", color='red')

    # Prepare the legend by taking each line and each label in lists
    functions = temp_line + wind_line
    labels = [function.get_label() for function in functions]
    ax_wind.legend(functions, labels, loc=1)

    ######################################################################################

    precips_arr = np.array(precips)
    print()
    for val in np.where(precips_arr > 1, precips_arr, -1):
        print(val)

    ######################################################################################

    ######################################################################################

    ######################################################################################

    # Display the finished product
    plt.show()


if __name__ == "__main__":
    main()
