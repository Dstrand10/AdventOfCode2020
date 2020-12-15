import itertools


class BagRule:

    def __init__(self, input_data):

        self.input_data = input_data
        self.bag_color = None
        self.total_amount_of_bags_inside = 0
        self.contain_bag_color_list = None
        self.contain_bag_color_amount_map = None

    def initBagColor(self):
        bag = self.input_data.split("contain")
        own_bag_color = str(bag[0]).split(" ")
        own_bag_color = own_bag_color[:len(own_bag_color) - 2]
        self.bag_color = ' '.join(own_bag_color)

    def initBagsInside(self):
        bag = self.input_data.split("contain")
        contain_bag_color_list = []
        contain_bag_color_amount_map = []
        contain_bag_colors = str(bag[1]).split(",")
        if len(contain_bag_colors) > 1:
            for contain_bag in contain_bag_colors:
                tmp_contain_bag = contain_bag.split(" ")
                tmp_contain_bag_color = tmp_contain_bag[2:len(tmp_contain_bag) - 1]
                tmp_contain_bag_color = ' '.join(tmp_contain_bag_color)
                amount_of_bags = tmp_contain_bag[1]
                self.total_amount_of_bags_inside += int(amount_of_bags)
                contain_bag_color_list.append(tmp_contain_bag_color)
                contain_bag_color_amount_map.append((tmp_contain_bag_color, amount_of_bags))
        elif len(contain_bag_colors) == 1 and "no other bags" not in contain_bag_colors[0]:
            tmp_contain_bag = str(contain_bag_colors).split(" ")
            tmp_contain_bag_color = tmp_contain_bag[2:len(tmp_contain_bag) - 1]
            tmp_contain_bag_color = ' '.join(tmp_contain_bag_color)
            amount_of_bags = tmp_contain_bag[1]
            self.total_amount_of_bags_inside += int(amount_of_bags)
            contain_bag_color_list.append(tmp_contain_bag_color)
            contain_bag_color_amount_map.append((tmp_contain_bag_color, amount_of_bags))
        self.contain_bag_color_list = contain_bag_color_list
        self.contain_bag_color_amount_map = contain_bag_color_amount_map

    def initBag(self):
        self.initBagColor()
        self.initBagsInside()


# Recursive formula, think of it you're stepping dow to the furthest bag while keeping count of the exponential
# development of your trail (multiply with the number of bags of the group when you travel into one). Eventually a bag
# will not contain any more bags and then you have it, the amount for that specific path. Then just travel all other
# paths as well and you will end up with the right answer. Amazeballs.
def calculateNbrOfBags(bag, bag_rules, exponential_nbr_of_bags):
    amount_of_bags = 0
    current_bag = next((x for x in bag_rules if x.bag_color == bag[0]), None)
    next_bags = current_bag.contain_bag_color_amount_map

    if len(next_bags) > 0:
        for bag in next_bags:
            next_bag_nbr = int(bag[1])
            tmp_exponential_nbr_of_bags = exponential_nbr_of_bags * next_bag_nbr
            amount_of_bags += tmp_exponential_nbr_of_bags
            amount_of_bags += calculateNbrOfBags(bag, bag_rules, tmp_exponential_nbr_of_bags)
    return amount_of_bags


def getBagRules(input_data):
    bag_rules = []
    for bag_rule_data in input_data:
        bag_rule = BagRule(bag_rule_data)
        bag_rule.initBag()
        bag_rules.append(bag_rule)
    return bag_rules


def solution_1(bag_rules):
    working_colors = set()
    color_to_check = ["shiny gold"]
    while True:
        tmp_colors_to_check = []
        for color in color_to_check:
            colors_to_check = list(map(lambda y: y.bag_color, [x for x in bag_rules if color in x.contain_bag_color_list]))
            tmp_colors_to_check.append(colors_to_check)
        tmp_colors_to_check = list(itertools.chain(*tmp_colors_to_check))  # flatmap
        if len(tmp_colors_to_check) == 0: #Finished with all colors
            break
        for color in tmp_colors_to_check:
            working_colors.add(color)
        color_to_check = tmp_colors_to_check
    return working_colors


def main():
    input_data = open('input.txt', "r").read().split("\n")

    bag_rules = getBagRules(input_data)

    working_colors = solution_1(bag_rules)
    sol1 = len(working_colors)

    print("Solution to first question. Number of working colors are: " + str(sol1))

    nbr_of_first_bag = 1
    initial_bag = ("shiny gold", nbr_of_first_bag)
    amount_of_bags = calculateNbrOfBags(initial_bag, bag_rules, nbr_of_first_bag)
    print("Solution to second question. Number of bags to buy: " + str(amount_of_bags))


if __name__ == "__main__":
    main()
