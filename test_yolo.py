import cv2
from PIL import Image

import YOLOv3
from YOLOv3 import Recognition

img = cv2.imread('1593173590.jpg')
print(img.shape)

img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img3 = Image.fromarray(img2)



my  = Recognition()



print('---------------------------------\n' \
     + 'recognistion: ' + str(my.recognition(img3)))



#cv2.imshow('x',img2)
#cv2.waitKey(0)
#cv2.destroyAllWindows()




