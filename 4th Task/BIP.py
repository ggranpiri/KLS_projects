def shag(x, time, way):
    way += [x]
    if sorted(way) == [0, 1, 2, 3, 4, 5, 6, 7]:
        return time
    for i in range(len(history[x])):
        if history[x][i] and i not in way:
            if i in [3, 4, 7]:
                return max(4, shag(i, time + history[x][i], way))

            else:
                return shag(i, time + history[x][i], way)

    return time


history = [[0, 2, 0, 0, 4, 0, 0, 3],
           [2, 0, 2, 0, 0, 0, 0, 0],
           [0, 2, 0, 4, 0, 0, 0, 0],
           [0, 0, 4, 0, 4, 2, 0, 0],
           [4, 0, 0, 4, 0, 0, 2, 0],
           [0, 0, 0, 2, 0, 0, 2, 2],
           [0, 0, 0, 0, 2, 2, 0, 0],
           [3, 0, 0, 0, 0, 2, 0, 0]]

print(shag(way=[], time=0, x=0))
