from Passport.Passport import Passport


def sol1(passports):
    count_valid_password = 0

    for passport in passports:
        passport_parsed = []
        passport_rows = passport.split("\n")
        for passport_row in passport_rows:
            infos = passport_row.split(" ")
            for info in infos:
                passport_field, passport_data = info.split(":")
                if passport_data != "":
                    passport_parsed.append((passport_field, passport_data))
        if len(passport_parsed) == 8 or (len(passport_parsed) == 7 and "cid" not in list(map(lambda x: x[:][0], passport_parsed))):
            count_valid_password += 1
    return count_valid_password


def sol2(passports):
    count_valid_password = 0
    for passport in passports:
        passport_obj = Passport()
        passport_rows = passport.split("\n")
        for passport_row in passport_rows:
            infos = passport_row.split(" ")
            for info in infos:
                passport_field, passport_data = info.split(":")
                if passport_data != "":
                    passport_obj.set_val(passport_field, passport_data)
        if passport_obj.valid():
            count_valid_password += 1
    return count_valid_password


def main():
    with open('input.txt', "r") as f:
        passports = str(f.read()).split("\n\n")

        sol_1 = sol1(passports)
        print(sol_1)

        sol_2 = sol2(passports)
        print(sol_2)


if __name__ == "__main__":
    main()
