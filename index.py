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
pyautogui.write("mattcb@gmail.com")
pyautogui.press("tab")
pyautogui.write("123456")
pyautogui.press("tab")
pyautogui.press("Enter")

table = pd.read_csv("products.csv")

for line in table.index:
    
    price = str(table.loc[line, "preco_unitario"])
    category = str(table.loc[line, "categoria"])
    cost = str(table.loc[line, "custo"])
    code = str(table.loc[line, "codigo"])

    pyautogui.click(x=1019, y=20)
    pyautogui.write(code)

    pyautogui.write(table.loc[line, "marca"])

    pyautogui.press("tab")
    pyautogui.write(table.loc[line, "tipo"])

    pyautogui.press("tab")
    pyautogui.write(category)
    
    pyautogui.press("tab")
    pyautogui.write(price)

    pyautogui.press("tab")
    pyautogui.write(cost)

    pyautogui.press("tab")
    pyautogui.write(table.loc[line, "obs"])

    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(5000)