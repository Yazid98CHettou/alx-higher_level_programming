#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    RETT = list(a_dictionary.keys())[0]
    BIGG = a_dictionary[RETT]
    for a, b in a_dictionary.items():
        if b > BIGG:
            BIGG = b
            RETT = a
    return (RETT)
