def find_max_min_sum(data):
    """
    Given the list of numbers, return the sum of the maximum and minimum numbers in the list
    args:
        data: list of numbers
    returns: sum of the maximum and minimum numbers in the list
    """
    minm = data[0]
    maks = data[0]
    for i in data:
        if i>maks:
            maks = i
        else:
            minm = i
    return maks + minm
print(find_max_min_sum([2,3,8,9,4,6,1]))