def func(inp):

    w = inp[0]

    x = (z % 26) 
    x += 12

    if x != w:
        z *= 26
        z += (w+6)


    #----------------------    
    w = inp[1]

    x = (z % 26)
    x += 10

    if x != w:
        z *= 26
        z += (w+6)


    #----------------------
    w = inp[2]

    x = (z % 26)
    x += 13
    
    if x != w:
        z *= 26
        z += (w+3)


    #----------------------
    w = inp[3]
    
    x = (z % 26)
    x += -11
    
    z //= 26

    if x != w:
        z *= 26
        z += (w+11)



    #----------------------
    w = inp[4]

    x = (z % 26)
    x += 13
    
    if x != w:
        z *= 26
        z += (w+9)


    #----------------------
    w = inp[5]
    x = (z % 26)
    x += -1

    z //= 26

    if x != w:
        z *= 26
        z += (w+3)


    #----------------------
    w = inp[6]

    x = (z % 26)
    x += 10
    
    if x != w:
        z *= 26
        z += (w+13)



    #----------------------
    w = inp[7]
    x = (z % 26)
    x += 11

    if x != w:
        z *= 26
        z += (w+6)



    #----------------------
    w = inp[8]
    x = (z % 26)
    x += 0

    z //= 26

    if x != w:
        z *= 26
        z += (w+14)


    #----------------------
    w = inp[9]
    x = (z % 26)
    x += 10

    if x != w:
        z *= 26
        z += (w+10)



    #----------------------
    w = inp[10]
    x = (z % 26)
    x += -5

    z //= 26

    if x != w:
        z *= 26
        z += (w+12)


    #----------------------
    w = inp[11]
    x = (z % 26)
    x += -16

    z //= 26


    if x != w:
        z *= 26
        z += (w+10)


    #----------------------
    w = inp[12]
    x = (z % 26)
    x += -7

    z //= 26

    if x != w:
        z *= 26
        z += (w+11)


    #----------------------
    w = inp[13]
    x = (z % 26)
    x += -11

    z //= 26


    if x != w:
        z *= 26
        z += (w+15)

    return x, z, w