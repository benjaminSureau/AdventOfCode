def possible_games(games):
    possible_game_ids = []
    for game_id, game in games.items():
        possible = True
        for batch in game:
            if (
                batch.get("red", 11) > 12
                or batch.get("green", 12) > 13
                or batch.get("blue", 13) > 14
            ):
                possible = False
                break
        if possible:
            possible_game_ids.append(game_id)
    return sum(possible_game_ids)


def read_games_from_file(filename):
    games = {}
    with open(filename) as file:
        for line in file:
            game_id, game_data = line.split(": ")
            game_id = int(game_id.split()[-1])
            batches = game_data.strip().split("; ")
            games[game_id] = []
            for batch in batches:
                colors = batch.split(", ")
                batch_dict = {}
                for color in colors:
                    count, _name = color.split(" ")
                    batch_dict[_name] = int(count)
                games[game_id].append(batch_dict)
    return games


# games = read_games_from_file("./2/input.txt")
# print(possible_games(games))


def calculate_power(games):
    powers = []
    for game_id, game in games.items():
        min_cubes = {"red": 0, "green": 0, "blue": 0}
        for turn in game:
            for color, count in turn.items():
                min_cubes[color] = max(min_cubes[color], count)

        power = min_cubes["red"] * min_cubes["green"] * min_cubes["blue"]

        powers.append(power)

    return sum(powers)


games = read_games_from_file("./2/input_2.txt")
print(calculate_power(games))
