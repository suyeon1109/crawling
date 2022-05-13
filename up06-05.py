#5
for y in range(1,6):
    for g in range(y):
        print(' ', end='')
    for x in range(6-y):
        print('*', end='')
    print('\n')



#6
for y in range(1,10):
    for g in range(y):
        print(' ', end='')
    for x in range(10-y*2-1):
        print('*', end='')
    print('\n')
