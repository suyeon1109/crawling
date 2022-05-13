while True:
    num = int(input("정수를 입력해주세요: "))
    if num%10!=0:
        print(str(num)+"는 10으로 나눠지지 않습니다")
    elif num%10==0:
        print(str(num)+"는 10으로 나누어집니다")
    ans = input("한번 더? [Yes...0/No...any]: ")
    if ans=='0':
        continue
    else:
        break