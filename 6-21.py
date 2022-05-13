#21,22
while True:
    char = input("문자입력(quit:종료): ")
    if char == 'quit':
        break
    elif char>='a'and char <='z':
        print(str(char)+"의 대문자:"+chr(ord(char)-32))
    elif char>='A'and char <='Z':
        print(str(char)+"의 소문자:"+chr(ord(char)+32))
    else:
        print("잘못된 값을 입력하셨습니다.")


    
"""
print(ord('a'))
print(ord('A'))

char = 'f'
print(chr(ord(char)+32))
"""

