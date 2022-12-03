scores = {
        'X': 1,
        'Y': 2,
        'Z': 3
}

totalScore = 0

with open('input') as file:
    for line in file.read().splitlines():
        move1, move2 = line.split(' ')
        
        totalScore += scores[move2]
        
        if move1 == 'A':
            if move2 == 'Y':
                totalScore += 6
            elif move2 == 'X':
                totalScore += 3
        elif move1 == 'B':
            if move2 == 'Z':
                totalScore += 6
            elif move2 == 'Y':
                totalScore += 3
        elif move1 == 'C':
            if move2 == 'X':
                totalScore += 6
            elif move2 == 'Z':
                totalScore += 3
        
print(totalScore)
