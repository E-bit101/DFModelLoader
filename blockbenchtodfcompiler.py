import json

def format_positions(positions, round_to):
    formatted_positions = ', '.join('/'.join(map(lambda x: format(round(x, round_to), '.2f'), pos)) for pos in positions)
    return formatted_positions

def convert_rotation(rotation):
    return [(angle + 360) % 360 for angle in rotation]

def extract_data(json_input, round_to):
    data = json.loads(json_input)
    positions = []
    scales = []
    rotations = []

    for element in data["elements"]:
        # Extract and round position
        position = [round(x, round_to) for x in element["from"]]
        positions.append(position)

        # Extract and round scale
        scale = [round(to - from_, round_to) for to, from_ in zip(element["to"], element["from"])]
        scales.append(scale)

        # Extract and convert rotation
        rotation = convert_rotation(element.get("rotation", [0, 0, 0]))
        rotations.append(rotation)

    return positions, scales, rotations

def Run():
    json_input = input("Paste your code here: ")
    round_to = 2

    positions, scales, rotations = extract_data(json_input, round_to)

    print(format_positions(positions, round_to) + "_" + format_positions(scales, round_to) + "_" + format_positions(rotations, round_to))

    usrresponse = input("type go to run again or just press enter to close")
    if usrresponse == "go":
        Run()

Run()
