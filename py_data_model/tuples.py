

def is_hashable(t):
    try:
        h = hash(t)
        print(f"Yes Hash(able) -  value {h}")
    except TypeError:
        print("TypeError: unhashable type")

def tuples_():
    li = [10, 20]
    t = ("a", li)
    print(f"Value of tuple before {t}")

    li.extend([50]);    print(li)

    print(f"Values of tuple reference is immutables: {t}")

    # accessing tuple values by slice
    print(f"Slicing a tuple {t[-2]}")

    # if you want to determine if any object has fidex value
    # you can use the has built-in
    is_hashable(t)

    tt = ("a", li)
    is_hashable(tt)

    tt = (1, 2, "a")
    is_hashable(tt)


    # in place concatenation
    tt += (10, 20, 10)
    print(F"In place concat - creating a new tuple: {tt}")

    print(f"{tt.count(10)} - count of 10 in tuple {tt}")

    print(f"{tt.index(10)} - first occurance of index of 10 in tuple {tt}")

    a = (1, 2)
    b = (3, 4)
    c = a * 3
    print(f"Tuple multiplication {c}")  # (1, 2, 1, 2, 1, 2) is the answer

def fun(a, b, c, d, *rest):
    return a, b, c, d, rest

def upacking_using_star():
    print("*"*80)
    # Using * to grab excess items
    a, b, *rest = range(5)
    print(f"Using * to grab excess items: {a, b, rest}")

    # rest can be an empty list
    a, b, *rest = range(2)
    print(f"Using * to grab excess items: {a, b, rest}")

    # * can appear in any position
    a, *body, c, d = range(5)
    print(f"Using * to grab excess items: {a, body, c, d}")


    # *a, *b, c = range() # SyntaxError: two starred expressions in assignment


    # you can use * multiple times in a function call
    r = fun(*[1,2], 3, *range(4,7))
    print(f"Using * multiple times in a function call: {r}")

    # you can use * to create a list
    li = [*range(3), *range(3, 7)]
    print(f"Using * to create a list: {li}")

    s = {*range(0,5), *[5,6, 7]}
    print(f"Using * to create a set: {s}")

    t = (*range(0,5), *[5,6,7])
    print(f"Using * to create a tuple: {t}")


    metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
    ]

    print(f'{"":15} | {"lat.":^9} | {"long.":^9}') # center align

    # print(f'{"":15} | {"lat.":>9} | {"long.":>9}') # right align
    # using unpacking in the for loop
    for name, _, _, (lat, long) in metro_areas:
        if long <= 0:
            print(f'{name:15} | {lat:9.4f} | {long:9.4f}')

    


if __name__ == "__main__":
    tuples_()
    upacking_using_star()
    