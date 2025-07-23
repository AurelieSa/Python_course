import matplotlib.pyplot as plt
import numpy as np

def check_born(x, b_inf, b_sup):
  return x >= b_inf and x < b_sup

def new_grid(H, W):
  return [[0 for _ in range(W)] for _ in range(H)]

def init_grid(size):
  return np.random.randint(0, 2, size=(size, size)).tolist()


def run(t_sim, size, update_function):

  grid = init_grid(size)

  plt.ion()
  fig, ax = plt.subplots()

  for _ in range(t_sim):  # nombre d'itérations
      ax.clear()
      ax.imshow(grid, cmap="binary")
      plt.title("Jeu de la Vie")
      plt.pause(0.2)
      grid = update_function(grid, size)

  plt.ioff()
  plt.show()

def update(grid, size):

  next_grid = new_grid(size, size)

  for h in range(size):
    for w in range(size):
      # check neighbours
      neighbours = 0

      for dw in [-1, 0, 1]:
        for dh in [-1, 0, 1]:
          if dw==0 and dh==0:
            continue
          
          x, y = w+dw, h+dh

          if check_born(x, 0, size) and check_born(y, 0, size):
            neighbours += grid[x][y]

      # check conway rule
      if grid[w][h]==1:
        if neighbours==2 or neighbours==3:
          next_grid[w][h] = 1
      else:
        if neighbours==3:
          next_grid[w][h] = 1

  return next_grid

if __name__ == "__main__":

  run(10, 30, update_function=update)