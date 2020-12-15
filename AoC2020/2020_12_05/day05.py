class Seat:

    def __init__(self, input_data):
        self.seatID = None
        self.input_data = input_data
        self.calculateSeatID()

    def calculateSeatID(self):
        row_data = self.input_data[:7]
        seat_data = self.input_data[7:]

        rowID = range(0, 128)
        leftRightID = range(0, 8)
        for char in row_data:
            if char == "B":
                rowID = rowID[int(len(rowID) / 2):]
            elif char == "F":
                rowID = rowID[:int(len(rowID) / 2)]
            else:
                print("Unknown character or something else went wrong: " + char)
        for char in seat_data:
            if char == "L":
                leftRightID = leftRightID[:int(len(leftRightID) / 2)]
            elif char == "R":
                leftRightID = leftRightID[int(len(leftRightID) / 2):]
            else:
                print("Unknown character or something else went wrong: " + char)
        self.seatID = (rowID[0]) * 8 + leftRightID[0]


def sol2(seats):
    seatIDs = [seat.seatID for seat in seats]
    seatIDs.sort()
    for index, seatID in enumerate(seatIDs):
        if seatIDs[index + 1] - seatID > 1:
            return int((seatIDs[index + 1] + seatID) / 2)


def getSeats(input_data):
    seats = []
    for line in input_data:
        seat = Seat(line)
        seats.append(seat)
    return seats


def main():
    input_data = open("input.txt").read().split("\n")

    seats = getSeats(input_data)
    largestSeatID = max([seat.seatID for seat in seats])
    print("The largest seatID found in the plane is: " + str(largestSeatID))

    mySeat = sol2(seats)
    print("Our seat is located at: " + str(mySeat))


if __name__ == "__main__":
    main()
