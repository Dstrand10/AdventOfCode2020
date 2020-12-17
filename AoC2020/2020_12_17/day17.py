class ConwayCubesGame:

    def __init__(self, init_state):
        self.current_state = []
        self.init_state = init_state
        self.current_state.append((0, init_state))

        self.current_range_x = None
        self.current_range_y = None
        self.current_range_z = None

    def run_solution_1(self):
        self.current_range_z = range(min([x[0] for x in self.current_state]),
                                     max([x[0] for x in self.current_state]) + 1)
        self.current_range_y = range(len(self.current_state[0][1]))
        self.current_range_x = range(len(self.current_state[0][1][0]))

        next_range_z = range(min([x[0] for x in self.current_state]) - 1, max([x[0] for x in self.current_state]) + 2)
        next_range_y = range(-1, len(self.current_state[0][1]) + 2)
        next_range_x = range(-1, len(self.current_state[0][1][0]) + 2)

        active_coords = []
        for z in next_range_z:
            for y in next_range_y:
                for x in next_range_x:
                    if self.coord_active_sol_1(z, y, x):
                        active_coords.append((z, y, x))

        # Dirty way of creating the next space state
        next_space_state = []
        xy_plane = []
        for i in range(max(next_range_y) + 1):
            xy_plane.append('.' * (max(next_range_x) + 1))
        for j in next_range_z:
            next_space_state.append((j, xy_plane.copy()))

        for active_coord in active_coords:
            z = active_coord[0]
            y = active_coord[1] + 1
            x = active_coord[2] + 1
            z_plane = list(filter(lambda z_var: z_var[0] == z, next_space_state))[0][1]
            z_plane[y] = z_plane[y][:x] + '#' + z_plane[y][x + 1:]


        self.current_state = next_space_state

    def coord_active_sol_1(self, z, y, x):
        count = 0
        for z_rel in range(z - 1, z + 2):
            for y_rel in range(y - 1, y + 2):
                for x_rel in range(x - 1, x + 2):
                    if z_rel == z and y_rel == y and x_rel == x:
                        continue
                    if z_rel in self.current_range_z and y_rel in self.current_range_y and x_rel in self.current_range_x:
                        z_plane = list(filter(lambda z_var: z_var[0] == z_rel, self.current_state))[0][1]
                        if z_plane[y_rel][x_rel] == "#":
                            count += 1

        if \
                (
                        z not in self.current_range_z or y not in self.current_range_y or x not in self.current_range_x) and count == 3:
            return True
        elif z not in self.current_range_z or y not in self.current_range_y or x not in self.current_range_x:
            return False
        elif list(filter(lambda z_var: z_var[0] == z, self.current_state))[0][1][y][x] == "#" and (
                count == 2 or count == 3):
            return True
        elif list(filter(lambda z_var: z_var[0] == z, self.current_state))[0][1][y][x] == "." and count == 3:
            return True

        return False

    def run_solution_1_for_real(self):
        for i in range(6):
            self.run_solution_1()

        return self.count_activated_cubes()

    def count_activated_cubes(self):
        count = 0
        for z, xy_plane in self.current_state:
            for x in xy_plane:
                for elem in x:
                    if elem == "#":
                        count += 1
        return count


class ConwayCubesGameSmarter:

    def __init__(self, input_data):

        self.input_data = input_data
        self.current_state = {}

        self.current_range_w = None
        self.current_range_z = None
        self.current_range_y = None
        self.current_range_x = None

    def init_starting_state(self):
        for idx_y, y in enumerate(self.input_data):
            for idx_x, elem in enumerate(y):
                if elem == "#":
                    self.current_state[(idx_y, idx_x, 0, 0)] = elem

        self.current_range_w = range(min([x[3] for x in self.current_state.keys()]),
                                     max([x[3] for x in self.current_state.keys()]) + 1)
        self.current_range_z = range(min([x[2] for x in self.current_state.keys()]),
                                     max([x[2] for x in self.current_state.keys()]) + 1)
        self.current_range_y = range(min([x[0] for x in self.current_state.keys()]),
                                     max([x[0] for x in self.current_state.keys()]) + 1)
        self.current_range_x = range(min([x[1] for x in self.current_state.keys()]),
                                     max([x[1] for x in self.current_state.keys()]) + 1)

    def run_solution_2(self):

        self.init_starting_state()
        for i in range(6):
            self.calculate_next_state()
        return len([x for x in self.current_state.values() if x == "#"])

    def calculate_next_state(self):

        next_range_w = range(min(self.current_range_w) - 1, max(self.current_range_w) + 2)
        next_range_z = range(min(self.current_range_z) - 1, max(self.current_range_z) + 2)
        next_range_y = range(min(self.current_range_y) - 1, max(self.current_range_y) + 2)
        next_range_x = range(min(self.current_range_x) - 1, max(self.current_range_x) + 2)

        next_state = {}
        for w in next_range_w:
            for z in next_range_z:
                for y in next_range_y:
                    for x in next_range_x:
                        if self.coord_active_sol_2(y, x, z, w):
                            next_state[(y, x, z, w)] = "#"

        self.current_state = next_state
        self.current_range_w = next_range_w
        self.current_range_z = next_range_z
        self.current_range_y = next_range_y
        self.current_range_x = next_range_x

    def coord_active_sol_2(self, y, x, z, w):
        count = 0
        for w_rel in range(w - 1, w + 2):
            for z_rel in range(z - 1, z + 2):
                for y_rel in range(y - 1, y + 2):
                    for x_rel in range(x - 1, x + 2):
                        if w_rel == w and z_rel == z and y_rel == y and x_rel == x:
                            continue
                        if self.current_state.get((y_rel, x_rel, z_rel, w_rel)) == "#":
                            count += 1
                        if count > 3:
                            return False

        if self.current_state.get((y, x, z, w)) is None and count == 3:
            return True
        elif self.current_state.get((y, x, z, w)) == "#" and (count == 2 or count == 3):
            return True
        else:
            return False

    def pretty_print(self):

        for w in self.current_range_w:
            for z in self.current_range_z:
                print("z = " + str(z) + " w = " + str(w))
                for y in self.current_range_y:
                    print_string = ''
                    for x in self.current_range_x:
                        if self.current_state.get((y, x, z, w)) == '#':
                            print_string = print_string + "#"
                        else:
                            print_string = print_string + "."
                    print(print_string)


def main():
    input_data = open('input.txt', "r").read().split("\n")

    conway_cube = ConwayCubesGame(input_data)
    sol1 = conway_cube.run_solution_1_for_real()


    conway_cube = ConwayCubesGameSmarter(input_data)
    sol2 = conway_cube.run_solution_2()
    #conway_cube.pretty_print()

    print("Solution 1: " + str(sol1))
    print("Solution 2: " + str(sol2))


if __name__ == "__main__":
    main()
