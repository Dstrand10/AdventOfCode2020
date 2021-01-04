def get_tile_paths(input_data):
    tile_paths = []
    for row in input_data:
        tile_path = []
        while row:
            if row[0] == "e" or row[0] == "w":
                tile_path.append(row[0])
                row = row[1:]
            else:
                tile_path.append(row[0:2])
                row = row[2:]
        tile_paths.append(tile_path)
    return tile_paths


def get_tiles_flipped(tile_paths):
    tile_flipped_coords = []
    for tile_path in tile_paths:
        ref_coord = [0, 0]
        for operation in tile_path:
            if operation == "ne":
                ref_coord[0] += 0.5
                ref_coord[1] += 0.5
            elif operation == "e":
                ref_coord[0] += 1
            elif operation == "se":
                ref_coord[0] += 0.5
                ref_coord[1] -= 0.5
            elif operation == "sw":
                ref_coord[0] -= 0.5
                ref_coord[1] -= 0.5
            elif operation == "w":
                ref_coord[0] -= 1
            elif operation == "nw":
                ref_coord[0] -= 0.5
                ref_coord[1] += 0.5
        tile_flipped_coords.append(ref_coord)
    return tile_flipped_coords


def calculate_black_tiles(tiles_flipped):
    tiles_flipped = list(map(tuple, tiles_flipped))
    tiles = {}

    for tile_flipped in tiles_flipped:
        if tile_flipped not in tiles.keys():
            tiles[tile_flipped] = 1
        else:
            tiles[tile_flipped] += 1

    return [x for x, y in tiles.items() if y % 2 == 1]


def get_nbr_black_adjacent_tiles(tile, black_tiles):

    count = 0
    adj_tiles = adjacent_tiles(tile)

    for adj_tile in adj_tiles:
        if adj_tile in black_tiles:
            count += 1

    return count


def get_black_to_white_tiles(black_tiles):
    black_to_white = []
    for black_tile in black_tiles:
        nbr_of_black_adjacent_tiles = get_nbr_black_adjacent_tiles(black_tile, black_tiles)
        if nbr_of_black_adjacent_tiles == 0 or nbr_of_black_adjacent_tiles > 2:
            black_to_white.append(black_tile)

    return black_to_white


def adjacent_tiles(black_tile):
    return [(black_tile[0] + 0.5, black_tile[1] + 0.5), (black_tile[0] + 1, black_tile[1]),
            (black_tile[0] + 0.5, black_tile[1] - 0.5), (black_tile[0] - 0.5, black_tile[1] - 0.5),
            (black_tile[0] - 1, black_tile[1]), (black_tile[0] - 0.5, black_tile[1] + 0.5)]


def get_white_to_black_tiles(black_tiles):
    white_tiles = set()
    white_to_black = set()

    for black_tile in black_tiles:
        adj_tiles = adjacent_tiles(black_tile)
        for adj_tile in adj_tiles:
            if adj_tile not in black_tiles:
                white_tiles.add(adj_tile)

    for white_tile in white_tiles:
        nbr_of_black_tiles = get_nbr_black_adjacent_tiles(white_tile, black_tiles)
        if nbr_of_black_tiles == 2:
            white_to_black.add(white_tile)
    return white_to_black


def main():
    input_data = open('input.txt', "r").read().split("\n")

    tile_paths = get_tile_paths(input_data)

    tiles_flipped = get_tiles_flipped(tile_paths)

    black_tiles = calculate_black_tiles(tiles_flipped)
    black_tiles = set(black_tiles)

    solution_1 = len(black_tiles)

    iterations = range(100)

    for iteration in iterations:
        black_to_white_tiles = get_black_to_white_tiles(black_tiles)

        white_to_black_tiles = get_white_to_black_tiles(black_tiles)

        for black_to_white_tile in black_to_white_tiles:
            black_tiles.remove(black_to_white_tile)

        for white_to_black_tile in white_to_black_tiles:
            black_tiles.add(white_to_black_tile)
        print("Day " + str(iteration + 1) + ": " + str(len(black_tiles)))

    solution_2 = len(black_tiles)

    print()
    print("Solution 1: " + str(solution_1))
    print("Solution 2: " + str(solution_2))


if __name__ == "__main__":
    main()
