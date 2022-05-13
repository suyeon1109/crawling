#24

while True:
    year = int(input("연도를 입력하시오: "))
    if year==0:
        print("The End")
        break
    month = int(input("월을 입력하시오: "))
    day=0

    if month == 4 or month == 6 or month == 9 or month == 11:
        day=30
    elif month == 2:
        if (year%4==0 and year%100!=0) or year%400==0:
            day=29
    else:
        day=31

    print(str(year)+"년", str(month)+"월의 날수는", str(day)+"입니다")
