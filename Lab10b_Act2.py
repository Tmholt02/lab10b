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

    # Divide the plot into two rows and two cols
    plt.subplots(2, 2)

    # Locate and plot each value within the spreadsheet
    dates: list[str] = []
    winds: list[float] = []
    precips: list[float] = []
    temps: list[float] = []
    temps_max: list[float] = []
    temps_min: list[float] = []
    for line in lines:
        line = line.split(',')
        dates.append(line[0])
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

    # Get the current title correct
    plt.title("Temperature vs Wind Speed")

    # Prepare and plot the wind speeds
    wind_line = ax_wind.plot(winds, label="Wind avg, mph", color='blue')
    ax_wind.set_ylabel("Average Wind Speed (mph)", color='blue')

    # Prepare and plot the temperatures
    temp_line = ax_temp.plot(temps, label="Temp avg, F", color='red')
    ax_temp.set_ylabel("Average Temperature (F)", color='red')

    # Prepare the legend by taking each line and each label in lists
    functions = temp_line + wind_line
    labels = [function.get_label() for function in functions]
    ax_wind.legend(functions, labels, loc=1)

    ######################################################################################

    # Select and label up the graph
    graph = plt.subplot(2, 2, 2)
    plt.title("Histogram of Precipitation")
    graph.set_ylabel("Number of Days")
    plt.xlabel("Precipitation (in)")

    # Make a histogram of precipitation values
    days, in_rain = np.histogram(precips, bins=np.linspace(start=0.0, stop=5.0, num=50))
    graph.bar(in_rain[1:-1], days[1:], in_rain[1] - in_rain[0], align="edge")

    ######################################################################################

    # Select and label up the graph
    graph = plt.subplot(2, 2, 3)
    plt.title("Wind Speed vs Temp Low")
    graph.set_ylabel("Average Wind Speed (mph)")
    plt.xlabel("Minimum Temperature (F)")

    # Plot the values I guess
    graph.scatter(temps_min, winds, color='black', s=2)

    ######################################################################################

    # Dictionary stores monthly data for finding averages
    monthly_temp_data = {
        # '<month>': ([<avg_temp_sum>, <sample_cnt>],
        #             [<min_temp_sum>, <sample_cnt>],
        #             [<max_temp_sum>, <sample_cnt>])
        '1':  ([0, 0], [0, 0], [0, 0]),
        '2':  ([0, 0], [0, 0], [0, 0]),
        '3':  ([0, 0], [0, 0], [0, 0]),
        '4':  ([0, 0], [0, 0], [0, 0]),
        '5':  ([0, 0], [0, 0], [0, 0]),
        '6':  ([0, 0], [0, 0], [0, 0]),
        '7':  ([0, 0], [0, 0], [0, 0]),
        '8':  ([0, 0], [0, 0], [0, 0]),
        '9':  ([0, 0], [0, 0], [0, 0]),
        '10': ([0, 0], [0, 0], [0, 0]),
        '11': ([0, 0], [0, 0], [0, 0]),
        '12': ([0, 0], [0, 0], [0, 0])
    }

    # We will loop through all days and find data for averaging
    for day_idx in range(len(dates)):

        # Identify what month this day is
        month = dates[day_idx].split('/')[0]

        # Increment sample counters
        monthly_temp_data[month][0][1] += 1
        monthly_temp_data[month][1][1] += 1
        monthly_temp_data[month][2][1] += 1

        # Add sample to the sum
        monthly_temp_data[month][0][0] += temps[day_idx]
        monthly_temp_data[month][1][0] += temps_min[day_idx]
        monthly_temp_data[month][2][0] += temps_max[day_idx]

    # Index = month and value = average monthly value for specified field
    months = range(1, 13)
    monthly_temps_avg = [value[0][0] / value[0][1] for value in monthly_temp_data.values()]
    monthly_temps_min = [value[1][0] / value[1][1] for value in monthly_temp_data.values()]
    monthly_temps_max = [value[2][0] / value[2][1] for value in monthly_temp_data.values()]

    # Plot theses on the appropriate plot in nice styles with a legend
    graph = plt.subplot(2, 2, 4)
    graph.bar(months, monthly_temps_avg, color='green')
    graph.plot(months, monthly_temps_min, color='blue', label='Low Temp')
    graph.plot(months, monthly_temps_max, color='red', label='High Temp')
    plt.xticks(months)
    graph.legend()

    # Title the graph and make labels
    plt.title("Average Temperature by Month")
    plt.xlabel("Month")
    graph.set_ylabel("Average Temp (F)")

    ######################################################################################

    # Display the finished product
    # I hope they like it
    plt.show()


if __name__ == "__main__":
    main()
