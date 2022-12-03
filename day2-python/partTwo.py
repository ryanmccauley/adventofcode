scores = {
        'X': 1,
        'Y': 2,
        'Z': 3
}

def get_shape_from_instruction(move, instruction):
    if instruction == 'X':
        if move == 'A':
            return 'Z'
        elif move == 'B':
            return 'X'
        elif move == 'C':
            return 'Y'
    elif instruction == 'Y':
        if move == 'A':
            return 'X'
        elif move == 'B':
            return 'Y'
        elif move == 'C':
            return 'Z'
    elif instruction == 'Z':
        if move == 'A':
            return 'Y'
        elif move == 'B':
            return 'Z'
        elif move == 'C':
            return 'X'

totalScore = 0

with open('input') as file:
    for line in file.read().splitlines():
        move1, move2 = line.split(' ')
        
        shape = get_shape_from_instruction(move1, move2)
        totalScore += scores[shape]

        if move2 == 'Y':
            totalScore += 3
        elif move2 == 'Z':
            totalScore += 6

print(totalScore)
