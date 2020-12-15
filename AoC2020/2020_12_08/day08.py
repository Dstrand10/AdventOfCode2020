from Accumulator import Accumulator


def main():
    input_data = open('input.txt', "r").read().split("\n")
    acc = Accumulator.Accumulator(input_data)
    acc.run()
    print(acc.global_value)

    for index, input_row in enumerate(input_data):
        input_data_changeable = input_data.copy()
        if input_row.split(" ")[0] == "jmp":
            input_data_changeable[index] = input_data_changeable[index].replace("jmp", "nop")
        elif input_row.split(" ")[0] == "nop":
            input_data_changeable[index] = input_data_changeable[index].replace("nop", "jmp")

        acc = Accumulator.Accumulator(input_data_changeable)
        acc.run()
        if not acc.inf_loop:
            print(acc.global_value)


if __name__ == "__main__":
    main()