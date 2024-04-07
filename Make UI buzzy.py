import pyautogui
import pyautogui
import time

# Set the size of each side of the square
side_length = 100

while True:



    # Move right
    pyautogui.moveRel(side_length, 0)
    time.sleep(5)  # Pause for half a secondc


       # Scroll down
    pyautogui.press('pagedown')
    time.sleep(10)  # Adjust timing as needed


       # Scroll down
    pyautogui.press('pagedown')
    time.sleep(10)  # Adjust timing as needed


    # Move right
    pyautogui.moveRel(side_length, 0)
    time.sleep(10)  # Pause for half a second

  
       # Scroll up
    pyautogui.press('pageup')
    time.sleep(10)  # Adjust timing as needed


    # Press Control + Tab
    pyautogui.hotkey('ctrl', 'tab')
    time.sleep(15)



       # Scroll down
    pyautogui.press('pagedown')
    time.sleep(10)  # Adjust timing as needed



       # Scroll down
    pyautogui.press('pagedown')
    time.sleep(10)  # Adjust timing as needed


       # Scroll down
    pyautogui.press('pagedown')
    time.sleep(10)  # Adjust timing as needed



    # Move down
    pyautogui.moveRel(0, side_length)
    time.sleep(17)

    # pyautogui.press('enter')
    # time.sleep(10)

    # Move left
    pyautogui.moveRel(-side_length, 0)
    time.sleep(15)



       # Scroll down
    pyautogui.press('pagedown')
    time.sleep(10)  # Adjust timing as needed


    # Move up
    pyautogui.moveRel(0, -side_length)
    time.sleep(12)

