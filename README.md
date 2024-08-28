# Priority-Queue
A Priority Queue Class in Python.

## What is Priority Queue
Priority Queue is a data structure with these functions: 
  
  `push`: put a new value into the queue.

  `pop`: delete the most minimum value from the queue.

It also has this property: 

  `top`: get the most minimum value in the queue.

Each of these functions or properties need the time of logarithm of the size of the queue.

## How to use it
### Set up
  You can give a parameter called 'cmp' into `__init__`, which must be a function or Lambda Expression. 
  
  'cmp' is the comparing method of the queue. In the queue, 'x < y' only if `cmp(x, y)` returns `true.
### Functions
  There are 2 functions `push(value)` and `pop()` in the class. Their usages have been introduced in last paragraph.

  `push` needs 1 parameter, which is the value to push in.

  `pop` doesn't need any parameter.
### Properties
  There is 1 property `top` in the class. It has been introduced in last paragraph.

  Remember: you should use it as `q.top`. __Don't use as `q.top()`__, or it will throw a exception. 
### Usages with Builtin Functions
  You can use `bool(q)` to know if `q` isn't empty.

  You can use `len(q)` to get the length of `q`.
