import numpy as np


class JurassicJigsaw:

    def __init__(self, input_data):
        self.input_data = input_data
        self.patterns = []
        self.puzzle = None
        self.image_from_puzzle = None
        self.sea_monster_window_coord = []
        self.window_x = None
        self.window_y = None
        self.sea_monster_final_image = None

    def parse_input_data(self):
        for tile in self.input_data:
            tile_nbr = int(str(tile).split("\n")[0].split(" ")[1].split(":")[0])

            pattern = str(tile).split("\n")[1:]
            tile_pattern = np.zeros((len(pattern), len(pattern[0])))

            for idy, pattern_row in enumerate(pattern):
                for idx, elem in enumerate(pattern_row):
                    if elem == "#":
                        tile_pattern[idy, idx] = 1
            self.patterns.append([tile_nbr, tile_pattern])

    def puzzle_jigsaw_sol1(self):
        first_tile_nbr, first_jigsaw = self.patterns[0]

        puzzle = self.pad_puzzle([[(first_tile_nbr, first_jigsaw)]])
        jigsaws_left = self.patterns[1:].copy()

        while jigsaws_left:
            for jigsaw in jigsaws_left:
                tile_nbr = jigsaw[0]
                jigsaw_pattern = jigsaw[1]
                position_y, position_x, jigsaw_pattern_rotated = self.find_jigsaw(jigsaw_pattern, puzzle)
                if position_y is not None and position_x is not None and jigsaw_pattern_rotated is not None:
                    puzzle[position_y][position_x] = (tile_nbr, jigsaw_pattern_rotated)
                    jigsaws_left.remove(jigsaw)
                    break
            puzzle = self.pad_puzzle(puzzle)
        self.puzzle = puzzle

    def find_jigsaw(self, jigsaw_pattern, puzzle):

        for flip in [False, True]:
            for rotations in range(4):
                jigsaw_to_test = self.rotate_flip(jigsaw_pattern, rotations, flip)

                position_y, position_x = self.check_puzzle_sides(puzzle, jigsaw_to_test)
                if position_y is not None and position_x is not None:
                    return position_y, position_x, jigsaw_to_test
        return None, None, None

    def pad_puzzle(self, puzzle):
        pad_top = len([x for x in puzzle[0] if x is not None]) > 0
        pad_left = len([x[0] for x in puzzle if x[0] is not None]) > 0
        pad_right = len([x[len(puzzle[0]) - 1] for x in puzzle if x[len(puzzle[0]) - 1] is not None]) > 0
        pad_bottom = len([x for x in puzzle[len(puzzle) - 1] if x is not None]) > 0

        if pad_top:
            puzzle.insert(0, [None] * len(puzzle[0]))
        if pad_left:
            for row in puzzle:
                row.insert(0, None)
        if pad_right:
            for row in puzzle:
                row.append(None)
        if pad_bottom:
            puzzle.append([None] * len(puzzle[0]))

        return puzzle

    def rotate_flip(self, pattern, rotations, flip):
        pattern_tmp = []

        if flip:
            for row in pattern:
                pattern_tmp.append(row[::-1])
        else:
            pattern_tmp = pattern

        if rotations == 0:
            return pattern_tmp
        for i in range(rotations):
            pattern_tmp = list(list(x)[::-1] for x in zip(*pattern_tmp))
        return pattern_tmp

    def check_puzzle_sides(self, puzzle, jigsaw_pattern_to_try):
        for idy, row in enumerate(puzzle):
            for idx, tile in enumerate(row):
                if tile is not None:
                    tile_jigsaw = tile[1]
                    # Checking to the left
                    if puzzle[idy][idx - 1] is None:
                        jigsaw_right_side = [x[len(jigsaw_pattern_to_try[0]) - 1] for x in jigsaw_pattern_to_try]
                        tile_left_side = [y[0] for y in tile_jigsaw]
                        matching = jigsaw_right_side == tile_left_side
                        if isinstance(matching, bool):
                            pass
                        else:
                            matching = matching.all()
                        if matching:
                            return idy, idx - 1

                    # Checking top
                    if puzzle[idy - 1][idx] is None:
                        jigsaw_bottom = jigsaw_pattern_to_try[len(jigsaw_pattern_to_try) - 1]
                        tile_top = tile_jigsaw[0]
                        matching = jigsaw_bottom == tile_top
                        if isinstance(matching, bool):
                            pass
                        else:
                            matching = matching.all()
                        if matching:
                            return idy - 1, idx

                    # Checking to the right
                    if puzzle[idy][idx + 1] is None:
                        jigsaw_left_side = [x[0] for x in jigsaw_pattern_to_try]
                        tile_right_side = [y[len(tile_jigsaw[0]) - 1] for y in tile_jigsaw]
                        matching = jigsaw_left_side == tile_right_side
                        if isinstance(matching, bool):
                            pass
                        else:
                            matching = matching.all()
                        if matching:
                            return idy, idx + 1

                    # Checking bottom
                    if puzzle[idy + 1][idx] is None:
                        jigsaw_top = jigsaw_pattern_to_try[0]
                        tile_bottom = tile_jigsaw[len(tile_jigsaw) - 1]
                        matching = jigsaw_top == tile_bottom
                        if isinstance(matching, bool):
                            pass
                        else:
                            matching = matching.all()
                        if matching:
                            return idy + 1, idx
        return None, None

    def parse_puzzle_image(self):
        puzzle_to_parse = [x[1:len(x) - 1] for x in self.puzzle[1:len(self.puzzle) - 1]]

        len_y = len(puzzle_to_parse[0][0][1]) - 2
        image = []
        for i in range(len(puzzle_to_parse) * len_y):
            image.append([])

        for idy, row in enumerate(puzzle_to_parse):
            for tile in row:
                pattern = [x[1:len(x) - 1] for x in tile[1][1:len(tile[1]) - 1]]
                for pattern_idy, pattern_row in enumerate(pattern):
                    for elem in pattern_row:
                        if elem == 1:
                            elem_txt = "#"
                        else:
                            elem_txt = "."
                        image[len_y * idy + pattern_idy].append(elem_txt)

        self.image_from_puzzle = self.rotate_flip(image, 2, True)  # Just to match the test input on website

    def parse_sea_monster(self, input_sea_monster):
        sea_monster = input_sea_monster.split("\n")
        self.window_x = len(sea_monster[0])
        self.window_y = len(sea_monster)
        for idy, row in enumerate(sea_monster):
            for idx, elem in enumerate(row):
                if elem == "#":
                    self.sea_monster_window_coord.append([idy, idx])

    def check_sea_monster_in_image(self):
        image = self.image_from_puzzle.copy()

        # Check sea monsters for each rotation
        for rotation in range(4):
            image = list(list(x)[::-1] for x in zip(*image))
            self.find_sea_monsters(image)

        # Flip image
        image_tmp = []
        for row in image:
            image_tmp.append(row[::-1])
        image = image_tmp

        # Check sea monsters for each rotation
        for rotation in range(4):
            image = list(list(x)[::-1] for x in zip(*image))
            self.find_sea_monsters(image)

        # Flip back image
        image_tmp = []
        for row in image:
            image_tmp.append(row[::-1])
        image = image_tmp
        self.sea_monster_final_image = image

    def find_sea_monsters(self, image):
        for idy in range(len(image) - self.window_y):
            for idx in range(len(image[0]) - self.window_x):
                window_works = True
                for sea_monster_y_coord, sea_monster_x_coord in self.sea_monster_window_coord:
                    if image[idy + sea_monster_y_coord][idx + sea_monster_x_coord] == "#":
                        continue
                    else:
                        window_works = False
                        break
                if window_works:
                    for sea_monster_y_coord, sea_monster_x_coord in self.sea_monster_window_coord:
                        image[idy + sea_monster_y_coord][idx + sea_monster_x_coord] = "O"


