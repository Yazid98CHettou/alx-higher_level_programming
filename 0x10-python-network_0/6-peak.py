#!/usr/bin/python3


def find_peak(list_of_integers):
    listt = list_of_integers
    if listt == []:
        return None
    Total = len(listt)
    if Total == 1:
        return listt[0]
    elif Total == 2:
        return max(listt)
    midl = int(Total / 2)
    peak = listt[midl]
    if peak > listt[midl - 1] and peak > listt[midl + 1]:
        return peak
    elif peak < listt[midl - 1]:
        return find_peak(listt[:midl])
    else:
        return find_peak(listt[midl + 1:])
