from PIL import Image
import numpy as np
img = Image.open('nine2.png')

data = list(img.getdata())
# print(data)
data = list(np.concatenate(data).flat)
# print(data)
for i in range(len(data)):
    data[i] = 255 - data[i]
print(data)


