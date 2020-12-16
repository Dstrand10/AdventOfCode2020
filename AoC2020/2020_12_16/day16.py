class TicketSystem:

    def __init__(self, rules: list[str], your_ticket: list[str], nearby_tickets: list[str]):
        self.rules = {}
        self.all_available_nbrs = set()

        for rule in rules:
            name = rule.split(": ")[0]
            nbr_set = set()
            for str_range in rule.split(": ")[1].split(" or "):
                nbr_range = range(int(str_range.split("-")[0]), int(str_range.split("-")[1]) + 1)
                nbr_set.update(nbr_range)
                self.all_available_nbrs.update(nbr_range)
            self.rules[name] = nbr_set

        self.own_ticket = list(map(int, your_ticket[1].split(",")))

        self.other_tickets = []
        for nearby_ticket in nearby_tickets[1:]:
            self.other_tickets.append(list(map(int, nearby_ticket.split(","))))

        self.ticket_desc_index = {}

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

    def figure_out_fields(self):
        tickets_working = [ticket for ticket in self.other_tickets if not self.discard_ticket(ticket)]
        tickets_working.append(self.own_ticket)

        rules_position = []

        for name, values in self.rules.items():
            idx = 0
            possible_idx = []
            while idx < len(tickets_working[0]):
                can_still_be_rule = True
                for ticket in tickets_working:
                    if ticket[idx] not in values:
                        can_still_be_rule = False
                        break
                if can_still_be_rule:
                    possible_idx.append(idx)
                idx += 1
            rules_position.append((name, possible_idx))

        working_on_rules_position = rules_position.copy()
        rules_done = {}
        while len(rules_done) < len(self.own_ticket):
            tmp_list = list(filter(lambda x: len(x[1]) == 1, working_on_rules_position))
            name = tmp_list[0][0]
            idx = tmp_list[0][1][0]
            rules_done[name] = idx

            working_on_rules_position.remove(tmp_list[0])
            for rule in working_on_rules_position:
                rule[1].remove(idx)

        for key, idx in rules_done.items():
            print(key + ": " + str(self.own_ticket[idx]))


def main():
    input_data = open('input.txt', "r").read().split("\n\n")
    rules = input_data[0].split("\n")
    your_ticket = input_data[1].split("\n")
    nearby_tickets = input_data[2].split("\n")

    ticket_system = TicketSystem(rules, your_ticket, nearby_tickets)

    not_available_nbrs = ticket_system.find_false_nbrs_sol1()
    print(sum(not_available_nbrs))

    ticket_system.figure_out_fields()


if __name__ == "__main__":
    main()
