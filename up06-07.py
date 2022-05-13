# for a in range(1,5):
#     for x in range(5-a):
#         print(' ', end='')
#     for y in range(65,a+66):
#         #for z in range(65,72):
#         print(chr(y), end='')
#     print('\n')

# 마지막 for문에서 홀수 나오게 해야되는건 알겠는데 어떻게 할지를 모르겠음


for a in range(1,5):
    ch=65
    for x in range(5-a):
        print(' ', end='')
    #ch=65
    for y in range(a*2-1):
        print(chr(ch), end='')
        ch+=1
    print('\n')