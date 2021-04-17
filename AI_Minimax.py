from copy import deepcopy
import numpy as np, math
import random
from AI_Movement import free_cells, move
from AI_Heuristics import heuristics

# The Depth limit constant. You might change this if you want
# Keep in mind that your AI search might be pretty slow if you use too high depth
DEPTH = 5
gridlist = [0]*DEPTH
def maximize(grid, depth=DEPTH): 
  '''
  Maximize function for the max (AI) of the MiniMax Algorithm
  If you want to change the depth of the search tree, try to 
  implement some conditions for the "early stopping" at minimize
  or set up your own limit constant.
  '''
  # TODO: Replace the value of the best_score
  # If you are not sure, check the implementation we talked about in week 2
  best_score = float('-inf')
  best_move = None

  if(depth == 0): # taking this out:- (or len(free_cells(grid)) == 0)
    best_score = heuristics(grid, len(free_cells(grid)))
    # print("maxed best score end", best_score)
    return best_score
  else:
  # TODO: Implement maximize function here
    gridlist[depth - 1] = deepcopy(grid)
    for child_node_action in range(4): # 0 = up, 1 = right, 2 = down, 3 = left
      grid_moved = deepcopy(gridlist[depth - 1])
      move(grid_moved, child_node_action)

      if(grid_moved == gridlist[depth - 1]):
        evaluation = float('-inf')
      else:
        evaluation = minimize(grid_moved, depth - 1)
        print("worked")

      # print("check", evaluation, "; depth", depth, "; child_node_action", child_node_action)
      if(evaluation > best_score):
        best_score = evaluation
        best_move = child_node_action
      # print("eval correct")

    if(depth == DEPTH):
      return best_move, best_score
    else:
      return best_score


def minimize(grid, depth=DEPTH):
  val = random.random()
  if(val - 0.10 <= 0.0):
    val = 4
  else:
    val = 2

  empty_cells = free_cells(grid)
  if(len(empty_cells) != 0):
    select = random.choice(empty_cells)
    x, y = select
    grid[y][x] = val
  best_score = heuristics(grid, len(free_cells(grid)))
  if (depth == 0):
    # print("minimized best score end", best_score)
    return best_score
  else:
    # print("passing from min to max. Current Depth: ", depth)
    return maximize(grid, depth - 1)

def minimize2(grid, depth=0): # added default player variable- ST
  '''
  Minimize function for the min (Computer) of the Minimax Algorithm
  Computer put new 2 tile (with 90% probability) or 
  4 tile (with 10% probability) at one of empty spaces
  '''

  empty_cells = free_cells(grid)
  num_empty = len(empty_cells)

  if depth > DEPTH:
    return heuristics(grid, num_empty)

  if num_empty == 0:
    _, new_score = maximize(grid, depth+1)
    return new_score

  # TODO: (Optional) Implement conditions to stop the searching earlier 
  # Would implement it after finish implementing Heuristics and MiniMax
  # ex) If there are enough empty spaces, we will proceed by skipping last two nodes
  # if num_empty >= 6 and depth >= 3:
  #  return heuristics(grid, num_empty)

  sum_score = 0

  for c, r in empty_cells:
    for v in [2, 4]:
      new_grid = deepcopy(grid)
      new_grid[c][r] = v

      _, new_score = maximize(new_grid, depth+1)

      if v == 2:
        new_score *= (0.9 / num_empty)
      else:
        new_score *= (0.1 / num_empty)

      sum_score += new_score

  return sum_score