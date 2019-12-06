import functools

#n is the number of months
#k is the number of offspring that each mature rabbit creates

#LRU CACHE is used to improve compute time. Read more about the Python Module Here:
# https://docs.python.org/3/library/functools.html

@functools.lru_cache(maxsize=None)
def fibbs_rabbits(n, k):
  if (n == 1 or n == 2):
    return 1
  else:
    return fibbs_rabbits(n - 1, k) + fibbs_rabbits(n-2, k) * k


print(fibbs_rabbits(36, 5))