# Quicksort algorithm
# Author: Prashanth Palaniappan

'''
Description:
this an implementation of the quicksort algorithm.
it is an in-place as well as a randomized algorithm.

Solution:
we randomly select a pivot element from the array entries,
and partition the array so that anything lesser than the pivot is to left of it
and anything greater than pivot is to right of it.
this automatically assigns the pivot to its right place.
Now, we recurse on the left and right parts to finally get a sorted array

psuedocode:
    quicksort(A, start_index, end_index):
        if (n==1) return n
        pivot_index = choose pivot(A, start_index, end_index)
        A, new_pivot_index = partition(A, pivot_index, end_index - start_index)
        quicksort(A, start_index, new_pivot_index - 1)
        quicksort(A, new_pivot_index + 1, end_index)
        return A
'''

import random


def partition(A, pivot_index, start_index, end_index):
    temp = A[start_index]
    A[start_index] = A[pivot_index]
    A[pivot_index] = temp
    i = start_index + 1
    j = start_index + 1
    while j <= end_index:
        if A[j] < A[start_index]:
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
            i = i + 1
        j = j + 1
    new_pivot_index = i - 1
    temp = A[new_pivot_index]
    A[new_pivot_index] = A[start_index]
    A[start_index] = temp
    return new_pivot_index


def quicksort(A, start_index, end_index):
    if start_index > end_index:
        start_index = end_index
    elif end_index < start_index:
        end_index = start_index
    if start_index == end_index:
        return
    pivot_index = random.randint(start_index, end_index)
    new_pivot_index = partition(A, pivot_index, start_index, end_index)
    quicksort(A, start_index, new_pivot_index - 1)
    quicksort(A, new_pivot_index + 1, end_index)
    return


# Get input array
x = []
array_size = int(input('Enter size of input array: '))
for i in range (0, array_size):
    x.append(int(input('Enter entry ' + str(i + 1) + ' of input array: ')))
print('\n The input array is: ' + str(x))
quicksort(x, 0, (array_size - 1))
print('\n The sorted array is: ' + str(x))


