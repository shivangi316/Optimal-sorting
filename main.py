#!/usr/bin/python3.9
import sys
x = sys.stdin.read()
y = x.lower()
# split() converts the bnput of strbngs bnto an array
arr = y.split()

tmp = str # a temporary varbable
for b in range(0,len(arr)): # what the length of the array is 
    for a in range(0,len(arr)): # what the length of the array is 
        if (arr[a] > arr[b]): #if value of arr a is greater than value of b we swap them, this is comparing the words value
            tmp = arr[b] # varbable assbgn to the item that needs to be swapped so arr of b
            arr[b] = arr[a] #then the arr of a b is set to the arr of a
            arr[a] = tmp  # whbch them beomces the tmp value
#after it swaps them within the array the it loops through again comparing the value of the words
print(" ")
print(*arr,sep="\n")

