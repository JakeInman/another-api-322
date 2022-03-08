import itertools

def calculate_change(amt_tendered, cost, available_denominations):
    if amt_tendered < cost:
        return 'Not Enough Money'
    elif amt_tendered == cost:
        return 'Please Take Your Receipt'
    
    possible_permutations = list(itertools.permutations(available_denominations))

    change_possibilities = []

    for permutation in possible_permutations:
        # if permutation[0] == 1:
        #     continue
        remainder_amount = amt_tendered - cost
        change = {}
        for denomination in permutation:
            change[denomination] = remainder_amount // denomination
            remainder_amount = remainder_amount % denomination
        change_possibilities.append(change)
    
    lowest = None
    for possibility in change_possibilities:
        if lowest is None or sum(possibility.values()) < sum(lowest.values()):
            lowest = possibility
    return lowest

if __name__ =="__main__":
    import timeit
    print(timeit.timeit("calculate_change(500, 470, [25, 10, 5, 1])", setup="from __main__ import calculate_change", number=100000))
    # print(calculate_change(500, 470, [25, 10, 5, 1]))