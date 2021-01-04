class Player:

    def __init__(self, input_data: str):
        input_data = input_data.split("\n")
        self.name = input_data[0]
        self.cards = list(map(int, input_data[1:]))


def play_round_sol1(player_1_cards, player_2_cards, count):
    player_1_card = player_1_cards.pop(0)
    player_2_card = player_2_cards.pop(0)

    if player_1_card > player_2_card:
        player_1_cards.append(player_1_card)
        player_1_cards.append(player_2_card)
    elif player_2_card > player_1_card:
        player_2_cards.append(player_2_card)
        player_2_cards.append(player_1_card)
    else:
        print("Something went really wrong wrong")
    count += 1

    return player_1_cards, player_2_cards, count


def calculate_score(player):
    score = 0
    for idx, card in enumerate(player.cards[::-1]):
        score += card * (idx + 1)
    return score


def play_round_sol2(player_1_cards, player_2_cards, count):
    played_rounds = []

    while player_1_cards and player_2_cards:

        if [''.join(list(map(str, player_1_cards))), ''.join(list(map(str, player_2_cards)))] in played_rounds:
            return [1], [], count
        else:
            played_rounds.append([''.join(list(map(str, player_1_cards))), ''.join(list(map(str, player_2_cards)))])

        player_1_card = player_1_cards[0]
        player_2_card = player_2_cards[0]

        if player_1_card <= len(player_1_cards[1:]) and player_2_card <= len(player_2_cards[1:]):
            p1_copy_deck = player_1_cards[1:player_1_card + 1].copy()
            p2_copy_deck = player_2_cards[1:player_2_card + 1].copy()
            p1_copy_deck, p2_copy_deck, count = play_round_sol2(p1_copy_deck, p2_copy_deck, count)
            player_1_cards.pop(0)
            player_2_cards.pop(0)
            if p1_copy_deck:
                player_1_cards.append(player_1_card)
                player_1_cards.append(player_2_card)
            elif p2_copy_deck:
                player_2_cards.append(player_2_card)
                player_2_cards.append(player_1_card)
            else:
                print("Something went really wrong")
            count += 1
        else:
            player_1_cards, player_2_cards, count = play_round_sol1(player_1_cards, player_2_cards, count)
    return player_1_cards, player_2_cards, count


def main():
    input_data = list(open('input.txt', "r").read().split("\n\n"))

    player_1 = Player(input_data[0])
    player_2 = Player(input_data[1])

    count = 0
    while player_1.cards and player_2.cards:
        play_round_sol1(player_1.cards, player_2.cards, count)
        count += 1

    if player_1.cards:
        print()
        score = calculate_score(player_1)
        print("Solution 1: Player 1 won! The score is " + str(score))
        print("The number of rounds played: " + str(count))
    elif player_2.cards:
        print()
        score = calculate_score(player_2)
        print("Solution 1: Player 2 won! The score is " + str(score))
        print("The number of rounds played: " + str(count))

    # Starting recursive combat
    player_1 = Player(input_data[0])
    player_2 = Player(input_data[1])

    count = 0
    while player_1.cards and player_2.cards:
        player_1_cards, player_2_cards, count = play_round_sol2(player_1.cards, player_2.cards, count)

    if player_1.cards:
        print()
        score = calculate_score(player_1)
        print("Solution 2: Player 1 won! The score is " + str(score))
        print("The number of rounds played: " + str(count))
    elif player_2.cards:
        print()
        score = calculate_score(player_2)
        print("Solution 2: Player 2 won! The score is " + str(score))
        print("The number of rounds played: " + str(count))

if __name__ == "__main__":
    main()
