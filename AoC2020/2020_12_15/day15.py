def sol(input_data, pos):
    game_list = {}
    for idx, nbr in enumerate(input_data[:-1]):
        game_list[nbr] = idx

    said_number = input_data[-1]
    count = len(input_data) - 1

    while True:

        if said_number in game_list.keys():
            next_nbr = count - game_list[said_number]
        else:
            next_nbr = 0

        game_list[said_number] = count

        if count == pos - 1:
            return said_number

        count += 1
        said_number = next_nbr


def main():
    input_data = list(map(int, open('input.txt', "r").read().split(",")))

    sol1 = sol(input_data, 2020)
    print("Solution 1: " + str(sol1))

    sol2 = sol(input_data, 30_000_000)
    print("Solution 2: " + str(sol2))


if __name__ == "__main__":
    main()
