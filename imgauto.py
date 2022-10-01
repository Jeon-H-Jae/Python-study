import pyautogui
# 사진따오기 함수 pyautogui.screenshot('1.png',region=(x,y,x_num,y_num))
pyautogui.moveTo(1035,853)
pyautogui.screenshot('1.png',region=(1018,841,50,50)) # 1018,841
i= pyautogui.locateCenterOnScreen('1.png',confidence=0.9)
pyautogui.click(i)