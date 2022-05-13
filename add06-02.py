while True:
    num = int(input("정수를 입력해주세요: "))
    if num<0:
        pass
    else:
        for i in range(0,num):
            print(num-i,end='')
    break
