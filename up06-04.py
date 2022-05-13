# min_num = 99
# max_num = 10

# count = int(input("몇개의 데이터를 입력 받을 건가요? "))
# print(str(count)+"개의 데이터를 입력하세요")

# for n in range(1,count+1):
#     while True:
#         num = int(input(str(n)+"번째 데이터 입력: "))
#         if num >= 10 and num<=99:
#             break
#         else:
#             print("***2자리 정수를 입력하세요***")
#     if min_num>=num:
#         min_num = num
#     if max_num <= num:
#         max_num=num

# print("최댓값:", max_num, "최소값:", min_num)



min_num = 0
max_num = 0

count = int(input("몇개의 데이터를 입력 받을 건가요? "))
print(str(count)+"개의 데이터를 입력하세요")

for n in range(1,count+1):
    num = int(input(str(n)+"번째 데이터 입력: "))
    if n==1:
        min_num = num
        max_num = num
    if min_num>=num:
        min_num = num
    if max_num <= num:
        max_num=num

print("최댓값:", max_num, "최소값:", min_num)