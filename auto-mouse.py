import pyautogui
import time

# #화면크기 출력
# print(pyautogui.size())

# #시간차 두기
# time.sleep(2) #안에 몇초인지 넣기

# #마우스의 현재위치 받기 (x,y)
# # print(pyautogui.position())
# # x,y = pyautogui.position() #저장
# # print(x,y)

# pyautogui.moveTo(63,791, 2) #x,y,duration(float)
# pyautogui.click() #button='left' or 'right' / 비워두면 무조건 왼쪽
# pyautogui.doubleClick()

#마우스 드래그
# print(pyautogui.position())
# time.sleep(2)
# print(pyautogui.position())
# pyautogui.moveTo(355,122,2)
# pyautogui.dragTo(629,396,2, button = 'left')


# time.sleep(5)
# print(pyautogui.position())
# pyautogui.moveTo(1373,406,2)
# pyautogui.dragTo(1373,407,2, button = 'left')
# pyautogui.dragTo(1370,603,2, button = 'left')

pyautogui.moveTo(1371,512,2)
time.sleep(1)
pyautogui.click(button='right')
pyautogui.moveTo(1214,390,2)
pyautogui.click(button='left')
pyautogui.moveTo(810,162,2)
pyautogui.doubleClick()
pyautogui.dragTo(684,241,2, button = 'left')
pyautogui.moveTo(1363,723,2)