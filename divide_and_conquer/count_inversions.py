# Count number of inversions using divide and conquer method
# Author: Prashanth Palaniappan

'''
Description: This algorithm counts the number of inversions in an array.
An inversion means a[i] > a[j] for i < j.
This is used in recommendation systems to check how similar users are, and recommend content accordingly

Solution:
The algorithm piggybacks on mergesort.
Merge sort works by dividing the problem in half and recursively sorting the left and right halves.
During the combine step (merging the sorted left and sorted right halfs),
when an entry in the right half is lesser than an entry in the left half,
number of inversions will be remaining entries in the left half.
'''


def sort_and_count(x):
    '''

    :param x: input array
    :return: sorted array, number of inversions
    '''
    n = len(x)
    if n == 1:
        return x, 0
    else:
        a = x[0:n//2]
        b = x[n//2:n]
        a, left_count = sort_and_count(a)
        b, right_count = sort_and_count(b)
        split_count = 0
        i = 0
        j = 0
        k = 0
        y = [None] * n
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                y[k] = a[i]
                i += 1
                k += 1
            elif b[j] < a[i]:
                y[k] = b[j]
                j += 1
                k += 1
                split_count = split_count + (len(a) - i)
        while i < len(a):
            y[k] = a[i]
            i += 1
            k += 1
        while j < len(b):
            y[k] = b[j]
            j += 1
            k += 1
        count = left_count + right_count + split_count
        return y, count


# Get input array
x = []
array_size = int(input('Enter size of input array: '))
for i in range (0, array_size):
    x.append(int(input('Enter entry ' + str(i + 1) + ' of input array: ')))
result, count = sort_and_count(x)
print('\n The input array is: ' + str(x))
print('\n The sorted array is: ' + str(result))
print('\n The number of inversions is ' + str(count))
