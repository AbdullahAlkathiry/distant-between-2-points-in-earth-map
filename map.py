import numpy as np
from matplotlib import pyplot as plt
from coordinate_change import det_path, change_pic2
import math as m


lat1 = float(input("enter the lattiude of the first point : "))*m.pi/180
long1 = float(input("enter the longitude of the first point : "))*m.pi/180
lat2 = float(input("enter the lattiude of the second point : "))*m.pi/180
long2 = float(input("enter the longitude of the second point : "))*m.pi/180
lat, long = det_path(lat1, long1, lat2, long2)
x, y = change_pic2(lat, long)
im = plt.imread("WRLD2.jpg")
plt.imshow(im)
print(str(long[499]) + " /// " + str(lat[499]))
print(str(long[0]) + " /// " + str(lat[0]))
plt.plot(x, y)
plt.xlim(0, 3000)
plt.ylim(2550, 0)
plt.show()

