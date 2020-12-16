class TicketSystem:

    def __init__(self, rules: list[str], your_ticket: list[str], nearby_tickets: list[str]):

        self.all_available_nbrs = set()
        self.own_ticket = list(map(int, your_ticket[1].split(",")))
        self.ticket_length = len(self.own_ticket)

        self.rules = []
        for rule in rules:
            name = rule.split(": ")[0]
            nbr_set = set()
            for str_range in rule.split(": ")[1].split(" or "):
                nbr_range = range(int(str_range.split("-")[0]), int(str_range.split("-")[1]) + 1)
                nbr_set.update(nbr_range)
                self.all_available_nbrs.update(nbr_range)
            self.rules.append((name, nbr_set))

        self.other_tickets = []
        for nearby_ticket in nearby_tickets[1:]:
            self.other_tickets.append(list(map(int, nearby_ticket.split(","))))

    # Finding numbers in tickets which can't fit in in any field range
    def find_false_nbrs_sol1(self):
        not_available_nbrs = []
        for other_ticket in self.other_tickets:
            for nbr in other_ticket:
                if nbr not in self.all_available_nbrs:
                    not_available_nbrs.append(nbr)
        return not_available_nbrs

    def discard_ticket(self, ticket):
        for nbr in ticket:
            if nbr not in self.all_available_nbrs:
                return True
        return False

    def figure_out_fields_sol2(self):

        # Discarding not valid tickets
        tickets_working = [ticket for ticket in self.other_tickets if not self.discard_ticket(ticket)]

        # Calculating possible indices for each field
        field_possible_indices = []
        for field, valid_numbers in self.rules:
            possible_idx = []
            for idx in range(0, self.ticket_length):
                can_still_be_rule = True
                for ticket in tickets_working:
                    if ticket[idx] not in valid_numbers:
                        can_still_be_rule = False
                        break
                if can_still_be_rule:
                    possible_idx.append(idx)
            field_possible_indices.append((field, possible_idx))

        # Working out the possible indices for the fields
        fields_with_idex_done = []
        while len(fields_with_idex_done) < self.ticket_length:
            # Checking for fields which only can have 1 specific index
            field_with_decided_index = list(filter(lambda x: len(x[1]) == 1, field_possible_indices))[0]
            name = str(field_with_decided_index[0])
            idx = int(field_with_decided_index[1][0])
            fields_with_idex_done.append((name, idx))

            field_possible_indices.remove(field_with_decided_index)
            for _, possible_idxs in field_possible_indices:
                possible_idxs.remove(idx)

        # Filtering out fields starting with 'departure' and their indices. Then calculating the product for the numbers
        # on my own ticket using said indices.
        departure_list = list(filter(lambda x: str(x[0]).startswith("departure"), fields_with_idex_done))
        total_prod = 1
        for name, idx in departure_list:
            own_ticket_nbr = self.own_ticket[idx]
            total_prod *= own_ticket_nbr
            # print(name + ": " + str(own_ticket_nbr))
        return total_prod


def main():
    input_data = open('input.txt', "r").read().split("\n\n")
    rules = input_data[0].split("\n")
    your_ticket = input_data[1].split("\n")
    nearby_tickets = input_data[2].split("\n")

    ticket_system = TicketSystem(rules, your_ticket, nearby_tickets)

    not_available_nbrs = ticket_system.find_false_nbrs_sol1()
    print("Solution 1: " + str(sum(not_available_nbrs)))

    sol_2 = ticket_system.figure_out_fields_sol2()
    print("Solution 2: " + str(sol_2))


if __name__ == "__main__":
    main()
