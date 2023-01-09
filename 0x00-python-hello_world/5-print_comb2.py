for i in range(0, 100):
    print("{0:0=2d},".format(i), end=" ")
    if i == 99:
        print("{}\n".format(i))
