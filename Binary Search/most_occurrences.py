from first_occurrence import firstOccurrence
from last_occurrence import lastOccurrence

def mostOccurrence(arr, n, k):
    lO = lastOccurrence(arr, n, k)
    fO = firstOccurrence(arr, n, k)
    return lO - fO + 1

arr = [1,2,4,5,5,5,6,7,7]
frequency = mostOccurrence(arr, len(arr), 5)
print(frequency)