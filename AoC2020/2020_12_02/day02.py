def find_valid_passwords_first_method(input_data):
    count_valid_pws = 0
    for pw_row in input_data:
        criteria, pw = pw_row.split(": ")
        lowerBound, _ = criteria.split("-")
        ph_1, letter = criteria.split(" ")
        _, upperBound = ph_1.split("-")
        if int(lowerBound) <= pw.count(letter) <= int(upperBound):
            count_valid_pws += 1
    return count_valid_pws


def find_valid_passwords_second_method(input_data):
    count_valid_pws = 0
    for pw_row in input_data:
        criteria, pw = pw_row.split(": ")
        lowerIndex, _ = criteria.split("-")
        ph_1, letter = criteria.split(" ")
        _, upperIndex = ph_1.split("-")
        if (pw[int(lowerIndex) - 1] == letter or pw[int(upperIndex) - 1] == letter) and pw[int(lowerIndex) - 1] != pw[
            int(upperIndex) - 1]:
            count_valid_pws += 1
    return count_valid_pws


def main():
    with open('input.txt') as f:
        input_data = list(map(str, f))
        nbr_of_valid_pws = find_valid_passwords_first_method(input_data)
        print(nbr_of_valid_pws)

        nbr_of_valid_pws_2 = find_valid_passwords_second_method(input_data)
        print(nbr_of_valid_pws_2)


if __name__ == "__main__":
    main()
