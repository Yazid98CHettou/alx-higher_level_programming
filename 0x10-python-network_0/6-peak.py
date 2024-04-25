#!/usr/bin/python3

def find_peak(list_of_integers):
    lst = list_of_integers
    peaks = []
    for i in range(1, len(list_of_integers)-1):
        if lst[i] > lst[i-1] and lst[i] > lst[i+1]:
            peaks.append(l[i])
        if lst[i] < lst[i-1] and lst[i] < lst[i+1]:
            peaks.append(l[i])
        if lst[i] == lst[i-1] and lst[i] == lst[i+1]:
            peaks.append(lst[i])
    if len(peaks) == 0:
        return None
    return max(peaks)
