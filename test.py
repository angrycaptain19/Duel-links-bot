import pyautogui
import módulo1
import time

def click_image(coords, clicks):
 if coords == [698.0, 456.5] or coords == [481.5, 559.5] or coords == [703.0, 608.5] or coords == [712.5, 433.5]:
  return coords
 else:
  for each in range(clicks):
   pyautogui.click(coords)
  return coords

master = pyautogui.screenshot(region=(438, 350, 480, 346))
#master = pyautogui.screenshot()

master.save("master.png")
ttg = módulo1.get_coords("master.png", "close_orbs.png", .96, .8, 2)
print(ttg)
print([ttg[0] - 410, ttg[1] - 360])


#click_image([ttg[0] - 410, ttg[1] - 360], 1)
click_image(ttg, 1)
