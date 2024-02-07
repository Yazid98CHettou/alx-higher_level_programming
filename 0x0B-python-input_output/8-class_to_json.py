#!/usr/bin/python3
"""returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an objec"""


def class_to_json(obj):
    """Return the dictionary represntation of a simple data structure."""
    return obj.__dict__
