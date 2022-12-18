import random
import copy

def game_is_over(board):
  # Check if any of the rows have the same value (and it's not empty)
  for row in range(3):
    if (board[row][0] != ' ') and (board[row][0] == board[row][1] == board[row][2]):
      return True

  # Check if any of the columns have the same value (and it's not empty)
  for col in range(3):
    if (board[0][col] != ' ') and (board[0][col] == board[1][col] == board[2][col]):
      return True

  # Check if the diagonals have the same value (and it's not empty)
  if (board[0][0] != ' ') and (board[0][0] == board[1][1] == board[2][2]):
    return True
  if (board[0][2] != ' ') and (board[0][2] == board[1][1] == board[2][0]):
    return True

  if get_available_moves(board) == []:
    return True

  # If none of the previous checks returned True, the game is not over
  return False

'''
def evaluate_board(board):
  # check for winning combinations
  for i in range(3):
    # check for horizontal wins
    if board[i * 3] == board[i * 3 + 1] == board[i * 3 + 2] and board[i * 3] != " ":
      return board[i * 3]
    # check for vertical wins
    if board[i] == board[i + 3] == board[i + 6] and board[i] != " ":
      return board[i]

  # check for diagonal wins
  if board[0] == board[4] == board[8] and board[0] != " ":
    return board[0]
  if board[2] == board[4] == board[6] and board[2] != " ":
    return board[2]

  # check for a draw
  if " " not in board:
    return "DRAW"

  # no winner or draw, return empty string
  return ""
'''

def evaluate_board(board):
    # check rows
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2]:
            if board[row][0] == 'X':
                return 10
            elif board[row][0] == 'O':
                return -10
    # check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            if board[0][col] == 'X':
                return 10
            elif board[0][col] == 'O':
                return -10
    # check diagonals
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == 'X':
            return 10
        elif board[0][0] == 'O':
            return -10
    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == 'X':
            return 10
        elif board[0][2] == 'O':
            return -10
    # check for a tie
    if all(board[i][j] != ' ' for i in range(3) for j in range(3)):
        return 0
    
    # game is still ongoing
    score = 0
    # check rows
    for row in range(3):
        if board[row][0] == board[row][1]:
            if board[row][1] == 'X' and board[row][2] != 'O':
                score += 1
            elif board[row][1] == 'O' and board[row][2] != 'X':
                score -= 1
        if board[row][1] == board[row][2]:
            if board[row][1] == 'X' and board[row][2] != 'O':
                score += 1
            elif board[row][1] == 'O' and board[row][2] != 'X':
                score -= 1
        if board[row][0] == board[row][2]:
            if board[row][0] == 'X' and board[row][1] != 'O':
                score += 1
            elif board[row][0] == 'O' and board[row][1] != 'X':
                score -= 1

    # check columns
    for col in range(3):
        if board[0][col] == board[1][col]:
            if board[1][col] == 'X' and board[2][col] != 'O':
                score += 1
            elif board[1][col] == 'O' and board[2][col] != 'X':
                score -= 1
        if board[1][col] == board[2][col]:
            if board[1][col] == 'X' and board[0][col] != 'O':
                score += 1
            elif board[1][col] == 'O' and board[0][col] != 'X':
                score -= 1
        if board[0][col] == board[2][col]:
            if board[0][col] == 'X' and board[1][col] != 'O':
                score += 1
            elif board[0][col] == 'O' and board[1][col] != 'X':
                score -= 1

    # check diagonals
    if board[0][0] == board[1][1]:
        if board[1][1] == 'X' and board[2][2] != 'O':
            score += 1
        elif board[1][1] == 'O' and board[2][2] != 'X':
            score -= 1
    if board[1][1] == board[2][2]:
        if board[1][1] == 'X' and board[0][0] != 'O':
            score += 1
        elif board[1][1] == 'O' and board[0][0] != 'X':
            score -= 1
    if board[0][2] == board[1][1]:
        if board[1][1] == 'X' and board[2][0] != 'O':
            score += 1
        elif board[1][1] == 'O' and board[2][0] != 'X':
            score -= 1
    if board[1][1] == board[2][0]:
        if board[1][1] == 'X' and board[0][2] != 'O':
            score += 1
        elif board[1][1] == 'O' and board[0][2] != 'X':
            score -= 1
    if board[0][2] == board[2][0]:
        if board[0][2] == 'X' and board[1][1] != 'O':
            score += 1
        elif board[0][2] == 'O' and board[1][1] != 'X':
            score -= 1
    if board[0][0] == board[2][2]:
        if board[0][0] == 'X' and board[1][1] != 'O':
            score += 1
        elif board[0][0] == 'O' and board[1][1] != 'X':
            score -= 1

    # return a score based on who is closer to winning
    return score
    
    #return 0


