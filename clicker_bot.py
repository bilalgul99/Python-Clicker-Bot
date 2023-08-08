import keyboard
import pyautogui
import time
# Get the coordinates of the first position to click
x1, y1 = -1,-1

# Get the coordinates of the second position to click
x2, y2 = -1, -1
click=True
def on_press(event):
    global x1, y1,x2, y2,click
    
    if event.name == 'a':
        # Record the current position when the 'a' key is pressed
        x1, y1 = pyautogui.position()
        print(f'Recorded position for "a": ({x1}, {y1})')
    
    elif event.name == 'b':
        # Record the current position when the 'b' key is pressed
        x2, y2 = pyautogui.position()
        print(f'Recorded position for "b": ({x2}, {y2})')
    elif event.name == 'q':
        print('exiting')
        click=False

keyboard.on_press(on_press)
if click:
    while x2==-1 or y2==-1:
        if not click:
            break
        pass
print("starting")
# Keep clicking the mouse at the recorded positions repeatedly with a time gap of 1 second
while click:
    pyautogui.click(x=x1,y=y1)
    #pyautogui.press('f5')
    time.sleep(3)
    pyautogui.click(x=x2,y=y2)
    time.sleep(3)
