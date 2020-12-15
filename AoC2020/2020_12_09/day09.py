def findIfTwoNumbersInListSum(nbr_list, nbr):
    two_sum_nbrs = None
    for index, first_in_list in enumerate(nbr_list):
        for second_nbr_in_list in nbr_list[index + 1:]:
            if first_in_list + second_nbr_in_list == nbr:
                two_sum_nbrs = first_in_list, second_nbr_in_list
    return two_sum_nbrs


def sol_1(input_data, preamble):
    for i in range(0, len(input_data) - preamble):
        nbr_list = input_data[i:preamble + i]
        nbr = input_data[preamble + i]
        two_sum_nbrs = findIfTwoNumbersInListSum(nbr_list, nbr)
        if two_sum_nbrs is None:
            return nbr


def sol_2(input_data, nbr):
    for i in range(0, len(input_data)):
        index = i
        while True:
            if sum(input_data[i:index]) == nbr:
                return max(input_data[i:index]) + min(input_data[i:index])
            elif sum(input_data[i:index]) > nbr:
                break
            index += 1


def main():
    input_data = list(map(int, open('input.txt', "r").read().split("\n")))

    preamble = 25  # Length of nbr tail to check
    sol1 = sol_1(input_data, preamble)
    print(sol1)

    sol2 = sol_2(input_data, sol1)
    print(sol2)


if __name__ == "__main__":
    main()
