class Cup:
    def __init__(self, cup_nbr, prev_cup, next_cup):
        self.cup_nbr = cup_nbr
        self.prev_cup = prev_cup
        self.next_cup = next_cup


def get_cup_arrengement(input_data, part1):
    cups_nbrs = []
    for cup_nbr in input_data:
        cups_nbrs.append(Cup(cup_nbr, None, None))

    if not part1:
        for i in range(len(cups_nbrs) + 1, 1_000_001):
            cups_nbrs.append(Cup(i, None, None))

    cups_arrengement = {}
    for idx, cup in enumerate(cups_nbrs):
        if idx - 1 >= 0:
            cup.prev_cup = cups_nbrs[idx - 1]
        else:
            cup.prev_cup = cups_nbrs[-1]

        if idx + 1 < len(cups_nbrs):
            cup.next_cup = cups_nbrs[idx + 1]
        else:
            cup.next_cup = cups_nbrs[0]

        cups_arrengement[cup.cup_nbr] = cup
    return cups_arrengement


def print_cup_arrengement(current_cup):
    cup_nbr_order = []
    tmp_cup = current_cup
    while str(tmp_cup.cup_nbr) not in cup_nbr_order:
        cup_nbr_order.append(str(tmp_cup.cup_nbr))
        next_cup = tmp_cup.next_cup
        tmp_cup = next_cup
    cup_nbr_order.remove(str(current_cup.cup_nbr))
    cup_nbr_order.insert(0, "(" + str(current_cup.cup_nbr) + ")")

    print("cups: " + ' '.join(cup_nbr_order))


def get_sol1_output(cups_arrengement):
    cup = cups_arrengement[1]
    sol_1_output = []
    tmp_cup = cup.next_cup
    while tmp_cup.cup_nbr != 1:
        sol_1_output.append(str(tmp_cup.cup_nbr))
        next_cup = tmp_cup.next_cup
        tmp_cup = next_cup
    return ''.join(sol_1_output)


def main():
    input_data = list(map(int, open('input.txt', "r").read()))
    for is_part1 in [True, False]:

        if is_part1:
            print()
            print("Running solution 1...")
            print()
        else:
            print()
            print("Running solution 2...")
            print()
        cups_arrengement = get_cup_arrengement(input_data, is_part1)

        current_cup = cups_arrengement[input_data[0]]
        max_nbr_cup = max(cups_arrengement.keys())
        min_nbr_cup = min(cups_arrengement.keys())

        if is_part1:
            moves = 100
        else:
            moves = 10_000_000

        for i in range(moves):

            dest_cup_nbr = current_cup.cup_nbr - 1
            if dest_cup_nbr < min_nbr_cup:
                dest_cup_nbr = max_nbr_cup

            first_cup: Cup = current_cup.next_cup
            first_cup_nbr = first_cup.cup_nbr
            second_cup: Cup = first_cup.next_cup
            second_cup_nbr = second_cup.cup_nbr
            third_cup: Cup = second_cup.next_cup
            third_cup_nbr = third_cup.cup_nbr

            while dest_cup_nbr == first_cup_nbr or dest_cup_nbr == second_cup_nbr or dest_cup_nbr == third_cup_nbr:
                dest_cup_nbr -= 1
                if dest_cup_nbr < min_nbr_cup:
                    dest_cup_nbr = max_nbr_cup

            if is_part1:
                print("-- move " + str(i + 1) + " --")
                print_cup_arrengement(current_cup)
                print("pick up: " + str(first_cup_nbr) + ", " + str(second_cup_nbr) + ", " + str(third_cup_nbr))
                print("destination: " + str(dest_cup_nbr))
                print()

            fourth_cup: Cup = third_cup.next_cup

            # Fix chain where 3 removed cups
            current_cup.next_cup = fourth_cup
            fourth_cup.prev_cup = current_cup

            # Insert the 3 cups
            destination_cup = cups_arrengement[dest_cup_nbr]
            next_after_dest_cup: Cup = destination_cup.next_cup

            destination_cup.next_cup = first_cup
            first_cup.prev_cup = destination_cup

            next_after_dest_cup.prev_cup = third_cup
            third_cup.next_cup = next_after_dest_cup

            # Continue to next cup
            current_cup = current_cup.next_cup

        if is_part1:
            print("-- final --")
            print_cup_arrengement(current_cup)
            print()
            sol_1 = get_sol1_output(cups_arrengement)
            print("Solution 1: " + sol_1)
        else:
            cup_1 = cups_arrengement[1]
            print("Solution 2: " + str(cup_1.next_cup.cup_nbr * cup_1.next_cup.next_cup.cup_nbr))


if __name__ == "__main__":
    main()
