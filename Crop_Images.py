#**Crop to bounding box.  Only run with full resolution images.**

import PIL
import os
import os.path
from PIL import Image

f = r'./cars196_train'
#f = r'./cars196_test'
index = 0

for file in sorted(os.listdir(f)):

     # x1 = test_annotations[index][1][0]
     # y1 = test_annotations[index][1][1] 
     # x2 = test_annotations[index][1][2]
     # y2 = test_annotations[index][1][3]

     x1 = train_annotations[index][1][0]
     y1 = train_annotations[index][1][1] 
     x2 = train_annotations[index][1][2]
     y2 = train_annotations[index][1][3]

    
    
     f_img = f+"/"+file
     print(f_img)
     if(file != '.DS_Store'):
         img = Image.open(f_img)
         img = img.crop((x1,y1,x2,y2))
         img.save(f_img)
         index = index + 1