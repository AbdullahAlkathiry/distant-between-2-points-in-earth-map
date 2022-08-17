import numpy as np
import math as m
from scipy.optimize import fsolve


def change_pic1(lat, long):
    lat1 = np.array(lat)
    lat1 = lat1*m.pi/360 + m.pi/4
    long1 = np.array(long)
    x = 8.1*long1+1410
    y = 1510 - 489.5 * np.log(np.tan(lat1))
    return np.array([x, y])


def change_pic2(lat, long):
    lat1 = np.array(lat)
    lat1 = lat1*m.pi/360 + m.pi/4
    long1 = np.array(long)
    x = 7.324*long1 + 1501
    y = 1338 - 426.953 * np.log(np.tan(lat1))
    return np.array([x, y])


def det_constant(x1, y1, x2, y2):
    def equations(var):
        z, w = var
        eq1 = z*m.tan(x1) - m.sin(y1 - w)
        eq2 = z*m.tan(x2) - m.sin(y2 - w)
        return [eq1, eq2]
    z, w = fsolve(equations, (1, 1))
    return z, w


def det_path(lat1, long1, lat2, long2):
    k, phi = det_constant(lat1, long1, lat2, long2)
    if lat1 > lat2:
        temp = lat1
        lat1 = lat2
        lat2 = temp
        temp = long1
        long1 = long2
        long2 = temp
    lats = m.atan(1 / k)
    end2 = abs(m.asin(k * m.tan(lat2)) + phi - long2) <= 0.009
    end1 = abs(m.asin(k * m.tan(lat1)) + phi - long1) <= 0.009
    end11 = abs(m.asin(-k * m.tan(lat1)) + phi + m.pi - long1) <= 0.009
    end22 = abs(m.asin(-k * m.tan(lat2)) + phi + m.pi - long2) <= 0.009
    end1s = abs(m.asin(-k * m.tan(lat1)) + phi - m.pi - long1) <= 0.009
    end2s = abs(m.asin(-k * m.tan(lat2)) + phi - m.pi - long2) <= 0.009
    print([end2, end1, end11, end22, end1s, end2s])
    if end1 and end2:
        lat = np.arange(start=lat1, stop=lat2, step=(lat2 - lat1) / 500)
        long = np.arcsin(k * np.tan(lat)) + phi
    elif end1:
        if end22:
            lat1s = np.arange(start=lat1, stop=lats, step=(lats - lat1) / 250)
            lat2s = np.arange(start=lats, stop=lat2, step=(lat2 - lats) / 250)
            long1s = np.arcsin(k * np.tan(lat1s)) + phi
            long2s = np.arcsin(-k * np.tan(lat2s)) + phi + m.pi
        else:
            lats = -lats
            lat1s = np.arange(start=lat1, stop=lats, step=(lats - lat1) / 250)
            lat2s = np.arange(start=lats, stop=lat2, step=(lat2 - lats) / 250)
            long1s = np.arcsin(k * np.tan(lat1s)) + phi
            long2s = np.arcsin(-k * np.tan(lat2s)) + phi - m.pi
        lat = np.append(lat1s, lat2s)
        long = np.append(long1s, long2s)
    elif end2:
        if end11:
            lat1s = np.arange(start=lat1, stop=lats, step=(lats - lat1) / 250)
            lat2s = np.arange(start=lats, stop=lat2, step=(lat2 - lats) / 250)
            long1s = np.arcsin(-k * np.tan(lat1s)) + phi + m.pi
            long2s = np.arcsin(k * np.tan(lat2s)) + phi
        else:
            lats = -lats
            lat1s = np.arange(start=lat1, stop=lats, step=(lats - lat1) / 250)
            lat2s = np.arange(start=lats, stop=lat2, step=(lat2 - lats) / 250)
            long1s = np.arcsin(-k * np.tan(lat1s)) + phi - m.pi
            long2s = np.arcsin(k * np.tan(lat2s)) + phi
        lat = np.append(lat1s, lat2s)
        long = np.append(long1s, long2s)
    elif end1s and end2s:
        lat = np.arange(start=lat1, stop=lat2, step=(lat2 - lat1) / 500)
        long = np.arcsin(-k * np.tan(lat)) + phi - m.pi

    lat = lat * 180 / m.pi
    long = long * 180 / m.pi
    print(str(k)+" // "+str(phi))
    return lat, long


