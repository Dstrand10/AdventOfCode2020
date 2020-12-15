import sys
import numpy as np

np.set_printoptions(threshold=sys.maxsize)
import matplotlib.pyplot as plt


def sol1(input_data):
    # Initial values
    count_1_diff = 0
    count_3_diff = 0
    outage_volt = 0

    while True:
        possible_outage_volts = [x for x in input_data if outage_volt + 3 >= x > outage_volt]

        if len(possible_outage_volts) > 0:
            new_outage_volt = min(possible_outage_volts)
            if new_outage_volt - outage_volt == 1:
                count_1_diff += 1
            elif new_outage_volt - outage_volt == 3:
                count_3_diff += 1
            outage_volt = new_outage_volt
        else:
            break

    outage_volt += 3
    count_3_diff += 1  # Since last adapter also can do a 3-step
    print("The output voltage is: " + str(outage_volt))
    return count_1_diff * count_3_diff


def sol2(input_data):
    end_output_voltage = max(input_data)
    adj_matrix = np.zeros((end_output_voltage + 1, end_output_voltage + 1))

    # Initial step from 0 volt
    adj_matrix[0, 1] = 1
    adj_matrix[0, 2] = 1
    adj_matrix[0, 3] = 1

    # Parsing the input data to prepare the adjacency matrix
    for nbr in input_data:
        row = nbr
        column = nbr
        if column + 1 <= end_output_voltage:
            adj_matrix[row, column + 1] += 1
        if column + 2 <= end_output_voltage:
            adj_matrix[row, column + 2] += 1
        if column + 3 <= end_output_voltage:
            adj_matrix[row, column + 3] += 1

    count_distribution = []
    for i in range(0, end_output_voltage + 1):
        matrix = np.linalg.matrix_power(adj_matrix, i)
        count_distribution.append(matrix[0][end_output_voltage])
    # plt.plot(count_distribution)
    # plt.show()
    return sum(count_distribution)


def main():
    input_data = list(map(int, open('input.txt', "r").read().split("\n")))

    sol_1 = sol1(input_data)
    print("Solution to question 1: " + str(sol_1))

    sol_2 = sol2(input_data)
    print("Solution to question 2: " + str(int(sol_2)))


if __name__ == "__main__":
    main()
