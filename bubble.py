import numpy as np
from time import process_time_ns as ns

def sort(v):
  for j in range(len(v)-1,0,-1): 
    for i in range(j):
      if v[i]>v[i+1]:
        t = v[i+1]
        v[i]=v[i+1]
        v[i+1] = t

def main(*args):
 
  v = np.random.randint(1, 100, 100)
  s = sorted(v)
  r = sorted(v, reverse=True)
  
  n1 = ns()
  n = sort(s)
  n2 = ns()
  print(n2-n1)
  
  n1 = ns()
  n = sort(v)
  n2 = ns()
  print(n2-n1)

  n1 = ns()
  n = sort(r)
  n2 = ns()
  print(n2-n1)

if __name__== '__bubble__':
  bubble()