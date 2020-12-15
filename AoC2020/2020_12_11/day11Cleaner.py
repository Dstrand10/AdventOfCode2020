from _operator import add
from copy import deepcopy


class GameOfSeatsClean:

    def __init__(self):
        self.seat_matrix = None
        self.next_seat_matrix = None
        self.sit_threshold = None
        self.lift_threshold = None
        self.width = None
        self.height = None

        self.visited_states = []
        self.did_converge = False
        self.index_same_visited_state = None
        self.taken_seats_when_done = None

    def run_solution1(self, input_data, threshold):
        self.initData(input_data, threshold)

        while True:
            self.changeSeats(self.checkAdjacentIfSeatedExceedsThreshold)
            if self.has_state_been_visited():
                break
            self.seat_matrix = deepcopy(self.next_seat_matrix)
            self.visited_states.append(deepcopy(self.next_seat_matrix))

        self.taken_seats_when_done = [item for sublist in self.seat_matrix for item in sublist].count("#")
        print("Number of taken seats in solution 1: " + str(self.taken_seats_when_done))

    def run_solution2(self, input_data, threshold):
        self.initData(input_data, threshold)

        while True:
            self.changeSeats(self.checkEveryDirectionIfSeatedExceedsThreshold)
            if self.has_state_been_visited():
                break
            self.seat_matrix = deepcopy(self.next_seat_matrix)
            self.visited_states.append(deepcopy(self.next_seat_matrix))

        self.taken_seats_when_done = [item for sublist in self.seat_matrix for item in sublist].count("#")
        print("Number of taken seats in solution 2: " + str(self.taken_seats_when_done))

    def checkEveryDirectionIfSeatedExceedsThreshold(self, coord, find_threshold):
        count = 0
        for x_dir in range(-1, 2):
            for y_dir in range(-1, 2):
                if x_dir == 0 and y_dir == 0:
                    continue
                direction = (y_dir, x_dir)
                coord_to_check = list(map(add, coord, direction))
                while True:
                    if 0 <= coord_to_check[0] < self.height and 0 <= coord_to_check[1] < self.width:
                        if self.seat_matrix[coord_to_check[0]][coord_to_check[1]] == "#":
                            # Count 1 since you see a taken place
                            count += 1
                            break
                        if self.seat_matrix[coord_to_check[0]][coord_to_check[1]] == "L":
                            # Count nothing since you see a free place
                            break
                        if self.seat_matrix[coord_to_check[0]][coord_to_check[1]] == ".":
                            # Continue in the same direction since you see not a seat
                            coord_to_check = list(map(add, coord_to_check, direction))
                            continue
                    break
                if count >= find_threshold:
                    return True
        return False

    def checkAdjacentIfSeatedExceedsThreshold(self, coord, find_threshold):
        count = 0
        for x_rel_coord in range(-1, 2):
            for y_rel_coord in range(-1, 2):
                if x_rel_coord == 0 and y_rel_coord == 0:
                    continue
                coord_to_check = list(map(add, coord, (y_rel_coord, x_rel_coord)))
                if 0 <= coord_to_check[0] < self.height and 0 <= coord_to_check[1] < self.width:
                    if self.seat_matrix[coord_to_check[0]][coord_to_check[1]] == "#":
                        count += 1
                    if count >= find_threshold:
                        return True
        return False

    def changeSeats(self, change_seat_function):
        for x_coord in range(0, self.width):
            for y_coord in range(0, self.height):
                coord = (y_coord, x_coord)
                if self.seat_matrix[y_coord][x_coord] == "L" and not change_seat_function(coord, self.sit_threshold):
                    self.next_seat_matrix[y_coord][x_coord] = "#"
                elif self.seat_matrix[y_coord][x_coord] == "#" and change_seat_function(coord, self.lift_threshold):
                    self.next_seat_matrix[y_coord][x_coord] = "L"

    def has_state_been_visited(self):
        for index, visited_state in enumerate(self.visited_states):
            next_state_visited = True
            for row_id in range(0, self.height):
                for seat_id in range(0, self.width):
                    if visited_state[row_id][seat_id] is not self.next_seat_matrix[row_id][seat_id]:
                        next_state_visited = False
                    if not next_state_visited:
                        break
                if not next_state_visited:
                    break

            if next_state_visited:
                if index == len(self.visited_states) - 1:
                    self.did_converge = True
                else:
                    self.index_same_visited_state = index
                return True

    def initData(self, input_data, threshold):
        self.seat_matrix = input_data
        self.next_seat_matrix = deepcopy(input_data)
        self.sit_threshold = threshold[0]
        self.lift_threshold = threshold[1]
        self.width = len(input_data[0])
        self.height = len(input_data)
        self.visited_states = [deepcopy(input_data)]


def print_game_of_seats_states(gos):
    print()
    states = gos.visited_states.copy()
    states.append(gos.next_seat_matrix)

    for idx, state in enumerate(states):
        print("Index of state: " + str(idx))
        print("----------------------------------------------------------------------------------------")
        for row in state:
            print(''.join(row))
        print()

    if gos.did_converge:
        print("The series converged, meaning the last state is stable and will never change. The total amount of "
              "occupied seats are: " + str(gos.taken_seats_when_done))
    else:
        print("The series did not converge but found itself in a steady loop. The current state can also be found at "
              "index: " + str(gos.index_same_visited_state) + " which is found " + str(
            len(states) - 1 - gos.index_same_visited_state)
              + " iterations ago.")


def main():
    input_data = open('input.txt', "r").read().split("\n")
    input_matrix = []
    for row in input_data:
        input_matrix.append(list(row))

    threshold_part1 = (1, 4)
    gos = GameOfSeatsClean()
    gos.run_solution1(input_matrix, threshold_part1)

    threshold_part2 = (1, 5)
    gos.run_solution2(input_matrix, threshold_part2)
    print_game_of_seats_states(gos)


if __name__ == "__main__":
    main()
