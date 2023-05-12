def unpacking_seq():
    # Aavailable in python 3.5
    
    # you can use * to create a list
    li = [*range(3), *range(3, 7)]
    print(f"Using * to create a list: {li}")

    s = {*range(0,5), *[5,6, 7]}
    print(f"Using * to create a set: {s}")

    t = (*range(0,5), *[5,6,7])
    print(f"Using * to create a tuple: {t}")

if __name__ == "__main__":
    unpacking_seq()