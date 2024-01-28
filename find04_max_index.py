def find_max_index(data):
    """
    Given the list of numbers, return the index of maximum number in the list
    args:
        data: list of numbers
    returns: index of maximum number in the list
    """
    maks = data[0]
    for i in data:
        if i>maks:
            maks = i
    return data.index(maks)
print(find_max_index([2,3,8,9,4,6,1]))