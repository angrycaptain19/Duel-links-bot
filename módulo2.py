import pyautogui
import módulo1
import time
import os

location = 0


#time.sleep function makes the program work on slower connections
#location_arr[0] = pvp, location_arr[1] = cart, location_arr[2] = gam, location_arr[3] = gate 
location_arr = [(623.5, 693.5), (747.5, 697.0), (856.5, 698.0), (500.5, 694.5)]


def imagesearch(image, threshold, minthreshold = .6, repeat = 5, out = 0):
 
 #takes a screenshot of current frame at given region
 master = pyautogui.screenshot(region=(438, 350, 480, 346))
 master.save("master.png")
 

 #calls módulo1.get_coords function (this function returns either false or a set of coordinates [x, y])
 gg = módulo1.get_coords("master.png", image, threshold, minthreshold, out)


 #parameter to return False, repeat = num of frames wanted, each cycle rests one to "repeat"
 if repeat == 0 and gg == False:
   return False

 elif gg == False:
   return imagesearch(image, threshold, minthreshold, repeat - 1, out)

 else:
   return gg


#clicks given coords [x, y]
def click_image(coords, clicks):
 if coords == False:
   return
 #filter known false positives 
 if coords == [778.5, 410.0] or coords == [712.5, 433.5] or coords == [760.5, 449.1666666666667] or coords == [698.0, 456.5] or coords == [481.5, 559.5] or coords == [703.0, 608.5] or coords == [712.5, 433.5] or coords == [670.5, 461.0] or coords == [644.5, 608.5] or coords == [748.5, 447.5] or coords == [693.1666666666667, 510.5] or coords == [808.5, 694.5]:
  return coords
 else:
  #loop for every click
  for each in range(clicks):
   pyautogui.click(coords)
  return coords


#searches for opponent and initiates a duel
def search_npc():
 global location
 global location_arr


 print(location) 
 time.sleep(3)
 grant_reward()
 time.sleep(2)
 #searches for character image and clicks on it
 print("character")
 ttg = imagesearch("character" + ".png", .96, .7) 
 print(ttg)
 click_image(ttg, 1)
 time.sleep(5)
 
 #searches for skip image and clicks on it,
 print("skip_dialogue")
 ttg = imagesearch("skip_dialogue" + ".png", .8, .78)

 #if imagesearch cant find any opponent dialogue, changes location; if a character is found, clicks on character location  
 if ttg == False and location == 3:
   print("False1")
   location = 0
   click_image(location_arr[location], 1)
   return search_npc()
 elif ttg == False and location != 3:
   print("False2")
   location += 1
   click_image(location_arr[location], 1)
   return  search_npc()
 else: 
   print(ttg)
   click_image(ttg, 1)
   time.sleep(3)

   #searches for auto-duel image and clicks on it
   print("auto")
   ffg = imagesearch("auto-duel" + ".png", .96, .9)
   click_image(ffg, 1)






#clicks given coordinates until some image is visible (skip) [x, y]
def duel_skip(skip, coords): 
 print("duel skip")
 ttg = imagesearch(skip + ".png", .8, .78)
 if ttg != False:
   time.sleep(2)
   click_image(ttg, 2)
 elif ttg == False:
   click_image(coords, 1)
   return duel_skip(skip, coords)   

#grants rewards depending on location 
def grant_reward():
 print("granting reward...")
 global location
 if location == 0:
   click_image([800.0, 460.5], 1)
   time.sleep(2)
   return
 elif location == 1:
   click_image([663.5, 384.0], 1)
   time.sleep(2)
   return   
 elif location == 2:
   click_image([600.0, 587.0], 1)
   time.sleep(2)
   return      
 elif location == 3:  
   click_image([680.0, 389.0], 1)
   time.sleep(2)
   return
 time.sleep(4)
 ttg = imagesearch("ok_reward.png", .96, .8)
 click_image(ttg, 1)


def pvp_duel():
  while True:
   print("looking for: pvp_page")
   rfg = imagesearch("pvp_page" + ".png", .96, .9, 2)
   if rfg == False:
     print("pvp page == False")
     click_image([680.5, 381.0], 1)
  
   time.sleep(5)   
   print("click on duel")
   click_image([688.0, 189.5], 1)  
   time.sleep(2)
   click_image([684.0, 354.5], 1)
   print("dueling")
   duel_skip("nice", [893.0, 480.5])
   duel_skip("duel", [1090.5 -410 , 1045.5 - 360])



#function to find npc and duel with them
def find_npc_duel():
 while True:
  #if refill image is visble, refills orbs
  rfg = imagesearch("refill" + ".png", .96, .7)
  if rfg != False:
    click_image([721.5, 273], 1)
    time.sleep(2)
    click_image([731.5, 438.5], 1)
    time.sleep(2)
    click_image([651.0, 453.5], 1)
  #searches for opponent and initiates a duel
  search_npc()
  time.sleep(10)
 
  #clicks given coordinates until the duel is over and character dialogue is visible
  duel_skip("skip_dialogue", [1090.5 -410 , 1045.5 - 360])




#function to find npc and duel with them (no orbs)
def find_npc_duel_no_orb():
 while True:
  #if refill image is visible close it
  rfg = imagesearch("refill" + ".png", .96, .7)
  if rfg != False:
    print("closing refill...")
    click_image([652.0, 669.5], 1)
  #searches for opponent and initiates a duel
  search_npc()
  time.sleep(10)
 
  #clicks given coordinates until the duel is over and character dialogue is visible
  duel_skip("skip_dialogue", [1090.5 -410 , 1045.5 - 360])