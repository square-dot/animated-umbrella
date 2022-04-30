def process(line):
    i = 0

    newstring = ""

    for char in line:
        if char == "\"":
            if i%2 == 0:
                newstring = newstring + "``"
            else:
                newstring = newstring + "''"
            i += 1
        else:
            newstring = newstring + char
            
    return newstring

