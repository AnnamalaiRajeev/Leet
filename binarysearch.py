from copy import deepcopy


def binary_search(sorted_list, element):
    # returns element
    s = deepcopy(sorted_list)
    while len(s)-1 > 1:
        mid = (len(s)-1) // 2
        print(mid)
        if s[mid] == element:
            return mid,element
        if s[mid] <= element:
            s = s[mid+1:]
        if s[mid] >= element:
            s = s[:mid-1]
    return 0,0


def binary_search_1(sorted_list, element): # returns element and index #linear time # constant space
    i = 0
    r = len(sorted_list) - 1
    s = sorted_list
    while i<r:
        mid = r+i // 2
        if s[mid] == element:
            return mid,element
        if s[mid] <= element:
             i = mid+1
        if s[mid] >= element:
            r = mid-1
    return 0,0


def binary_search_recursion(i,r,sorted_list, element): #linear time #space logn
    mid = r+i // 2
    if sorted_list[mid] == element:
        return mid, element
    if element > sorted_list[mid]:
        i = mid+1
        return binary_search_recursion(i,r,sorted_list,element)
    if element<sorted_list[mid]:
        r = mid-1
        return binary_search_recursion(i,r,sorted_list,element)
    if i >=r:
        return -1,-1


if __name__ == '__main__':
    A = [1, 2, 3, 4, 7, 10, 15, 16, 18, 20]
    assert binary_search_1(A,15) == (6, 15)
    assert binary_search_recursion(0, len(A)-1, A, 15) == (6, 15)
