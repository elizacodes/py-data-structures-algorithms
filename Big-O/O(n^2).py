array = [1, 2, 3, 4, 5] #  O(1)

def big_O_Squared(array): # O(n)
    for i in range(len(array)): # O(n)
        for j in range(len(array)): # O(n)
            print(array[i], array[j]) # (O n^2) or n*n*O(1)
            
big_O_Squared(array) # O(1)

# Total time complexity for the big_O_Squared: n + n + n + O(2) = O(3n^2)
# However, ignore your constants... O(3n^2) = O(n^2)
# O(n^2) is what we call quadratic time.
