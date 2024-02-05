#!/usr/bin/python3
"""
Module with class MyList

"""
class MyList(list):
    def print_sorted(self):
        """Methot that sorted a list"""
        print(sorted(self))
