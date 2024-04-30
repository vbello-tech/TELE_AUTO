import pyautogui
import time

with open('list.txt', 'r') as file:
    #  Read the contents of the file
    user_list = usernames = file.read().splitlines()

#  user_list = ["@officialsehnz", "@o_fun1", "@Isaacnew980", "@Afokaz17"]
# Now 'usernames' contains all the usernames from the file
print(user_list)

message = ("Hi, I am also in the English group. I wanted to create the most amazing fashion channel so I had an idea "
           "using AI to create fashion. I invite you to my new channel so you can have a look. This is the link: "
           "https://t.me/fashionbyai")

for user in user_list:
    print(" sending to ", user)
    time.sleep(2)
    print("starting")
    pyautogui.press('esc')
    time.sleep(2)
    pyautogui.write(str(user));
    time.sleep(5)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.write(str(message));
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.press('esc')
    time.sleep(2)
    pyautogui.press('esc')

print('The script executed successfully.')
