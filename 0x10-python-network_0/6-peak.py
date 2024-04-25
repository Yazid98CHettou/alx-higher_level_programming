def find_peak(list_of_integers):

    lst = list_of_integers
    if lst == []:
        return None
    total = len(lst)
    if total == 1:
        return lst[0]
    elif total == 2:
        return max(lst)
    middle = int(total / 2)
    peak = lst[middle]
    if peak > lst[middle - 1] and peak > lst[middle + 1]:
        return peak
    elif peak < lst[middle - 1]:
        return find_peak(lst[:middle])
    else:
        return find_peak(lst[middle + 1:])
