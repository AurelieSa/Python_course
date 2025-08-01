from math import sqrt
from random import randint

def correcion_map(l, op):
  return [op(v) for v in l]

def correction_any(l, op):
  for v in l:
    if op(v):
      return True
    
  return False

def correction_all(l, op):
  for v in l:
    if not op(v):
      return False
    
  return True

def correction_min(l):
  return min(l)

def correction_max(l):
  return max(l)

def correction_avg(l):
  return sum(l)/len(l)

def correction_min_index(l):
  index = -1
  min_val = correction_max(l)

  for i in range(len(l)):
    v = l[i]
    if v<min_val:
      min_val = v
      index = i

  return index

def correction_max_index(l):
  index = -1

  max_val = correction_min(l)

  for i in range(len(l)):
    v = l[i]
    if v>max_val:
      max_val = v
      index = i
  
  return i

def correction_sort_gen(l, op):

  l_sorted = []

  while len(l) != 0:
    i = op(l)
    l_sorted.append(l[i])
    l.pop(i)

  return l_sorted

def correction_sort(l):
  return correction_sort_gen(l, correction_min_index)

def correction_distribution(l):
  d = {}

  for v in l:
    if v in d:
      d[v] += 1
    else:
      d[v] = 1

  return d

if __name__ == "__main__":
  l = [randint(-100, 100) for _ in range(100)]

  ls = correction_sort(l.copy())
  l.sort()

  if ls==l:
    print("ok")