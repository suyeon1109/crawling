while True:
    num = int(input("정수를 입력해주세요: "))
    if num <0:
        pass
    else:
        for i in range(1,num+1):
            print(i,end='')
    break