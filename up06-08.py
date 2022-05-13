money = int(input("금액을 입력하시오: "))
num = 10000
n=1
while n<=9:
    m = money//num 
    print(str(num)+"원:", str(m)+"장(개)")
    money%=num 

    if n%2!=0:
        num //= 2
    else:
        num//=5
    n+=1

        
#     print()
#     money-=money
#     if money ==0:
#         break
#     break

# if money >= 10000:
#     print(str(money//10000)+"장(개)")
#     money -= money//10000
# if money >= 5000 and money < 10000:
#     print(str(money//5000)+"장(개)")
#     money -= money//5000
# if money >= 1000 and money <5000:
#     print(str(money//1000)+"장(개)")
#     money -= money//1000
# if money >= 500 and money <1000:
#     print(str(money//500)+"장(개)")
#     money -= money//500
# if money >= 100 and money <500:
#     print(str(money//100)+"장(개)")
#     money -= money//100
# if money >= 50 and money <100:
#     print(str(money//50)+"장(개)")
#     money -= money//50
# if money >= 10 and money <50:
#     print(str(money//10)+"장(개)")
#     money -= money//10
# if money >= 5 and money <10:
#     print(str(money//5)+"장(개)")
#     money -= money//5
# else:
#     print(str(money//1)+"장(개)")    


        # if money >= 10**(5-i) and money<(10**(5-i))*5:
        #     print(str(money//(10**(5-i)))+"장(개)")
        #     money -= money//(10**(5-i))
        # elif money >= 5*10**(5-i) and money < 5*10**(5-i)*2:
        #     print(str(money//(5*10**(5-i)))+"장(개)")
        #     money -= money//(5*10**(5-i))

    # if i%2==0:
    #     won = int('5'+('0'*(2*i-1)))
    # else:
    #     won = int('1'+('0'*(2*i-1)))