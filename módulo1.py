import cv2
import numpy
from matplotlib import pyplot



#gives coordinates of desired image, master is the image in which to find everything;
#find is the image to find, e is maximum threshold, mine is minimum threshold and out is a test parameter;
#shows a rectangle on master image with image to find
def get_coords(master, find, e, mine, out):

 #if threshold < minimum threshold returns False
 if e < mine:
  return False
 else:
  #rounds threshold value to 3 decimals
  threshold = round(e, 3)
  
  
  #reads master image and splits it into R, G, B channels
  img_rgb = cv2.imread(master)
  img_B, img_G, img_R = cv2.split(img_rgb)

  #reads template image (find), splits it into R, G, B channels and gets height, width and  depth
  template = cv2.imread(find)
  template_B, template_G, template_R = cv2.split(template)
  h, w, s = template.shape


  
  #compares blue channel of both images and stores the values that exceed or equal threshold
  resB = cv2.matchTemplate(img_B,template_B,cv2.TM_CCOEFF_NORMED)
  locate = numpy.where( resB >= threshold)
  
  #if find image is not found len(locate[0]) and len(locate[1]) equal zero;
  # function is restarted with a threshold value - 0.025
  if len(locate[0]) == 0 & len(locate[1]) == 0:
    return get_coords(master, find, threshold - 0.025, mine, out)
  else:
    #checks for out function
    if out != 0:  
     #locate is zipped and unziped    
     tg = zip(*locate[::-1])
     print("out, press any key to exit...")
     for each in tg:    
        #draws a rectangle
        cv2.rectangle(img_rgb, each, (each[0] + w, each[1] + h), (0,255,0), 2) 
     #shows image and waits for a key-stroke       
     cv2.imshow(str(out)+'.png',img_rgb)
     cv2.waitKey(0)
        
    #locate is zipped    
    gg = zip(*locate[::-1])

    #variable cx1y1 gets initialized 
    cx1y1 = []
    #locate is unzipped and x, y values get stored in cx1y1
    for each in gg:    
     cx1y1 += [each]
    
    lenx1 = len(cx1y1) 
    #average x1 and y1 coords 
    avx1 = 0
    avy1 = 0

    #sums every x, y coordinate 
    for each in range(lenx1):
     avx1 += cx1y1[each][0]  
     avy1 += cx1y1[each][1]
    

    #calculates centroid of image (coords)
    a = avx1/lenx1, avy1/lenx1
    b = a[0] + w, a[1] + h
    c = b[0] - w, b[1]
    d = b[0], b[1] - h

    pmbase = (b[0] + c[0])/2
    pmaltura = (a[1] + c[1])/2
    print("trust lvl= " + str(threshold))
    #returns centroid of image and sums x and y values to match screen coordinates 
    return [pmbase + 410, pmaltura + 360]
  
