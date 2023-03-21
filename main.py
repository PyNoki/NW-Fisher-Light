from imports import *

keyboard = Controller()

#  ======== settings ========
resume_key = Key.f1
pause_key = Key.f2
exit_key = Key.backspace
#  ==========================

pause = True
running = True

def on_press(key):
    global running, pause

    if key == resume_key:
        pause = False
        print("[Resumed]")
    elif key == pause_key:
        pause = True
        print("[Paused]")
    elif key == exit_key:
        running = False
        print("[Exit]")

def display_controls():
    print("Autofisher is running")
    print("- Controls:")
    print("\t f1 = Resume")
    print("\t f2 = Pause")
    print("\t backspace = Exit")
    print("-----------------------------------------------------")
    print('Press f1 to start ...')

def main():
    forceReset = 0
    status = ''

    lis = Listener(on_press=on_press)
    lis.start()

    display_controls()
    while running:
        if not pause:

            if status == '':
                if pyautogui.locateOnScreen('casticon.png', confidence = 0.8) != None:
                    print ('Ready to cast, I see casticon')
                    status = 'casting'

            if status == 'casting':
                print('Moved to casting status')
                time.sleep(1.5)
                
                pydirectinput.keyUp('altleft')
                time.sleep(1.5)
                pydirectinput.keyDown('a')
                time.sleep(0.05)
                pydirectinput.keyUp('a')
                time.sleep(0.05)
                pydirectinput.keyDown('d')
                time.sleep(0.05)
                pydirectinput.keyUp('d')
                time.sleep(1.5)

                pydirectinput.keyDown('-')
                time.sleep(0.3)
                pydirectinput.keyUp('-')
                print('pressed the cast key ')
                time.sleep(1.5)

                if pyautogui.locateOnScreen('polecastedv2.png', confidence = 0.8) != None:
                    status = 'waitingOnBite'
                    print('I see the bobber, waiting on a fishy')

            if status == 'waitingOnBite':
                if pyautogui.locateOnScreen('bite.png', region=(743,220,451,707), confidence = 0.8) != None:
                    pydirectinput.keyDown('-')
                    time.sleep(0.1)
                    pydirectinput.keyUp('-')
                    print('gotcha bitch')
                    pydirectinput.keyDown('altleft')
                    status = 'tugtime'


            if status == 'tugtime':

                if pyautogui.locateOnScreen('f3.png', region=(743,220,451,707), confidence = 0.8) != None or pyautogui.locateOnScreen('polecastedv2.png', region=(743,220,451,707), confidence = 0.8) != None:
                    print('Noticed an icon that shouldnt be here, resetting')
                    forceReset = 7
                    status = ''

                if pyautogui.locateOnScreen('hold1.png', region=(743,220,451,707), confidence=0.6) != None or pyautogui.locateOnScreen('hold2.png', region=(743,220,451,707), confidence=0.8) != None or pyautogui.locateOnScreen('hold3.png', region=(743,220,451,707), confidence=0.9) != None:
                    pydirectinput.keyDown('-')
                    print('Pulling')
                    forceReset = 0

                else:
                    pydirectinput.keyUp('-')
                    print('Releasing')
                    forceReset += 1

                    if forceReset == 7:
                        print('Force reset activated - checking if still fighting the fish')
                        if pyautogui.locateOnScreen('hold1.png', region=(743,220,451,707), confidence=0.6) == None and pyautogui.locateOnScreen('hold2.png', region=(743,220,451,707), confidence=0.8) == None and pyautogui.locateOnScreen('hold3.png', region=(743,220,451,707), confidence=0.9) == None and pyautogui.locateOnScreen('hold2.png', region=(743,220,451,707), confidence=0.8) == None:
                            print('Doesnt look like youre fighting the fish anymore, resetting')
                            status = ''


    lis.stop()

if __name__ == "__main__":
    main()
