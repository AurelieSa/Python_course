import matplotlib.pyplot as plt
import numpy as np

def new_grid(H, W):
  return [[0 for _ in range(W)] for _ in range(H)]

def init_grid(size):
  return np.random.randint(0, 2, size=(size, size)).tolist()

def run(t_sim, size, update_function):

  grid = init_grid(size) # create random grid

  # create plot
  plt.ion()
  fig, ax = plt.subplots()

  for _ in range(t_sim):  # run animation
      ax.clear()
      ax.imshow(grid, cmap="binary")
      plt.title("Game of Life")
      plt.pause(0.2)
      grid = update_function(grid, size)

  plt.ioff()
  plt.show()


"""TODO"""
def check_born(x, b_inf, b_sup):
  raise NotImplementedError()

def update(grid, size):

  next_grid = new_grid(size, size)

  raise NotImplementedError()

  return next_grid

if __name__ == "__main__":

  run(10, 30, update_function=update)