import os

def load_maze(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return [list(line.rstrip()) for line in f]

def display_maze(maze, player_pos):
    os.system('cls' if os.name == 'nt' else 'clear')
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if (y, x) == player_pos:
                print('P', end='')
            else:
                print(cell, end='')
        print()

def move_player(maze, pos, direction):
    y, x = pos
    moves = {'w': (-1, 0), 's': (1, 0), 'a': (0, -1), 'd': (0, 1)}
    dy, dx = moves.get(direction, (0, 0))
    new_y, new_x = y + dy, x + dx
    if maze[new_y][new_x] != '#':
        return new_y, new_x
    return y, x

def find_start(maze):
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == 'S':
                return y, x
    return None

def is_goal(maze, pos):
    y, x = pos
    return maze[y][x] == 'G'

def start_game():
    maze = load_maze("map.txt")
    player_pos = find_start(maze)

    while True:
        display_maze(maze, player_pos)
        if is_goal(maze, player_pos):
            print("탈출 성공!")
            break
        move = input("이동(w/a/s/d): ").lower()
        if move in ['w', 'a', 's', 'd']:
            player_pos = move_player(maze, player_pos, move)

if __name__ == "__main__":
    start_game()
