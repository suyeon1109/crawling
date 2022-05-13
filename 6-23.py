#23

while True:
    n=int(input("번호 = "))
    if n == 0:
        print("goodbye")
        break
         
    else:
        kor=int(input("국어 = "))
        eng=int(input("영어 = "))
        math=int(input("수학 = "))

        max = kor

        if max<eng:
            max=eng
        if max < math:
            max=math
        print("최댓값은 "+str(max)+"입니다.")