def main():
    input_data = list(open('input.txt', "r").read().split("\n\n"))

    jurassic_jigsaw = JurassicJigsaw(input_data)
    jurassic_jigsaw.parse_input_data()

    jurassic_jigsaw.puzzle_jigsaw_sol1()

    product_of_corners = jurassic_jigsaw.puzzle[1][1][0] * jurassic_jigsaw.puzzle[1][len(jurassic_jigsaw.puzzle) - 2][
        0] * jurassic_jigsaw.puzzle[len(jurassic_jigsaw.puzzle[0]) - 2][1][0] * \
                         jurassic_jigsaw.puzzle[len(jurassic_jigsaw.puzzle[0]) - 2][len(jurassic_jigsaw.puzzle) - 2][0]
    print("Solution 1: " + str(product_of_corners))

    jurassic_jigsaw.parse_puzzle_image()

    input_sea_monster = open('input_sea_monster.txt', "r").read()
    jurassic_jigsaw.parse_sea_monster(input_sea_monster)

    jurassic_jigsaw.check_sea_monster_in_image()

    count = 0
    for row in jurassic_jigsaw.sea_monster_final_image:
        for elem in row:
            if elem == "#":
                count += 1
    print("Solution 2: " + str(count))


if __name__ == "__main__":
    main()
