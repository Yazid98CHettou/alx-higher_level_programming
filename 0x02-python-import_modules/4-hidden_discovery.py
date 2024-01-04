#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for Name in dir(hidden_4):
        if Name[0] != '_' and name[1] != '_':
            print(Name)
