#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    temp = dir(hidden_4)
    for tmp in temp:
        if tmp[:2] != "__":
            print(tmp)
