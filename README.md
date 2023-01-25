# Priority-Queue

A Priority Queue Structure. 

## Why write it

  Priority Queue has been written in C++ STL, but it is diffcult to use in Queue module in Python.
  
  This is a easier type.

## How to use

  ### Set up
  
  You can give a parameter 'cmp' into `__init__`. it must be a function or lambda expression with two parameter. It will be the compare method of the queue. In the queue, x < y only if cmp(x, y) is true.

  ### Function:
  
  Use 'push' to push a value into the queue. 
  
  Use 'pop' to pop the minimum value out of the queue.

  ### Property:
  
  Use 'top' to get the minimum value in the queue. 
  
  Use 'size' to get the size of the queue. Use 'empty' to get the queue is empty or not.
  
  ### Example 1:
  ```python
  q = PriorityQueue()
  q.push(5)
  q.push(7)
  q.push(2)
  q.push(21)
  while not q.empty:
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


## When to use it

  Priority Queue is a basic data structure. It can be used in some algorithm, like Dijkstra.
