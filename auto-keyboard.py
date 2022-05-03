import pyautogui
import pyperclip
import time

# pyperclip.copy("안녕 나는 수연이야.")
# pyautogui.hotkey('command', 'v')

#키보드로 문자열 작성하기
# pyautogui.write('Hello World', interval=0.4) #하나칠때마다 0.4초

# #press, keyDown, keyUp
# pyautogui.press('command')
# pyautogui.press('v')


# time.sleep(3)
# print(pyautogui.position())
pyautogui.moveTo(580,875,2)
pyautogui.doubleClick()
pyautogui.moveTo(298,101,2)
pyautogui.click(button='left')
pyautogui.write("dkssud sksms tndusdldi")