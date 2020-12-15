def get_memory_insertions_sol2(mask, mem_and_commands):
    mem_nbr_insertion = []
    for mem_and_command in mem_and_commands:
        mem = int(mem_and_command.split("] = ")[0].split("mem[")[1])
        nbr = int(mem_and_command.split("] = ")[1])
        bit_mem = bin(mem)[2:]
        bit_mem = bit_mem.rjust(36, "0")

        for index, bit in enumerate(mask):
            if mask[index] != "0":
                bit_mem = bit_mem[:index] + mask[index] + bit_mem[index + 1:]

        adresses = [bit_mem]

        for idx in range(0, len(bit_mem)):
            tmp_adress_list = []
            for adress in adresses:
                if adress[idx] == "X":
                    tmp_adress_list.append(adress[:idx] + "1" + adress[idx + 1:])
                    tmp_adress_list.append(adress[:idx] + "0" + adress[idx + 1:])
            if len(tmp_adress_list) > 0:
                adresses = tmp_adress_list

        for mem_adress in adresses:
            mem_nbr_insertion.append((int(mem_adress, 2), nbr))
    return mem_nbr_insertion


def get_memory_insertions_sol1(mask, mem_and_commands):
    mem_nbr_insertion = []
    for mem_and_command in mem_and_commands:

        mem = int(mem_and_command.split("] = ")[0].split("mem[")[1])
        nbr = int(mem_and_command.split("] = ")[1])
        bit_nbr = bin(nbr)[2:]
        bit_nbr = bit_nbr.rjust(36, "X")

        start_bit = "000000000000000000000000000000000000"
        for index, bit in enumerate(bit_nbr):
            if mask[index] != "X":
                start_bit = start_bit[:index] + mask[index] + start_bit[index + 1:]
            elif bit_nbr[index] != "X":
                start_bit = start_bit[:index] + bit_nbr[index] + start_bit[index + 1:]
        mem_nbr_insertion.append((mem, int(start_bit, 2)))

    return mem_nbr_insertion


class BitmaskSystem:

    def __init__(self):
        self.memory = {}
        self.total_in_memory = None

    def run_bitmask_sol1(self, input_data):
        for bitmask_mask_and_commands in input_data:
            mask = bitmask_mask_and_commands[0]
            mem_and_commands = bitmask_mask_and_commands[1:]
            mem_nbr_insertion = get_memory_insertions_sol1(mask, mem_and_commands)
            self.insert_in_memory(mem_nbr_insertion)

    def run_bitmask_sol2(self, input_data):
        for bitmask_mask_and_commands in input_data:
            mask = bitmask_mask_and_commands[0]
            mem_and_commands = bitmask_mask_and_commands[1:]
            mem_nbr_insertion = get_memory_insertions_sol2(mask, mem_and_commands)
            self.insert_in_memory(mem_nbr_insertion)

    def insert_in_memory(self, mem_nbr_insertion):
        for mem, nbr in mem_nbr_insertion:
            self.memory[mem] = nbr
        self.total_in_memory = sum(self.memory.values())


def main():
    input_data = open('input.txt', "r").read().split("mask = ")[1:]
    input_data_parsed = []
    for text in input_data:
        input_data_parsed.append(list(filter(None, text.split("\n"))))

    bitmask_system = BitmaskSystem()
    bitmask_system.run_bitmask_sol1(input_data_parsed)
    print("Solution 1: " + str(bitmask_system.total_in_memory))

    bitmask_system = BitmaskSystem()
    bitmask_system.run_bitmask_sol2(input_data_parsed)
    print("Solution 2: " + str(bitmask_system.total_in_memory))


if __name__ == "__main__":
    main()
