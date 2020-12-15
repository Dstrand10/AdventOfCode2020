import numpy as np
import timeit


def sol_1(input_data):
    timestampt_to_leave = int(input_data[0])
    buses = input_data[1].split(",")
    buses = [busid for busid in buses if busid != "x"]  # Removing x
    buses = list(map(int, buses))

    least_minutes_to_wait = np.Inf
    for busid in buses:
        minutes_to_wait = busid - timestampt_to_leave % busid
        if minutes_to_wait < least_minutes_to_wait:
            least_minutes_to_wait = minutes_to_wait
            solution1 = minutes_to_wait * busid
    return solution1


def sol_2(input_data):
    buses = input_data[1].split(",")
    total_mod = np.prod([int(bus) for bus in buses if bus != "x"])
    timestamp_before_mod = 0

    # Chinese reminder theorem calculating timestamp. Look it up
    for idx, bus in enumerate(buses):
        if bus != "x":
            m_i = int(bus)
            M_i = int(total_mod / m_i)
            M_i_inverse = pow(M_i, -1, m_i)
            timestamp_before_mod += -idx * M_i * M_i_inverse
    timestamp = timestamp_before_mod % total_mod
    return timestamp


def main():
    input_data = open('input.txt', "r").read().split("\n")
    sol1 = sol_1(input_data)
    sol2 = sol_2(input_data)
    print("Solution 1: " + str(sol1))
    print("Solution 2: " + str(sol2))


if __name__ == "__main__":
    main()
