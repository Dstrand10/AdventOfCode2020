from _operator import add
from copy import deepcopy


class GameOfSeats:

    def __init__(self, input_matrix):
        self.seatmatrix2 = None
        self.seatmatrix = deepcopy(input_matrix)
        self.width = len(input_matrix[0])
        self.height = len(input_matrix)
        self.next_seatmatrix = deepcopy(input_matrix)
        self.become_empty_threshold = 5

    def run(self):
        while True:
            # Solution 1
            # should_become_seated = self.findEmptySetsToBeSeated1()
            # self.updateEmptySeat(should_become_seated)
            # should_become_available = self.findTakenSeatsToBecomeAvailable()
            # self.updateTakenSeat(should_become_available)

            # Solution 2
            should_become_seated_2 = self.findEmptySeatsToBeSeated2()
            self.updateEmptySeat(should_become_seated_2)
            should_become_available_2 = self.findTakenSeatsToBecomeAvailable2()
            self.updateTakenSeat(should_become_available_2)

            if self.matrices_are_the_same():
                break
            else:
                for row in self.seatmatrix:
                    print(''.join(row))
                print("------------------------------------------")
            self.seatmatrix = deepcopy(self.next_seatmatrix)

        return self

    def findEmptySetsToBeSeated1(self):
        empty_seats_to_be_seated = []
        for row_index in range(0, self.height):
            for seat_index in range(0, self.width):
                if self.seatmatrix[row_index][seat_index] == ".":
                    continue
                elif self.shouldBeSeated(row_index, seat_index):
                    empty_seats_to_be_seated.append((row_index, seat_index))
        return empty_seats_to_be_seated

    def shouldBeSeated(self, row_index, seat_index):
        for idx_up, adj_row in enumerate(range(row_index - 1, row_index + 2)):
            for idx_left, adj_seat in enumerate(range(seat_index - 1, seat_index + 2)):

                if adj_row == row_index and adj_seat == seat_index:
                    continue
                elif adj_row < 0:
                    continue
                elif adj_row > self.height - 1:
                    continue
                elif adj_seat < 0:
                    continue
                elif adj_seat > self.width - 1:
                    continue

                if self.seatmatrix[adj_row][adj_seat] == ".":
                    continue
                elif self.seatmatrix[adj_row][adj_seat] == "#":
                    return False
        return True

    def updateEmptySeat(self, should_be_seated):
        for seat in should_be_seated:
            self.next_seatmatrix[seat[0]][seat[1]] = "#"

    def findTakenSeatsToBecomeAvailable(self):
        taken_seats_to_become_available = []
        for row_index in range(0, self.height):
            for seat_index in range(0, self.width):
                if self.seatmatrix[row_index][seat_index] == ".":
                    continue
                elif self.shouldBeAvailable(row_index, seat_index):
                    taken_seats_to_become_available.append((row_index, seat_index))
        return taken_seats_to_become_available

    def shouldBeAvailable(self, row_index, seat_index):

        count = 0
        for adj_row in range(row_index - 1, row_index + 2):
            for adj_seat in range(seat_index - 1, seat_index + 2):

                if adj_row == row_index and adj_seat == seat_index:
                    continue
                elif adj_row < 0:
                    continue
                elif adj_row > self.height - 1:
                    continue
                elif adj_seat < 0:
                    continue
                elif adj_seat > self.width - 1:
                    continue

                if self.seatmatrix[adj_row][adj_seat] == ".":
                    continue
                elif self.seatmatrix[adj_row][adj_seat] == "#":
                    count += 1
        return count >= self.become_empty_threshold

    def updateTakenSeat(self, should_become_available):
        for seat in should_become_available:
            self.next_seatmatrix[seat[0]][seat[1]] = "L"

    def matrices_are_the_same(self):
        for row_id, row_next in enumerate(self.next_seatmatrix):
            for seat_id, seat_next in enumerate(row_next):
                if self.seatmatrix[row_id][seat_id] is not self.next_seatmatrix[row_id][seat_id]:
                    return False
        return True

    def findEmptySeatsToBeSeated2(self):
        empty_seats_to_be_seated = []
        for row_index in range(0, self.height):
            for seat_index in range(0, self.width):
                if self.seatmatrix[row_index][seat_index] == ".":
                    continue
                elif self.shouldBeSeated2((row_index, seat_index)):
                    empty_seats_to_be_seated.append((row_index, seat_index))
        return empty_seats_to_be_seated

    def shouldBeSeated2(self, coord):

        for x_dir in range(-1, 2):
            for y_dir in range(-1, 2):
                if y_dir == 0 and x_dir == 0:
                    continue
                direction = (x_dir, y_dir)
                if self.canTakenSeatBeSeen(coord, direction):
                    return False
        return True

    def canTakenSeatBeSeen(self, coord, direction):

        coord_to_check = list(map(add, coord, direction))
        while True:
            if 0 <= coord_to_check[0] < self.height and 0 <= coord_to_check[1] < self.width:
                if self.seatmatrix[coord_to_check[0]][coord_to_check[1]] == ".":
                    coord_to_check = list(map(add, coord_to_check, direction))
                    continue
                elif self.seatmatrix[coord_to_check[0]][coord_to_check[1]] == "L":
                    return False
                elif self.seatmatrix[coord_to_check[0]][coord_to_check[1]] == "#":
                    return True
            return False

    def findTakenSeatsToBecomeAvailable2(self):
        taken_seats_to_become_available = []
        for row_index in range(0, self.height):
            for seat_index in range(0, self.width):
                if self.seatmatrix[row_index][seat_index] == "." or self.seatmatrix[row_index][seat_index] == "L":
                    continue
                elif self.shouldBeAvailable2((row_index, seat_index)) >= self.become_empty_threshold:
                    taken_seats_to_become_available.append((row_index, seat_index))
        return taken_seats_to_become_available

    def shouldBeAvailable2(self, coord):
        count = 0

        for x_dir in range(-1, 2):
            for y_dir in range(-1, 2):
                if y_dir == 0 and x_dir == 0:
                    continue
                direction = (x_dir, y_dir)
                count += self.canSeatBecomeFree(coord, direction)

        return count

    def canSeatBecomeFree(self, coord, direction):
        coord_to_check = list(map(add, coord, direction))
        while True:
            if 0 <= coord_to_check[0] < self.height and 0 <= coord_to_check[1] < self.width:
                if self.seatmatrix[coord_to_check[0]][coord_to_check[1]] == ".":
                    coord_to_check = list(map(add, coord_to_check, direction))
                    continue
                elif self.seatmatrix[coord_to_check[0]][coord_to_check[1]] == "L":
                    return 0
                elif self.seatmatrix[coord_to_check[0]][coord_to_check[1]] == "#":
                    return 1
            return 0


def main():
    input_data = open('input.txt', "r").read().split("\n")
    input_matrix = []
    for row in input_data:
        input_matrix.append(list(row))

    # print(input_matrix)
    gos = GameOfSeats(input_matrix)
    gos.run()
    count_taken_seats = 0
    for row in gos.seatmatrix:
        for seat in row:
            if seat == "#":
                count_taken_seats += 1
    print(count_taken_seats)


if __name__ == "__main__":
    main()
