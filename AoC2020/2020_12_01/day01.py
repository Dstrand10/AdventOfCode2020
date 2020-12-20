def find_two_numbers_adding_up(in_data, add_up_sum):
    for first_nbr in in_data:
        tmp_list = in_data.copy()
        tmp_list.remove(first_nbr)
        complement_nbr = add_up_sum - first_nbr
        if complement_nbr in tmp_list:
            return first_nbr, complement_nbr


def find_three_numbers_adding_up(in_data, add_up_sum):
    for nbr in in_data:
        tmp_list = in_data.copy()
        tmp_list.remove(nbr)
        complement_nbr = add_up_sum - nbr
        second_nbr, third_nbr = find_two_numbers_adding_up(tmp_list, complement_nbr)
        if second_nbr is not None and third_nbr is not None:
            return nbr, second_nbr, third_nbr
    return None, None, None


def recursive_solution_inf_deep(in_data, final_sum, nbrs_to_add):
    tmp_answer = None
    for index, i in enumerate(in_data):
        if nbrs_to_add > 2:
            tmp_nbr = recursive_solution_inf_deep(in_data[index + 1:], final_sum - i, nbrs_to_add - 1)
            if tmp_nbr is None:
                continue
            else:
                print("nbr found: " + str(i))
                tmp_answer = i * tmp_nbr
        elif nbrs_to_add == 2:
            if final_sum - i in in_data[index + 1:]:
                print("nbr found: " + str(final_sum - i))
                print("nbr found: " + str(i))
                return i * (final_sum - i)
    return tmp_answer


def main():
    with open('input.txt') as f:
        in_data = list(map(int, f))
        final_sum = 2020
        nbrs_to_add = 3

        first_nbr, second_nbr = find_two_numbers_adding_up(in_data, final_sum)
        if first_nbr is not None and second_nbr is not None:
            print("Solution to first question: " + str(first_nbr * second_nbr))
        else:
            print("Something went very wrong, solution could not be found.")

        first_nbr, second_nbr, third_nbr = find_three_numbers_adding_up(in_data, final_sum)
        if first_nbr is not None and second_nbr is not None and third_nbr is not None:
            print("Solution to second question: " + str(first_nbr * second_nbr * third_nbr))
        else:
            print("Something went very wrong, solution could not be found.")

        print(recursive_solution_inf_deep(in_data, final_sum, nbrs_to_add))


if __name__ == "__main__":
    main()
