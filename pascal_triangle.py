def calc_new_line(line):
    """
    Receives 1 line of the triangle, and creates another one
    """
    res = [1]
    for i in range(1, len(line)):
        res.append(line[i-1]+line[i])
    res.append(1)
    return res


if __name__ == "__main__":
    size = int(input("Enter size of the triangle: "))
    res = [[1]]
    for _ in range(size):
        new_line = calc_new_line(res[-1])
        res.append(new_line)
    print(res)
