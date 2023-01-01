with open("data.txt", "r") as f:
    lines = f.readlines()
    plays = [play.strip() for play in lines]

"""
WIN: 6
Draw: 3
Lost: 0

A - ROCK 
B - PAPER
C - Scissors

X - ROCK - 1
Y - PAPER - 2
Z - Scissors - 3

X - lose
Y - draw
Z - win
"""

result_map = {
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6,
}

play_map = {
    "A X": "A Z",
    "A Y": "A X",
    "A Z": "A Y",
    "B X": "B X",
    "B Y": "B Y",
    "B Z": "B Z",
    "C X": "C Y",
    "C Y": "C Z",
    "C Z": "C X",
}


total_score = sum(result_map[play_map[play]] for play in plays)
print(total_score)
