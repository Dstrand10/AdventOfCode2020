class Accumulator:
    def __init__(self, input_data):
        self.global_value = 0
        self.input_data = input_data
        self.cursor = 0
        self.visited_commands = []
        self.inf_loop = False

    def run(self):
        while True:
            self.executeRowCommand()
            if self.cursor in self.visited_commands:
                self.inf_loop = True
                break
            elif self.cursor == len(self.input_data):
                break
        return self

    def executeRowCommand(self):

        self.visited_commands.append(int(self.cursor))

        row_command = self.input_data[self.cursor]
        operation = str(row_command).split(" ")[0]
        amount = None
        amount_with_sign = str(row_command).split(" ")[1]
        if amount_with_sign[0] == "+":
            amount = int(amount_with_sign[1:])
        elif amount_with_sign[0] == "-":
            amount = -1 * int(amount_with_sign[1:])

        if operation == "nop":
            self.executeNop()
        elif operation == "acc":
            self.executeAcc(amount)
        elif operation == "jmp":
            self.executeJmp(amount)

    def executeNop(self):
        self.cursor += 1

    def executeAcc(self, amount):
        self.global_value += amount
        self.cursor += 1

    def executeJmp(self, amount):
        self.cursor += amount
