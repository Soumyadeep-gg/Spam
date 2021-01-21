import time
import datetime
import pyautogui
#install the pyautogui pip

Text = input('Enter your message-')

#datetime format = (year, month, day, hour, minute, second)
send_time = datetime.datetime(2021,1,21,12,22,00)
time.sleep(send_time.timestamp() - time.time())

for i in range(15):
        pyautogui.typewrite(Text)
        pyautogui.press('enter')
        time.sleep(.5)


# Put the cursor wherever you want to spam your massege.
print('done')
