def binary_search(lst, item):
    low = 0
    high = len(lst)-1
    while low <= high:
        mid = (low+high)//2
        if item == lst[mid]:
            return mid
        elif item < lst[mid]:
            high = mid-1
        else:
            low = mid+1
    return -1
