#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    data = dir(hidden_4)
    for token in data:
        if token.startswith("__"):
            continue
        print("{}".format(token))
