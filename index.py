import pandas as pd
import pyautogui 
import time

pyautogui.PAUSE = 3.0

pyautogui.press("win")
pyautogui.write("firefox")
pyautogui.press("enter")

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")


pyautogui.click(x=721, y=462)
pyautogui.write("mathcarvalhobarreto@gmail.com")
pyautogui.click(x=850, y=582)
pyautogui.write("123456")
pyautogui.click(x=942, y=664)