

def space():
    height = get_height()

    for i in range(height):
        print((height - 1 - i) * " ",end="")
        print((i + 1) * "#" + "  " , end="")



        for j in range(i + 1):
            print( "#",end="")
        print()


def get_height():
    while True :
        try:
            height = int(input("height: "))
            if height >= 1 and height <= 8:
                break
        except ValueError :
            print("your input is not a number")
    return height

space()