# O(1) = Constant Time
# No matter how many times the array/elements increase,
# the number of operations stay the same.

import time

small_array = ['remy' for i in range(10)]
medium_array = ['remy' for i in range(100)]
big_array = ['remy' for i in range(100000)]

def ratatouille(array):
    t0 = time.time()
    print(array[0]) # O(1) operation
    print(array[1]) # O(1) operation
    t1 = time.time()
    print(f"Time Calculated: {t1 - t0}")
    
ratatouille(small_array)
ratatouille(medium_array)
ratatouille(big_array)

# The time calculated is 0.0, because we are only taking the first and the second elements of the arrays.
# Therefore, we are performing O(1) operations, because they are remaining constant.
# We are performing two O(1) operations, therefore the function has an operation of O(2).
