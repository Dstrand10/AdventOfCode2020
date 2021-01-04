import re

# Global variables
rules = {}
regexes = {}


# Initializing rules from the input data
def init_rules(rules_input):
    for rule in rules_input:
        ruler_key = int(rule.split(": ")[0])
        rule_value = rule.split(": ")[1].replace("\"", "").split(" | ")
        rules[ruler_key] = rule_value


def to_regex(rule_nbr, get_regex_func):
    rule = rules[rule_nbr]

    if len(rule) > 1:
        regex1 = "(" + ")(".join([get_regex_func(int(i)) for i in rule[0].split(" ")]) + ")"
        regex2 = "(" + ")(".join([get_regex_func(int(i)) for i in rule[1].split(" ")]) + ")"

        ans = f"({regex1})|({regex2})"

    elif 'a' in rule[0] or 'b' in rule[0]:
        ans = rule[0]

    else:
        ans = "(" + ")(".join([get_regex_func(int(i)) for i in rule[0].split(" ")]) + ")"

    return ans


def get_regex_part1(number):
    if number in regexes:
        return regexes[number]

    ans = to_regex(number, get_regex_part1)
    regexes[number] = ans
    return ans


def init_rules_8_11():
    global r8
    global r11

    r42 = get_regex_part1(42)
    r31 = get_regex_part1(31)

    r8 = f"({r42})+"
    r11s = []
    for i in range(1, 5):
        r11s.append(f"({r42}){{{i}}}({r31}){{{i}}}")
    r11 = "(" + ")|(".join(r11s) + ")"


def get_regex_part2(number):
    if number == 8:
        return r8
    elif number == 11:
        return r11
    ans = to_regex(number, get_regex_part2)
    return ans


def main():
    with open("input.txt", "r") as input_data:
        input_data = input_data.read()
        rules_input = input_data.split("\n\n")[0].split("\n")
        string_input = input_data.split("\n\n")[1].split("\n")

        init_rules(rules_input)

        for is_part1 in [True, False]:

            if is_part1:
                regex_0 = get_regex_part1(0)
                count = 0
                for string in string_input:
                    is_match = bool(re.fullmatch(regex_0, string))
                    count += is_match

                print(f"Solution 1: {count}")
            else:
                init_rules_8_11()

                regex_0 = get_regex_part2(0)
                count = 0
                for string in string_input:
                    is_match = bool(re.fullmatch(regex_0, string))
                    count += is_match

                print(f"Solution 2: {count}")


if __name__ == '__main__':
    main()
