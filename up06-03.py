#up06-03

import random
com = random.randrange(1,101)
print("컴퓨터:",com)

n=1
num=0

while n <= 10:
    chance = int(input(str(n)+"번째 기회: "))
    if chance==com:
        print("정답")
        break
    elif chance>com:
        print("커요")
    else:
        print("작아요")

    if n==10:
        print("끝! 정답:",com)
        break
    
    n+=1