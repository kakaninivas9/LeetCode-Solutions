import pyautogui
import time
def towrite_forcodenow():
    
    print("typing start in 3sec")
    time.sleep(3)

    text = '''text'''

    lines = text.splitlines()
    for _ in range(len(lines)):
        pyautogui.press('enter')
        
    for _ in range(len(lines)):
        pyautogui.press('up')
    
    for line in lines:
        pyautogui.write(line, interval=0.02)
        pyautogui.press('escape')
        pyautogui.press('down')

towrite_forcodenow()
