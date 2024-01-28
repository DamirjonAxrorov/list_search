def find_min_index(data):
    """
    Given the list of numbers, return the index of minimum number in the list
    args:
        data: list of numbers
    returns: index of minimum number in the list
    """
    mini = data[0]
    for i in data:
        if i<mini:
            mini = i
    return data.index(mini)
print(find_min_index([2,3,8,-9,4,6,1]))