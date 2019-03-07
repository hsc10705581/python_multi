<<<<<<< HEAD
#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

import os
import numpy as np
import sys
from PIL import Image

path = "C:/characters/"
pics = os.listdir(path)
for pic in pics:
    img = Image.open(path + pic)
    img = img.convert('RGBA')

    ar = np.array(img)
    np.set_printoptions(threshold=1e6)
    for i in range(len(ar)):
        for j in range(len(ar[i])):
            pixel = ar[i][j]
            if pixel[0] == 255 and pixel[1] == 255 and pixel[2] == 255:
                ar[i][j][3] = 0
    img = Image.fromarray(ar, 'RGBA')
=======
#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

import os
import numpy as np
import sys
from PIL import Image

path = "C:/characters/"
pics = os.listdir(path)
for pic in pics:
    img = Image.open(path + pic)
    img = img.convert('RGBA')

    ar = np.array(img)
    np.set_printoptions(threshold=1e6)
    for i in range(len(ar)):
        for j in range(len(ar[i])):
            pixel = ar[i][j]
            if pixel[0] == 255 and pixel[1] == 255 and pixel[2] == 255:
                ar[i][j][3] = 0
    img = Image.fromarray(ar, 'RGBA')
>>>>>>> first commit
    img.save(path + pic)