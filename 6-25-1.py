while True: 
    while True:
        ch = input("더하기(A), 빼기(S), 곱하기(M),나누기(D)`n원하는 연산 선택: ")
        if ch=='A' or ch=='a' or ch=='S' or ch=='s' or ch=='M' or ch=='m' or ch=='d'or ch=='D':
            break
        
        #else:
        print("A,S,M,D중 하나만 입력하세요")

    a = int(input("첫 번째 숫자: "))
    b = int(input("두 번째 숫자: "))

    if ch == 'A' or ch=='a': print("정답:", a+b)
    elif ch == 'S' or ch=='s': print("정답:", a-b)
    elif ch == 'M' or ch=='m': print("정답:", a*b)
    elif ch == 'D' or ch=='d':
        while True:
            if b!=0:
                print("정답:", a/b)
                break
            else:
                print("0으로 나눌수 없습니다.")
                b = int(input("두 번째 숫자: "))


    ctn = input("계속(아무키나), 종료(Q/q): ")
    if ctn == 'q' or ctn =='Q':
        break





# ; if b!=0:
# ;     print("정답:", a/b)
# ; else:
# ;     print("0으로 나눌수 없습니다.")
# ;     while b>=0:
# ;         b = int(input("두 번째 숫자: "))
# ;         if b!=0:
# ;             break
