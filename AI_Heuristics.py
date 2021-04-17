import numpy as np, math
from copy import deepcopy
import statistics as st

def heuristics(grid, num_empty):
  '''
  This function scores the grid based on the algorithm implemented
  so that the maximize function of AI_Minimax can decide which branch
  to follow.
  '''
  grid = np.array(grid)
  testgrid = deepcopy(grid)
  score = 0

  # TODO: Implement your heuristics here. 
  # You are more than welcome to implement multiple heuristics

  # simple space heuristic
  # score = num_empty

  # pushing algorithm to make the tiles closer to each other
  dist_score = 0
  filler_loc = [-1]*16
  counter = 0
  vals = [-1]*16

  big_val = np.amax(testgrid)
  max_val = big_val/4
  while (big_val > 2): # max_val and max_val > (after the > sign)
    result = np.where(testgrid == big_val)
    filler_loc[counter] = result
    vals[counter] = big_val
    dist_score -= (st.pstdev(result[0]) + st.pstdev(result[1]))
    coordList = list(zip(result[0], result[1]))

    for location in coordList:
      x, y = location
      testgrid[x][y] = 0

    counter += 1
    big_val = np.amax(testgrid)


  # thisdict = {
  # 0 : 0,
  # 1 : 100,
  # 2 : 200, 
  # 3 : 300
  # }

  if(counter != 0):
  #  for xx in filler_loc[0][0]:
  #    dist_score -= thisdict[xx]
  #  for yy in filler_loc[0][1]:
  #    dist_score -= thisdict[yy]

    # dist_score -= 10*st.pstdev([st.mean(filler_loc[i][0])*math.log(vals[i], 2) for i in range(counter)])
    # dist_score -= 10*st.pstdev([st.mean(filler_loc[i][1])*math.log(vals[i], 2) for i in range(counter)])
    score += dist_score
    score += score*0.10*(16 - num_empty)
  else:
    score = num_empty

  # Weight for each score
  return score