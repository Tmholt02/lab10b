# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Thomas Holt
# Section:      464
# Assignment:   Lab10b Act 1
# Date:         11/19/2021


# import dependencies
import numpy as np
import matplotlib.pyplot as plt


# main method!
def main():

    # Lets store some data
    matrix = np.array([[1.00583, -0.087156], [0.087156, 1.00583]])
    points = [np.array([[1], [0]])]

    # 250 new points, each based on the previous times the matrix. Also have some fun with the markers and colors
    for i in range(250):
        points.append(matrix @ points[i])
        plt.scatter(points[i+1][0][0], points[i][1][0], color='byrg'[i % 4], marker=".,ov^<>12348spP*hH+xXDd|_"[i % 25])

    # Plot the last point and display the graph
    plt.scatter(points[250][0][0], points[250][1][0], color='byrg'[250 % 4], marker=".,ov^<>12348spP*hH+xXDd|_"[250 % 25])
    plt.show()


# Start script
if __name__ == "__main__":
    main()

