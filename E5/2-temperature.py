T = int(input())
if -273 < T < 6000:
    if T > 100:
        print('Steam')
    elif T < 0:
        print('Ice')
    else:
        print('Water')