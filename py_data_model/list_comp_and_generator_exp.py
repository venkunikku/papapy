import array

symbols = '$¢£¥€¤'
global last

def scope_of_a_variable_in_list_gen_comprehensions():
    # codes = [65, 66, 67]
    
    x = 'ABC'

    # you can use x as a local variable in list comp
    val = [ord(x) for x in x]
    print(F"Using x as a local variable and it will still hold orginal: {x} and final results : {val}")

    # This Walrus operator is availble from Py 3.8 version
    code = [last := ord(c) for c in x]
    print(F"You will see the last is still has the last assinged values: {last}")

if __name__ == "__main__":
    li_comp = [ord(c) for c in symbols]
    print(li_comp)


    li_comp = [ord(s) for s in symbols if ord(s) > 127]
    print(li_comp)

    # same things above can be done by filters. 
    # But list comp is much faster
    li_filter = list(filter(lambda c: c > 127, map(ord, symbols))) # filter(fun, sequence)
    print(li_filter)
    
    print(map(ord, symbols).__next__())
    


    # generator functions

    t = tuple(ord(c) for c in symbols)
    print(f"{t} - values of tules from a generator function")


    ar = array.array("I", (ord(c) for c in symbols))
    print(F"{ar} value of array.array generator function")

    scope_of_a_variable_in_list_gen_comprehensions()