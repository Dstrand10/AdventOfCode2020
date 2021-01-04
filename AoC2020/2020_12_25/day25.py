import numpy as np


def handshake(subject_nbr, loop_size):
    remainder = 20201227
    return pow(subject_nbr, loop_size, remainder)


def handshake_2(subject_nbr, loop_size):
    value = 1
    remainder = 20201227
    for i in range(loop_size):
        value *= subject_nbr
        value = value % remainder
    return value


def main():
    input_data = open('input.txt', "r").read().split("\n")
    card_public_key = int(input_data[0])
    door_public_key = int(input_data[1])
    subject_nbr = 7

    card_loop_size = -1
    door_loop_size = -1
    i = 0
    while card_loop_size < 0 or door_loop_size < 0:
        hand_shake = handshake(subject_nbr, i)
        if i % 1_000_000 == 0:
            print("Loop size: " + str(i))
        if hand_shake == card_public_key:
            card_loop_size = i
            print("Card loop size found: " + str(card_loop_size))
        elif hand_shake == door_public_key:
            door_loop_size = i
            print("Door loop size found: " + str(door_loop_size))
        i += 1

    print("Both loop sizes found card_loop_size: " + str(card_loop_size) + " door_loop_size: " + str(door_loop_size))
    encyption_key_1 = handshake_2(card_public_key, door_loop_size)
    encyption_key_2 = handshake_2(door_public_key, card_loop_size)

    if encyption_key_1 != encyption_key_2:
        print("Something went wrong, the encryption keys are not the same. Encryption_key_1: " + str(encyption_key_1) + " encryption_key_2: " + str(encyption_key_2))
    else:
        print("Solution 1: " + str(encyption_key_1))



if __name__ == "__main__":
    main()
