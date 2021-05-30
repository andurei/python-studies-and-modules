

from re import split

def linearSearch(my_list, value):
    for i in my_list:
        if (value == i):
            return True
    return False

def binarySearch(my_list, value):
    low = 0
    high = len(my_list) - 1
    mid = 0
    while (low <= high):
        mid = high + low // 2
        if (my_list[mid] < value):
            low - mid + 1
        elif (my_list[mid] > value):
            high = mid - 1
        else:
            return True
    return False

def binarySearch2(my_list, low, high, value):
    if (high >= low):
        mid = (high + low) // 2
        if (my_list[mid] == value):
            return True
        elif (my_list[mid] > value):
            return binarySearch2(my_list,low, mid-1, value)
        else:
            return binarySearch2(my_list,mid+1, high, value)
    
    else:
        return False
