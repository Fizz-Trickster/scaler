# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 04:52:25 2021

@author: yoonys
"""

import numpy as np
from scipy.interpolate import interp1d

def ppmDatainfo(i_dataList):
    o_ppmDatainfo = {}
    o_ppmDatainfo['FileFormat'] = i_dataList.pop(0).rstrip()
    o_ppmDatainfo['Hresolution'], o_ppmDatainfo['Vresolution'] = i_dataList.pop(0).split()
    o_ppmDatainfo['MaxValue'] = i_dataList.pop(0).rstrip()
    
    o_ppmDatainfo['Hresolution'] = int(o_ppmDatainfo['Hresolution'])
    o_ppmDatainfo['Vresolution'] = int(o_ppmDatainfo['Vresolution'])
    o_ppmDatainfo['MaxValue'] = int(o_ppmDatainfo['MaxValue'])
    
    return o_ppmDatainfo

def ppmDataList(i_dataList):
    o_ppmData = []
    for pixel in i_dataList:
        buf = []
        for subpixel in pixel.split():
            buf.append(int(subpixel))
        o_ppmData.append(buf)
        
    return o_ppmData

# f = open('./image/Hgrad_128x128_8bpc.ppm', 'r')
# f = open('./image/checker_128x100_8bpc.ppm', 'r')
f = open('./image/checkerRed_128x100_8bpc.ppm', 'r')

dataline = f.readlines()

ppmHeader = ppmDatainfo(dataline)

ppmData = ppmDataList(dataline)

ndarr = np.array(ppmData)

temp = ndarr.reshape(ppmHeader['Vresolution'], ppmHeader['Hresolution'], 3)
arr_ppm = ndarr.reshape(ppmHeader['Vresolution'], ppmHeader['Hresolution'], 3)

data_R = temp[:, :, 0]
data_G = temp[:, :, 1]
data_B = temp[:, :, 2]

x = np.linspace(0,127,128)
y = np.linspace(0,99,100)
f1 = interp1d(x, data_R[0])
print(f1(2.5))

xx = np.empty((0,128))

for idx in range(0,100):
    xx = np.append(xx,np.array([x]),axis=0)
    
f2_R = interp1d(x, data_R)
f2_G = interp1d(x, data_G)
f2_B = interp1d(x, data_B)
print(f2_R(126), f2_R(127), f2_G(100.5), f2_B(100.5))

o_data_R = np.empty((0,100),int)
for idx in range(0,128):
    o_data_R = np.append(o_data_R,np.array([f2_R(idx)]),axis=0)
a = o_data_R.T.tolist()

one = f2_R(0).tolist()