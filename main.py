#!/usr/bin/python3.9
import sys
a = sys.stdin.read()
b = a.lower()
# split() converts the bnput of strings into an arr
arr = b.split()

# tmp = str
# for i in range(0, len(arr)):
#     for j in range(0,len(arr)):
#         if (arr[j] > arr[i]):
#             tmp = arr[i]
#             arr[i] = arr[j]
#             arr[j] = tmp

# def sort3(array, size):
#     for index in range(size):
#         min_index = index

#         for j in range(index + 1, size):
# select the minimum element in every iteration
#             if array[j] < array[min_index]:
#                 min_index = j
# swapping the elements to sort the array
#         (array[index], array[min_index]) = (array[min_index], array [index])
# size = len(arr)
# sort3(arr, size)

# def sort2(arr):
#    if len(arr) > 1: #len is measuring the length of the array
#        # Finding the mid of the array
#        middle = len(arr)//2
        # Dividing the array elements
#        x = arr[:middle] # left side
#        y = arr[middle:] # right side
        # Sorting the first half
#        sort2(x)
        # Sorting the second half
#        sort2(y)
#       i=j=k=0 # setting all the index values that are going to be used to 0, i & j are being just for temporary arrays while k is being used for the array we are going to use
        
        # Copy data to temporary arrays x[] and y[]
#        while i < len(x) and j < len(y):
#            if x[i] < y[j]:
#                arr[k] = x[i]
#                i += 1
#            else: #if y[j] < x[i]
#                arr[k] = y[j]
#                j += 1
#            k += 1 # at the end of the while statement not the if & else statement
         # Checking if any element was left unsorted
#        while i < len(x):
#            arr[k] = x[i]
#            i += 1
#            k += 1
#        while j < len(y):
#            arr[k] = y[j]
#            j += 1
#            k += 1
#sort2(arr)

# def sort(array):
#     less = []
#     equal = []
#     greater = []
#     if len(array) > 1:
#         pivot = array[0] # We are picking the first element of the arr as the pivot so arr[0]
#         for x in array:
#             if x < pivot:
#                 less.append(x)
#             elif x == pivot:
#                 equal.append(x)
#             elif x > pivot:
#                 greater.append(x)
#         return sort(less)+equal+sort(greater) 
#     else:  # to handle the end part of recursion if there is only one element in the erray then this just returns the array
#         return array

# def sort4(arr, n):
#     midpoint = n // 2 # grabs the midpoint of the arr
#     while midpoint > 0:
# #loops until no more
#         for i in range(midpoint, n):
#             tmp = arr[i] # allows for var i to hold a dfferent values while saving the other in var tmp
#             j = i # checks for when var i is in correct arr value
#             while j >= midpoint and arr[j - midpoint] > tmp: # allows for j to work as a variable within the sort arr, and protects it for going into negative values
#                 arr[j] = arr[j - midpoint]
#                 j -= midpoint
#                 #puts arr values in place due to //= 2, returns original i value in the array from tmp value
#             arr[j] = tmp 
#         midpoint //= 2
       
# size = len(arr)
# sort4(arr, size)
#returns outputs to the size of the arr,

def sort5(arr):
    for i in range(1, len(arr)): #starts from the first, "sorted", variable of the arr, while the for loop takes care of reusing the while loop until properly sorted
        tmp = arr[i]
        j = i

        while j > 0 and arr[j - 1] > tmp: #this allows the sort func to push the alphabetically descending lesser var to the right, or down while keeping the higher in place, while amount of needed sorts is above 0
            arr[j] = arr[j - 1]
            j = j - 1
            arr[j] = tmp
sort5(arr)

print(" ")
print(*arr,sep="\n")
