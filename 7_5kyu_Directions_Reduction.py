def dirReduc(arr):
    t = True
    while t:
        if len(arr) < 2:
            break
        t = False
        i = 0
        for _ in range(len(arr) - 1):
            if ((arr[i] == "NORTH" and arr[i + 1] == "SOUTH")
                    or (arr[i] == "SOUTH" and arr[i + 1] == "NORTH")
                    or (arr[i] == "EAST" and arr[i + 1] == "WEST")
                    or (arr[i] == "WEST" and arr[i + 1] == "EAST")):
                arr.pop(i)
                arr.pop(i)
                t = True
            if (not arr) or t:
                break
            i += 1
    return arr


a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
print(dirReduc(a))
u = ["NORTH", "WEST", "SOUTH", "EAST"]
print(dirReduc(u))
