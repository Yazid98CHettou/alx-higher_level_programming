#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    a = 0
    new_list = []
    RSLT = 0
    for a in range(0, list_length):
        try:
            RSLT = (my_list_1[a] / my_list_2[a])
        except TypeError:
            RSLT = 0
            print("wrong type")
        except ZeroDivisionError:
            RSLT = 0
            print("division by 0")
        except IndexError:
            RSLT = 0
            print("out of range")
        finally:
            new_list.append(RSLT)
    return new_list

