import pyautogui
import time

def press_keys(times):
    for _ in range(times):
        time.sleep(0.1)
        pyautogui.press('up')
        pyautogui.press('right')
        pyautogui.press('space')

if __name__ == "__main__":
    x = int(input("Enter the number of times to press the keys: "))
    time.sleep(5)
    press_keys(x)
