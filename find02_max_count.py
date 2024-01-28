def find_max_count(data):
    """
    Given the list of numbers, Find count of maximum numbers in the list
    args:
        data: list of numbers
    returns: count of maximum numbers in the list
    """
    maks = data[0]
    for i in data:
        if i>maks:
            maks = i
    return data.count(maks)
print(find_max_count([2,3,9,8,9,4,6,9,1]))