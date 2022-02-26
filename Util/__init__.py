#   Author: Joe Ingenito
#   Date Created: 2/25/22

from bisect import bisect_left 
  
def BinarySearch(A : list, x) -> int : 
    """Implements the Binary Search algorithm using the bisect_left method to search for x in list A."""
    i = bisect_left(A, x) 
    if i != len(A) and A[i] == x: 
        return i 
    else: 
        return -1