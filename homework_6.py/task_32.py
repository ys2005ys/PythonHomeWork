def find_indexes(lst, min_val, max_val):
    indexes = []
    for i, val in enumerate(lst):
        if min_val <= val <= max_val:
            indexes.append(i)
    return indexes