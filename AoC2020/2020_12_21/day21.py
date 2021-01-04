class AllergenAssessment:

    def __init__(self):
        self.input_data = None
        self.food_ciphers = set()
        self.allergens = set()

        self.allergen_possible_food_ciphers = {}

        self.allergen_food_map: dict = {}

    def parse_input_data(self, input_data):
        self.input_data = []
        for row in input_data:
            food_ciphers = set(row.split(" (")[0].split(" "))
            self.input_data.append(food_ciphers)
            allergens = set()
            if " (" in row:
                allergens = str(row.split(" (")[1]).replace(")", "")
                allergens = allergens.replace("contains ", "")
                allergens = set(allergens.split(", "))

            for food_cipher in food_ciphers:
                self.food_ciphers.add(food_cipher)
            for allergen in allergens:
                self.allergens.add(allergen)

                if allergen in self.allergen_possible_food_ciphers.keys():
                    possible_food_ciphers = self.allergen_possible_food_ciphers[allergen]
                    self.allergen_possible_food_ciphers[allergen] = set(
                        possible_food_ciphers.intersection(food_ciphers))
                else:
                    self.allergen_possible_food_ciphers[allergen] = food_ciphers

    def get_non_allergen_food(self):
        non_allergen_food = self.food_ciphers

        for food_cipher in self.allergen_food_map.values():
            non_allergen_food.remove(food_cipher)

        return non_allergen_food

    def count_occurances(self, foods):
        count = 0

        for food in foods:
            count += len([x for x in self.input_data if food in x])

        return count

    def calculate_allergen_food_cipher_pairs(self):

        allergen_possible_foods = self.allergen_possible_food_ciphers.copy()

        allergen_food = {}

        while allergen_possible_foods:
            allergen_tmp = None
            food_tmp = None
            for allergen, foods in allergen_possible_foods.items():
                if len(foods) == 1:
                    allergen_tmp = allergen
                    food_tmp = list(foods)[0]
                    allergen_food[allergen_tmp] = food_tmp
                    break

            del allergen_possible_foods[allergen_tmp]
            for left_foods in allergen_possible_foods.values():
                if food_tmp in left_foods:
                    left_foods.remove(food_tmp)

        self.allergen_food_map = allergen_food

    def get_dangerous_ingredients_list(self):
        allergen_foods_list = list(self.allergen_food_map.items())
        allergen_foods_list.sort()
        return ','.join([x[1] for x in allergen_foods_list])


def main():
    input_data = list(open('input.txt', "r").read().split("\n"))

    allergen_assessment = AllergenAssessment()
    allergen_assessment.parse_input_data(input_data)

    allergen_assessment.calculate_allergen_food_cipher_pairs()
    non_allergen_food = allergen_assessment.get_non_allergen_food()

    count_occurances = allergen_assessment.count_occurances(non_allergen_food)

    dangerous_ingredients_list = allergen_assessment.get_dangerous_ingredients_list()

    print("Solution 1: " + str(count_occurances))
    print("Solution 2: " + str(dangerous_ingredients_list))


if __name__ == "__main__":
    main()
