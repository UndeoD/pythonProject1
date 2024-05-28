import f321
import pyautogui as bot
print('hello world')


f321.start()
bot.hotkey('win', 'r')
bot.typewrite('cmd')
bot.press('enter')
f321.finish()