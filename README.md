# Priority-Queue
A Priority Queue Class in Python.

## What is Priority Queue
  Priority Queue is a data structure with these functions: 
    `push`: put a new value into the queue.
    `pop`: delete the most minimum value from the queue.
  It also has this property: 
    `top`: get the most minimum value in the queue.
  Each of these functions or propertys need the time `O(log n)`. `n` is the length of the queue.

## How to use it
  ### Set up
    You can give an parameter called 'cmp' into `__init__`, which must be a function or Lambda Expression.
    'cmp' is the comparing method of the queue. In the queue, 'x < y' only if `cmp(x, y)` returns `true.
  
