# Priority-Queue

A Priority Queue Structure. 

_Upd 2023-03-13:Delete `size` and `empty`, use `__len__` and `__bool__` instead._

## Why write it

  Priority Queue has been written in C++ STL, but it is diffcult to use in Queue module in Python.
  
  This is a easier type.

## How to use

  ### Set up
  
  You can give a parameter `cmp` into `__init__`. It must be a function or lambda expression with two parameter. It will be the comparing method of the queue. In the queue, `x < y` only if `cmp(x, y)` is true.

  ### Function:
  
  Use `push` to add a value into the queue. 
  
  Use `pop` to detele the minimum value out of the queue.

  ### Property:
  
  Use `top` to get the minimum value in the queue when the queue isn't empty. 

  ### with Built-in Function

  ```python
  q = PriorityQueue()
  ```

  `bool(q)` returns true when `q` isn't empty.

  `len(q)` returns the length of the queue.
  
  ### Example 1:
  ```python
  q = PriorityQueue()
  q.push(5)
  q.push(7)
  q.push(2)
  q.push(21)
  while q:
      print(q.top)
      q.pop()
  ```
  will print
  ```
  2
  5
  7
  21
  ```
  
  ### Example 2:
  ```python
  q = PriorityQueue(cmp=lambda x, y: x[1] < y[1] if (x[0] == y[0]) else x[0] < y[0])
  q.push((1, 5))
  q.push((7, 2))
  q.push((4, 5))
  q.push((1, 7))
  while q:
      print(q.top)
      q.pop()
  ```
  will print
  ```
  (1, 5)
  (1, 7)
  (4, 5)
  (7, 2)
  ```


## When to use it

  Priority Queue is a basic data structure. It can be used in some algorithm, like Dijkstra.
