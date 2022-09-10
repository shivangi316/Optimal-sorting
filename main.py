#!/usr/bin/python3.9
import sys
a = sys.stdin.read()
b = a.lower()
# split() converts the bnput of strings into an arr
arr = b.split()

def sort(array):
    less = []
    equal = []
    greater = []
    if len(array) > 1:
        pivot = array[0] # We are picking the first element of the arr as the pivot so arr[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return sort(less)+equal+sort(greater) 
    else:  # to handle the end part of recursion if there is only one element in the erray then this just returns the array
        return array

print(" ")
print(*sort(arr),sep="\n")

