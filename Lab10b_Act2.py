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

    # Locate and plot each wind speed and temp
    winds = []
    temps = []
    for line in lines:
        line = line.split(',')
        winds.append(line[1])
        temps.append(line[3])

    plt.plot(winds, label="Wind avg, mph", color='blue')
    plt.plot(temps, label="Temp avg, F", color='red')

    plt.show()



if __name__ == "__main__":
    main()

