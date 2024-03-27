"""Main module."""

def reverse_complement(forward):
    """
    reverse_comlement(forward): Print reverse complement of the forward

    Parameters
    ----------
    forward : str
           Forward sequence
 
    """
    if type(forward) != str:
        print("ERROR: wrong type")
        return None
    a = forward.lower().count("a")
    t = forward.lower().count("t")
    g = forward.lower().count("g")
    c = forward.lower().count("c")
    if a+t+g+c != len(forward):
        print("ERROR: wrong value(s)")
        return None
    complement = ""    
    reverse = forward[::-1]
    if i in reverse == "a":
        complement += "t"
    elif i in reverse == "t":
        complement += "a"
    elif i in reverse == "g":
        complement += "c"
    elif i in reverse == "c":
        complement += "g"
    print(complement)
    return complement

