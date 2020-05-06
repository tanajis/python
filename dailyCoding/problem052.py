Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Implement an LRU (Least Recently Used) cache. It should be able to be initialized with a cache size n, and contain the following methods:

set(key, value): sets key to value. If there are already n items in the cache and we are adding a new item,
then it should also remove the least recently used item.
get(key): gets the value at key. If no such key exists, return null.
Each operation should run in O(1) time.



Implementation using Queue


def lru_cashe(n):
  return Queue(n)

def set(k,v):
  if Queue full:
       deque()
  enque({k:v})
  
  
def get(k):
  temp = Q[k]
  Q.remove(k)
  # Add at the start
  Q.enque(temp)
  
      