def get_available_moves(board):
    available_moves = []
    
    # Iterate over each row and column in the board
    for i in range(0,len(board)):
        for j in range(0, len(board[i])):
            
            # If the current position on the board is empty
            if board[i][j] == ' ':
                
                # Add the coordinates of the empty space to the list of available moves
                available_moves.append((i, j))
                
    return available_moves

def make_move(board, move, symbol):
    # Get the available moves on the board
    available_moves = get_available_moves(board)
    
    # If the given move is not in the list of available moves, return the original board
    if move not in available_moves:
        return board
    
    # Otherwise, update the board with the player's move
    board[move[0]][move[1]] = symbol
    
    return board


def minimax(board, depth, is_maximizing):
    next_move = (0,0)
    # Check if the game is over or if we have reached the maximum depth
    if game_is_over(board) or depth == 0:
        return (evaluate_board(board),next_move)

    # If it's the maximizing player's turn, find the move that maximizes the score
    if is_maximizing:
        best_score = -float("inf")
        for move in get_available_moves(board):
            board_copy = copy.deepcopy(board)
            new_board = make_move(board_copy, move, "X")
            score = minimax(new_board, depth - 1, False)[0]
            best_score = max(best_score, score)
            if (score == best_score):
              next_move = move
        return (best_score,next_move)

    # If it's the minimizing player's turn, find the move that minimizes the score
    else:
        best_score = float("inf")
        for move in get_available_moves(board):
            board_copy = copy.deepcopy(board)
            new_board = make_move(board_copy, move, "O")
            score = minimax(new_board, depth - 1, True)[0]
            best_score = min(best_score, score)
            if (score == best_score):
              next_move = move
        return (best_score,next_move)

def decide_next_move(board):
  # Check if the middle space is empty and choose it if it is
  if board[1][1] == " ":
    return (1, 1)
  
  # Check if any of the corners are empty and choose one at random if they are
  corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
  empty_corners = [c for c in corners if board[c[0]][c[1]] == " "]
  if len(empty_corners) > 0:
    return random.choice(empty_corners)
  
  # Otherwise, choose one of the remaining empty spaces at random
  empty_spaces = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
  return random.choice(empty_spaces)

def initialize_board():
    # Create a 3x3 array of space characters
    board = [        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]
    
    return board

def print_board(board):
  row1 = "| {} | {} | {} |".format(board[0][0], board[0][1], board[0][2])
  row2 = "| {} | {} | {} |".format(board[1][0], board[1][1], board[1][2])
  row3 = "| {} | {} | {} |".format(board[2][0], board[2][1], board[2][2])
  print()
  print(row1)
  print(row2)
  print(row3)
  print()


def player_move(board, player):
  # Ask the player to make a move
  while True:
    row = int(input("Enter row (1-3): "))
    col = int(input("Enter column (1-3): "))

    # Check if the row and column are valid
    if row < 1 or row > 3 or col < 1 or col > 3:
      print("Invalid row or column, try again!")
      continue

    # Check if the chosen position is empty
    if board[row-1][col-1] != ' ':
      print("The chosen position is not empty, try again!")
      continue

    # Place the player's symbol on the board
    board[row-1][col-1] = player
    break

  return board


def main():
  board = initialize_board()
  print_board(board)

  while (not game_is_over(board)):
    # Player X goes first
    board = player_move(board, "X")
    print_board(board)

    if game_is_over(board):
      break
    
    # Player O goes next
    move = minimax(board,3,False)[1]
    make_move(board, move, "O")
    #board = player_move(board, "O")
    print_board(board)

  print("Game Over, ",end="")
  if (evaluate_board(board) == 10):
    print("Player 'X' Wins!")
  elif (evaluate_board(board) == -10):
    print("Player 'O' Wins!")
  else:
    print("It's A Draw!")

if __name__ == "__main__":
  main()
