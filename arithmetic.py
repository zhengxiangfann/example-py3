#coding:utf_8

"""
 arithmetic
"""

from __future__ import print_function
def sequential_search(lis, key):
    '''遍历无序列表
    '''
    length = len(lis)
    for i in range(length):
        if lis[i] == key:
            return i
    return False


def binary_search(lis, key):
    '''
    binary search
    '''
    low = 0
    high = len(lis) -1
    time = 0
    while low < high:
        time += 1
        mid = int((low + high) /2)
        if key < lis[mid]:
            high = mid -1
        elif key > lis[mid]:
            low = mid + 1
        else:
            print("times: %s" % time)
            return mid
    print("times:%s"%time)
    return False

def binary_search1(lis, key):
    '''
    插值查找
    '''
    low = 0
    high = len(lis) -1
    time = 0
    while low < high:
        time += 1
        mid = low + int((high-low) * (key - lis[low])/(lis[high] - lis[low]))
        print("mid=%s, low=%s, high=%s" % (mid, low, high))
        if key < lis[mid]:
            high = mid - 1
        elif key > lis[mid]:
            low = mid -1
        else:
            print("times: %s" % time)
            return mid
    print("times: %s" % time)
    return False


def fibonacci_search(lis, key):
    F = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,
         233, 377, 610, 987, 1597, 2584, 4181, 6765,
         10946, 17711, 28657, 46368]
    low = 0
    high = len(F) - 1
    k = 0
    while high > F[k] - 1:
        k += 1
    print(k)
    i = high
    while F[k]-1 > i:
        lis.append(lis[high])
        i += 1
    print(lis)
    time = 0
    while low <= high:
        time += 1
        if k < 2:
            mid = low
        else:
            mid = low + F[k-1] -1
        print('low=%s, mid=%s, high=%S' %(low, mid, high))
        if key < lis[mid]:
            high = mid - 1
            k -= 1
        elif key > lis[mid]:
            low = mid + 1
            k -= 2
        else:
            if mid <= high:
                print('times:%s'% time)
                return mid
            else:
                print('times: %s'% time)
                return high
    print('times: %s' % time)
    return False



if __name__ == '__main__':
    LIST = [1, 5, 8, 123, 22, 54, 7, 99, 300, 222]
    #result = sequential_search(LIST, 123)
    RESULT = binary_search1(LIST, 123)
    print(RESULT)
