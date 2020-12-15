import numpy as np


class Ship:

    def __init__(self, input_data):
        self.direction = 0
        self.x_coord = 0
        self.y_coord = 0
        self.input_data = input_data
        self.waypoint = [10, 1]

    def travel_with_waypoint(self):
        self.x_coord = 0
        self.y_coord = 0
        for instruction in self.input_data:
            cmd = instruction[0]
            nbr = int(instruction[1:])
            if cmd == "N":
                self.waypoint[1] += nbr
            elif cmd == "S":
                self.waypoint[1] -= nbr
            elif cmd == "W":
                self.waypoint[0] -= nbr
            elif cmd == "E":
                self.waypoint[0] += nbr
            elif cmd == "R":
                tmp_x = self.waypoint[0] * np.cos(np.deg2rad(nbr)) + self.waypoint[1] * np.sin(
                    np.deg2rad(nbr))
                tmp_y = - self.waypoint[0] * np.sin(np.deg2rad(nbr)) + self.waypoint[1] * np.cos(
                    np.deg2rad(nbr))
                self.waypoint = [tmp_x, tmp_y]
            elif cmd == "L":
                tmp_x = self.waypoint[0] * np.cos(np.deg2rad(nbr)) - self.waypoint[1] * np.sin(
                    np.deg2rad(nbr))
                tmp_y = self.waypoint[0] * np.sin(np.deg2rad(nbr)) + self.waypoint[1] * np.cos(
                    np.deg2rad(nbr))
                self.waypoint = [tmp_x, tmp_y]
            elif cmd == "F":
                self.x_coord += nbr * self.waypoint[0]
                self.y_coord += nbr * self.waypoint[1]
            else:
                print("Something went wrong when parsing instruction, check it out: " + str(instruction))

    def travel(self):
        self.x_coord = 0
        self.y_coord = 0
        for instruction in self.input_data:
            cmd = instruction[0]
            nbr = int(instruction[1:])
            if cmd == "N":
                self.y_coord += nbr
            elif cmd == "S":
                self.y_coord -= nbr
            elif cmd == "W":
                self.x_coord -= nbr
            elif cmd == "E":
                self.x_coord += nbr
            elif cmd == "R":
                self.direction -= nbr
            elif cmd == "L":
                self.direction += nbr
            elif cmd == "F":
                self.x_coord += nbr * np.cos(np.deg2rad(self.direction))
                self.y_coord += nbr * np.sin(np.deg2rad(self.direction))
            else:
                print("Something went wrong when parsing instruction, check it out: " + str(instruction))



def main():
    input_data = open('input.txt', "r").read().split("\n")
    ship = Ship(input_data)

    # Solution 1
    ship.travel()
    print("Coordinates at x: " + str(round(ship.x_coord)) + " and y: " + str(
        round(ship.y_coord)) + " with a Manhattan distance of: " + str(round(abs(ship.x_coord) + abs(ship.y_coord))))
    ship.travel_with_waypoint()
    print("Coordinates at x: " + str(round(ship.x_coord)) + " and y: " + str(
        round(ship.y_coord)) + " with a Manhattan distance of: " + str(round(abs(ship.x_coord) + abs(ship.y_coord))))


if __name__ == "__main__":
    main()
